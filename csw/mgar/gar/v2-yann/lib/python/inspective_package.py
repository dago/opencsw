import package
import os
import re
import logging
import hachoir_parser
import sharedlib_utils
import magic
import copy
import common_constants
import subprocess
import ldd_emul
import configuration as c

"""This file isolates code dependent on hachoir parser.

hachoir parser takes quite a while to import.
"""

# Suppress unhelpful warnings
# http://bitbucket.org/haypo/hachoir/issue/23
import hachoir_core.config
hachoir_core.config.quiet = True


ROOT_RE = re.compile(r"^(reloc|root)/")


def StripRe(x, strip_re):
  return re.sub(strip_re, "", x)


def GetFileMetadata(file_magic, base_dir, file_path):
  full_path = unicode(os.path.join(base_dir, file_path))
  if not os.access(full_path, os.R_OK):
    return {}
  file_info = {
      "path": StripRe(file_path, ROOT_RE),
      "mime_type": file_magic.GetFileMimeType(full_path)
  }
  if base_dir:
    file_info["path"] = os.path.join(base_dir, file_info["path"])
  if not file_info["mime_type"]:
    logging.error("Could not establish the mime type of %s",
                  full_path)
    # We really don't want that, as it misses binaries.
    msg = (
        "It was not possible to establish the mime type of %s.  "
        "It's a known problem which occurs when indexing a large "
        "number of packages in a single run.  "
        "It's probably caused by a bug in libmagic, or a bug in "
        "libmagic Python bindings. "
        "Currently, there is no fix for it.  "
        "You have to restart your process - it "
        "will probably finish successfully when do you that."
        % full_path)
    raise package.PackageError(msg)
  if sharedlib_utils.IsBinary(file_info):
    parser = hachoir_parser.createParser(full_path)
    if not parser:
      logging.warning("Can't parse file %s", file_path)
    else:
      try:
        file_info["mime_type_by_hachoir"] = parser.mime_type
        machine_id = parser["/header/machine"].value
        file_info["machine_id"] = machine_id
        file_info["endian"] = parser["/header/endian"].display
      except hachoir_core.field.field.MissingField, e:
        logging.warning(
            "Error in hachoir_parser processing %s: %r", file_path, e)
  return file_info


class InspectivePackage(package.DirectoryFormatPackage):
  """Extends DirectoryFormatPackage to allow package inspection."""

  def GetFilesMetadata(self):
    """Returns a data structure with all the files plus their metadata.

    [
      {
        "path": ...,
        "mime_type": ...,
      },
    ]
    """
    if not self.files_metadata:
      self.CheckPkgpathExists()
      self.files_metadata = []
      files_root = self.GetFilesDir()
      all_files = self.GetAllFilePaths()
      file_magic = FileMagic()
      basedir = self.GetBasedir()
      for file_path in all_files:
        full_path = unicode(self.MakeAbsolutePath(file_path))
        file_info = GetFileMetadata(file_magic, self.pkgpath, full_path)
        # To prevent files from containing the full temporary path.
        file_info["path"] = StripRe(file_path, ROOT_RE)
        self.files_metadata.append(file_info)
    return self.files_metadata

  def ListBinaries(self):
    """Lists all the binaries from a given package.

    Original checkpkg code:

    #########################################
    # find all executables and dynamic libs,and list their filenames.
    listbinaries() {
      if [ ! -d $1 ] ; then
        print errmsg $1 not a directory
        rm -rf $EXTRACTDIR
        exit 1
      fi
      find $1 -print | xargs file |grep ELF |nawk -F: '{print $1}'
    }

    Returns a list of absolute paths.

    Now that there are files_metadata, this function can safely go away, once
    all its callers are modified to use files_metadata instead.
    """
    if self.binaries is None:
      self.CheckPkgpathExists()
      files_metadata = self.GetFilesMetadata()
      self.binaries = []
      # The nested for-loop looks inefficient.
      for file_info in files_metadata:
        if sharedlib_utils.IsBinary(file_info):
          self.binaries.append(file_info["path"])
      self.binaries.sort()
    return self.binaries

  def GetPathsInSubdir(self, remove_prefix, subdir):
    file_paths = []
    for root, dirs, files in os.walk(os.path.join(self.pkgpath, subdir)):
      full_paths = [os.path.join(root, f) for f in files]
      file_paths.extend([f.replace(remove_prefix, "") for f in full_paths])
    return file_paths

  def GetAllFilePaths(self):
    """Returns a list of all paths from the package."""
    if not self.file_paths:
      # Support for relocatable packages
      basedir = self.GetBasedir()
      self.CheckPkgpathExists()
      remove_prefix = "%s/" % self.pkgpath
      self.file_paths = self.GetPathsInSubdir(remove_prefix, "root")
      if self.RelocPresent():
        self.file_paths += self.GetPathsInSubdir(remove_prefix, "reloc")
    return self.file_paths

  def RelocPresent(self):
    return os.path.exists(os.path.join(self.directory, "reloc"))

  def GetFilesDir(self):
    """Returns the subdirectory in which files, are either "reloc" or "root"."""
    if self.RelocPresent():
      return "reloc"
    else:
      return "root"

  def GetBinaryDumpInfo(self):
    # Binaries. This could be split off to a separate function.
    # man ld.so.1 for more info on this hack
    env = copy.copy(os.environ)
    env["LD_NOAUXFLTR"] = "1"
    binaries_dump_info = []
    basedir = self.GetBasedir()
    for binary in self.ListBinaries():
      # Relocatable packages complicate things. Binaries returns paths with
      # the basedir, but files in reloc are in paths without the basedir, so
      # we need to strip that bit.
      binary_in_tmp_dir = binary
      if basedir:
        binary_in_tmp_dir = binary_in_tmp_dir[len(basedir):]
        binary_in_tmp_dir = binary_in_tmp_dir.lstrip("/")
      binary_abs_path = os.path.join(self.directory, self.GetFilesDir(), binary_in_tmp_dir)
      binary_base_name = os.path.basename(binary_in_tmp_dir)
      args = [common_constants.DUMP_BIN, "-Lv", binary_abs_path]
      logging.debug("Running: %s", args)
      dump_proc = subprocess.Popen(args, stdout=subprocess.PIPE, env=env)
      stdout, stderr = dump_proc.communicate()
      ret = dump_proc.wait()
      binary_data = ldd_emul.ParseDumpOutput(stdout)
      binary_data["path"] = binary
      if basedir:
        binary_data["path"] = os.path.join(basedir, binary_data["path"])
      binary_data["base_name"] = binary_base_name
      binaries_dump_info.append(binary_data)
    return binaries_dump_info

  def GetDefinedSymbols(self):
    """Returns text symbols (i.e. defined functions) for packaged ELF objects

    To do this we parse output lines from nm similar to the following. "T"s are
    the definitions which we are after.

      0000104000 D _lib_version
      0000986980 D _libiconv_version
      0000000000 U abort
      0000097616 T aliases_lookup
    """
    binaries = self.ListBinaries()
    defined_symbols = {}

    for binary in binaries:
      binary_abspath = os.path.join(self.directory, "root", binary)
      # Get parsable, ld.so.1 relevant SHT_DYNSYM symbol information
      args = ["/usr/ccs/bin/nm", "-p", "-D", binary_abspath]
      nm_proc = subprocess.Popen(
          args,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE)
      stdout, stderr = nm_proc.communicate()
      retcode = nm_proc.wait()
      if retcode:
        logging.error("%s returned an error: %s", args, stderr)
        continue
      nm_out = stdout.splitlines()

      defined_symbols[binary] = []
      for line in nm_out:
        sym = self._ParseNmSymLine(line)
        if not sym:
          continue
        if sym['type'] not in ("T", "D", "B"):
          continue
        defined_symbols[binary].append(sym['name'])

    return defined_symbols

  def GetBinaryElfInfo(self):
    """Returns various informations symbol and version present in elf header

    To do this we parse output lines from elfdump -syv, it's the
    only command that will give us all informations we need on symbols and versions.
    We will analyse 3 sections:
     - version section: contains soname needed, version interface required for each soname,
                        and version definition
     - symbol table section: contains list of symbol and soname/version interface providing it
                             (the latter is an index in the version section)
     - syminfo section: contains special linking flags for each symbol
    """
    binaries = self.ListBinaries()
    binaries_elf_info = {}

    for binary in binaries:
      binary_abspath = os.path.join(self.directory, "root", binary)
      # elfdump is the only tool that give us all informations
      args = ["/usr/ccs/bin/elfdump", "-svy", binary_abspath]
      elfdump_proc = subprocess.Popen(
          args,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE)
      stdout, stderr = elfdump_proc.communicate()
      retcode = elfdump_proc.wait()
      if retcode or stderr:
        logging.error("%s returned one or more errors: %s", args, stderr.splitlines()[0])
        continue
      elfdump_out = stdout.splitlines()

      symbols = {}
      binary_info = {'version definition': [],
                     'version needed': [],
                     'symbol table': []}
      # we will merge syminfo and symbol table information in one list
      # so the syminfo list is the same as the symbol table one
      binary_info['syminfo'] = binary_info['symbol table']

      # The list of fields we want to retrieve in the elfdump output by section
      # if the field is a tuple, it means we will map the original field name
      # to another name in the final data structure
      elf_fields = {'version definition': ['version', 'dependency'],
                    'version needed': [('file', 'soname'), 'version'],
                    'symbol table': [('name', 'symbol'), ('ver', 'version'),
                                     'bind', ('shndx', 'external')],
                    'syminfo': [('library', 'soname'), 'symbol', 'flags']}

      cur_section = None
      for line in elfdump_out:

        elfdump_data, cur_section = self._ParseElfdumpLine(line, cur_section)

        # header or blank line contains no information
        if not elfdump_data:
          continue

        elf_info = {}
        for field in elf_fields[cur_section]:
          if type(field) == tuple:
            elf_info[field[1]] = elfdump_data[field[0]]
          else:
            elf_info[field] = elfdump_data[field]

        # we merge symbol table and syminfo informations so we have to check
        # if the symbol has not already been added
        if cur_section in ('symbol table', 'syminfo'):
          if not elf_info['symbol']:
            continue
          if elf_info['symbol'] in symbols:
            symbols[elf_info['symbol']].update(elf_info)
            continue
          else:
            symbols[elf_info['symbol']] = elf_info

        binary_info[cur_section].append(elf_info)

      # elfdump doesn't repeat the name of the soname in the version section
      # if it's the same on two contiguous line, so we have to make sure
      # the information is present in each entry
      for i, version in enumerate(binary_info['version needed'][1:]):
        if not version['soname']:
          version['soname'] = binary_info['version needed'][i]['soname']

      # if it exists, the first "version definition" entry is the base soname
      # we don't need this information
      if binary_info['version definition']:
        binary_info['version definition'].pop(0)

      # To not rely of the section order output of elfdump, we resolve symbol version
      # informations here after having parsed all elfdump output
      nb_versions_definition = len(binary_info['version definition'])
      for sym_info in binary_info['symbol table']:
        version_index = int(sym_info['version']) - 2
        if version_index > 1:
          if version_index < nb_versions_definition:
            version = binary_info['version definition'][version_index]
          else:
            version = binary_info['version needed'][version_index - nb_versions_definition]
            sym_info['version'] = version['version']
            sym_info['soname'] = version['soname']
        else:
          sym_info['version'] = None

        if sym_info['external'] == 'UNDEF':
          sym_info['external'] = True
        else:
          sym_info['external'] = False

        # we make sure the field are present even if the syminfo section is not
        sym_info.setdefault('soname')
        sym_info.setdefault('flags')

      binaries_elf_info[binary] = binary_info

    return binaries_elf_info

  def GetLddMinusRlines(self):
    """Returns ldd -r output."""
    binaries = self.ListBinaries()
    ldd_output = {}
    for binary in binaries:
      binary_abspath = os.path.join(self.directory, "root", binary)
      # this could be potentially moved into the DirectoryFormatPackage class.
      # ldd needs the binary to be executable
      os.chmod(binary_abspath, 0755)
      args = ["ldd", "-Ur", binary_abspath]
      ldd_proc = subprocess.Popen(
          args,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE)
      stdout, stderr = ldd_proc.communicate()
      retcode = ldd_proc.wait()
      if retcode:
        uname_info = os.uname()
        if (uname_info[2] == '5.9' and uname_info[4] == 'i86pc' and
            '/amd64/' in binary_abspath and 'has wrong class or data encoding' in stderr):
          # we are trying to analyze a 64 bits binary on a Solaris 9 x86
          # which exists only in 32 bits, that's not possible
          # we ignore the error and return no information as it is likely
          # that the ldd infos will be the same on the 32 bits binaries analyzed
          return {}
        else:
          logging.error("%s returned an error: %s", args, stderr)

      ldd_info = []
      for line in stdout.splitlines():
        result = self._ParseLddDashRline(line, binary_abspath)
        if result:
          ldd_info.append(result)
        ldd_output[binary] = ldd_info

      return ldd_output

  def _ParseNmSymLine(self, line):
    re_defined_symbol = re.compile('[0-9]+ [ABDFNSTU] \S+')
    m = re_defined_symbol.match(line)
    if not m:
      return None
    fields = line.split()
    sym = { 'address': fields[0], 'type': fields[1], 'name': fields[2] }
    return sym

  def _ParseElfdumpLine(self, line, section=None):

    headers_re = (r'(?P<section>Version Needed|Version Definition|Symbol Table|Syminfo) Section:\s+(?:\.SUNW_version|\.dynsym|\.SUNW_syminfo|.symtab)\s*$|'
                   '\s*(?:index\s+)?version\s+dependency\s*$|'
                   '\s*(?:index\s+)?file\s+version\s*$|'
                   '\s*index\s*value\s+size\s+type\s+bind\s+oth\s+ver\s+shndx\s+name\s*$|'
                   '\s*index\s+flags\s+bound to\s+symbol\s*$|'
                   '\s*$')

    re_by_section = { 'version definition': (r'\s*(?:\[(?P<index>\d+)\]\s+)?(?P<version>.*\S)\s+(?P<dependency>\S+)?\s*$'),
                      'version needed': (r'\s*(?:\[(?P<index>\d+)\]\s+)?(?:(?P<file>\S+)\s+(?!\[ (?:INFO|WEAK) \]))?(?P<version>\S+)(?:\s+\[ (?:INFO|WEAK) \])?\s*$'),
                      'symbol table': (r'\s*\[\d+\]\s+(?:0x[0-9a-f]+|REG_G\d+)\s+0x[0-9a-f]+\s+\S+\s+(?P<bind>\S+)\s+\S+\s+(?P<ver>\S+)\s+(?P<shndx>\S+)\s+(?P<name>\S+)?\s*$'),
                      'syminfo': (r'\s*\[\d+\]\s+(?P<flags>[ABCDFILNPS]+)\s+(?:(?:\[\d+\]\s+(?P<library>.*\S)|<self>)\s+)?(?P<symbol>.*\S)\s*') }

    elfdump_data = None
    m = re.match(headers_re, line)
    if m:
      if m.lastindex:
        section = m.group('section').lower()
    elif section:
      m = re.match(re_by_section[section], line)
      if m:
        elfdump_data = m.groupdict()

    if not m:
      raise package.StdoutSyntaxError("Could not parse %s" % (repr(line)))

    return elfdump_data, section

  def _ParseLddDashRline(self, line, binary=None):
    found_re = r"^\t(?P<soname>\S+)\s+=>\s+(?P<path_found>\S+)"
    symbol_not_found_re = (r"^\tsymbol not found:\s(?P<symbol>\S+)\s+"
                           r"\((?P<path_not_found>\S+)\)")
    only_so = r"^\t(?P<path_only>\S+)$"
    version_so = (r'^\t(?P<soname_version_not_found>\S+) '
                  r'\((?P<lib_name>\S+)\) =>\t \(version not found\)')
    stv_protected = (r'^\trelocation \S+ symbol: (?P<relocation_symbol>\S+): '
                     r'file (?P<relocation_path>\S+): '
                     r'relocation bound to a symbol '
                     r'with STV_PROTECTED visibility$')
    sizes_differ = (r'^\trelocation \S+ sizes differ: '
                    r'(?P<sizes_differ_symbol>\S+)$')
    sizes_info = (r'^\t\t\(file (?P<sizediff_file1>\S+) size=(?P<size1>0x\w+); '
                  r'file (?P<sizediff_file2>\S+) size=(?P<size2>0x\w+)\)$')
    sizes_one_used = (r'^\t\t(?P<sizediffused_file>\S+) size used; '
                      r'possible insufficient data copied$')
    unreferenced_object = (r'^\s*unreferenced object=(?P<object>.*); unused dependency of (?P<binary>.*)$')
    unused_object = (r'^\s*unused object=.*$')
    unused_search_path = (r'^\s*unused search path=.*  \(RUNPATH/RPATH from file .*\)$')
    blank_line = (r'^\s*$')
    common_re = (r"(%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s)"
                 % (found_re, symbol_not_found_re, only_so, version_so, stv_protected, sizes_differ, sizes_info,
                    sizes_one_used, unreferenced_object, unused_object, unused_search_path, blank_line))
    m = re.match(common_re, line)
    response = None
    if m:
      response = {}
      d = m.groupdict()
      if "soname" in d and d["soname"]:
        # it was found
        response["state"] = "OK"
        response["soname"] = d["soname"]
        response["path"] = d["path_found"]
        response["symbol"] = None
      elif "symbol" in d and d["symbol"]:
        response["state"] = "symbol-not-found"
        response["soname"] = None
        response["path"] = d["path_not_found"]
        response["symbol"] = d["symbol"]
      elif "binary" in d and d["binary"] and binary == d["binary"]:
        response["state"] = "soname-unused"
        response["soname"] = os.path.basename(d["object"])
        response["path"] = None
        response["symbol"] = None
      elif d["path_only"]:
        response["state"] = "OK"
        response["soname"] = None
        response["path"] = d["path_only"]
        response["symbol"] = None
      elif d["soname_version_not_found"]:
        response["state"] = "version-not-found"
        response["soname"] = d["soname_version_not_found"]
        response["path"] = None
        response["symbol"] = None
      elif d["relocation_symbol"]:
        response["state"] = 'relocation-bound-to-a-symbol-with-STV_PROTECTED-visibility'
        response["soname"] = None
        response["path"] = d["relocation_path"]
        response["symbol"] = d["relocation_symbol"]
      elif d["sizes_differ_symbol"]:
        response["state"] = 'sizes-differ'
        response["soname"] = None
        response["path"] = None
        response["symbol"] = d["sizes_differ_symbol"]
      elif d["sizediff_file1"]:
        response["state"] = 'sizes-diff-info'
        response["soname"] = None
        response["path"] = "%s %s" % (d["sizediff_file1"], d["sizediff_file2"])
        response["symbol"] = None
      elif d["sizediffused_file"]:
        response["state"] = 'sizes-diff-one-used'
        response["soname"] = None
        response["path"] = "%s" % (d["sizediffused_file"])
        response["symbol"] = None

    else:
      raise package.StdoutSyntaxError("Could not parse %s with %s"
                                      % (repr(line), common_re))

    return response

  def GetDependencies(self):
    """Gets dependencies information.

    Returns:
      A tuple of (list, list) of depends and i_depends.
    """
    # The collection of dependencies needs to be a list (as opposed to
    # a set) because there might be duplicates and it's necessary to
    # carry that information.
    depends = []
    i_depends = []
    depend_file_path = os.path.join(self.directory, "install", "depend")
    if os.path.exists(depend_file_path):
      with open(depend_file_path, "r") as fd:
        for line in fd:
          fields = re.split(c.WS_RE, line)
          if len(fields) < 2:
            logging.warning("Bad depends line: %s", repr(line))
          if fields[0] == "P":
            pkgname = fields[1]
            pkg_desc = " ".join(fields[1:])
            depends.append((pkgname, pkg_desc))
          if fields[0] == "I":
            pkgname = fields[1]
            i_depends.append(pkgname)
    return depends, i_depends

  def GetObsoletedBy(self):
    """Collects obsolescence information from the package if it exists

    Documentation:
    http://wiki.opencsw.org/obsoleting-packages

    Returns:

    A dictionary of "has_obsolete_info", "syntax_ok" and
    "obsoleted_by" where obsoleted_by is a list of (pkgname,
    catalogname) tuples and has_obsolete_info and syntax_ok are
    booleans.

    If the package has not been obsoleted or the package predates the
    implementation of this mechanism, obsoleted_by is an empty list
    and has_obsolete_info will be False.

    If the package provides obsolescence information but the format of
    the information is invalid, syntax_ok will be False and the list
    may be empty.  It will always contain the valid entries.
    """

    has_obsolete_info = False
    obsoleted_syntax_ok = True
    obsoleted_by = []
    obsoleted_by_path = os.path.join(self.directory, "install", "obsolete")

    if os.path.exists(obsoleted_by_path):
      has_obsolete_info = True
      with open(obsoleted_by_path, "r") as fd:
        for line in fd:
          fields = re.split(c.WS_RE, line)
          if len(fields) < 2:
            obsoleted_syntax_ok = False
            logging.warning("Bad line in obsolete file: %s", repr(line))
            continue
          pkgname, catalogname = fields[0:2]
          obsoleted_by.append((pkgname, catalogname))

    return { "syntax_ok": obsoleted_syntax_ok,
             "obsoleted_by": obsoleted_by,
             "has_obsolete_info": has_obsolete_info }


class FileMagic(object):
  """Libmagic sometimes returns None, which I think is a bug.
  Trying to come up with a way to work around that.  It might not even be
  very helpful, but at least detects the issue and tries to work around it.
  """

  def __init__(self):
    self.cookie_count = 0
    self.magic_cookie = None

  def _GetCookie(self):
    magic_cookie = magic.open(self.cookie_count)
    self.cookie_count += 1
    magic_cookie.load()
    if "MAGIC_MIME" in dir(magic):
      flag = magic.MAGIC_MIME
    elif "MIME" in dir(magic):
      flag = magic.MIME
    magic_cookie.setflags(flag)
    return magic_cookie

  def _LazyInit(self):
    if not self.magic_cookie:
      self.magic_cookie = self._GetCookie()

  def GetFileMimeType(self, full_path):
    """Trying to run magic.file() a few times, not accepting None."""
    self._LazyInit()
    mime = None
    for i in xrange(10):
      mime = self.magic_cookie.file(full_path)
      if mime:
        break;
      else:
        # Returned mime is null. Re-initializing the cookie and trying again.
        logging.error("magic_cookie.file(%s) returned None. Retrying.",
                      full_path)
        self.magic_cookie = self._GetCookie()
        # In practice, this retrying doesn't help.  There seems to be
        # something process-related which prevents libmagic from
        # functioning.  The only known workaround is to shutdown the
        # process and run it again.
        #
        # The issues have been observed with file-5.04.
    return mime


class InspectiveCswSrv4File(package.CswSrv4File):
  """Allows to get the inspective version of the dir format pkg."""

  # The presence of this method makes it explicit that we want an inspective
  # version of the directory format package.
  def GetInspectivePkg(self):
    return self.GetDirFormatPkg()

  def GetDirFormatClass(self):
    return InspectivePackage
