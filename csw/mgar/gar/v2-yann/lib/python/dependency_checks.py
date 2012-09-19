# $Id$

import checkpkg
import os.path
import re
import ldd_emul
import sharedlib_utils
import common_constants
import operator
import logging

# This shared library is present on Solaris 10 on amd64, but it's missing on
# Solaris 8 on i386.  It's okay if it's missing.
ALLOWED_ORPHAN_SONAMES = set([u"libm.so.2"])

DEPRECATED_LIBRARY_LOCATIONS = (
    ("/opt/csw/lib", "libdb-4.7.so", "Deprecated Berkeley DB location"),
    ("/opt/csw/lib/mysql", "libmysqlclient_r.so.15",
     "Please use /opt/csw/mysql5/..."),
    ("/opt/csw/lib/mysql", "libmysqlclient.so.15",
     "Please use /opt/csw/mysql5/..."),
    ("/opt/csw/lib", "libnet.so",
     "Please use -L/opt/csw/lib/libnet-new for linking. "
     "See more at http://wiki.opencsw.org/project-libnet"),
)

DLOPEN_LIB_LOCATIONS = (
    r'^opt/csw/lib/python/site-packages.*',
)

DEPENDENCY_FILENAME_REGEXES = (
    (r".*\.pl$",   (u"CSWperl",)),
    (r".*\.pm$",   (u"CSWperl",)),
    (r".*\.py$",   (u"CSWpython",)),
    (r".*\.rb$",   (u"CSWruby", u"CSWruby18", u"CSWruby191", u"CSWlibruby1-9-1-1")),
    (r".*\.elc?$", (u"CSWemacscommon",)),
    (r"/opt/csw/apache2/", (u"CSWapache2",)),
)

PREFERRED_DIRECTORY_PROVIDERS = set([u"CSWcommon"])

BASE_SOLARIS_LIBRARIES = (
     "libsocket.so.1", "libnsl.so.1", "libdl.so.1", "librt.so.1", "libresolv.so.2", "libpthread.so.1",
     # linked by default with C++, see "Default C++ Libraries" in Solaris Studio C++ User'sGuide
     "libCstd.so.1", "libCrun.so.1", "libm.so.1", "libm.so.2", "libw.so.1", "libcx.so.1", "libc.so.1", "libC.so.3", "libC.so.5",
)

ALLOWED_VERSION_DEPENDENCIES = {
    "libc.so.1": ['SYSVABI_1.3', 'SUNWprivate_1.1', 'SUNW_1.22.6',
                  'SUNW_1.22.5', 'SUNW_1.22.4', 'SUNW_1.22.3', 'SUNW_1.22.2',
                  'SUNW_1.22.1', 'SUNW_1.22', 'SUNW_1.21.3', 'SUNW_1.21.2',
                  'SUNW_1.21.1', 'SUNW_1.21', 'SUNW_1.20.4', 'SUNW_1.20.1',
                  'SUNW_1.20', 'SUNW_1.19', 'SUNW_1.18.1', 'SUNW_1.18',
                  'SUNW_1.17', 'SUNW_1.16', 'SUNW_1.15', 'SUNW_1.14',
                  'SUNW_1.13', 'SUNW_1.12', 'SUNW_1.11', 'SUNW_1.10',
                  'SUNW_1.9', 'SUNW_1.8', 'SUNW_1.7', 'SUNW_1.6', 'SUNW_1.5',
                  'SUNW_1.4', 'SUNW_1.3', 'SUNW_1.2', 'SUNW_1.1', 'SUNW_0.9',
                  'SUNW_0.8', 'SUNW_0.7', 'SISCD_2.3'],
}


def ProcessSoname(
    ldd_emulator,
    soname, path_and_pkg_by_basename, binary_info, isalist, binary_path, logger,
    error_mgr,
    pkgname, messenger):
  """This is not an ideal name for this function.

  Returns:
    orphan_sonames
  """
  logging.debug("ProcessSoname(), %s %s"
                % (binary_info["path"], soname))
  orphan_sonames = []
  resolved = False
  path_list = path_and_pkg_by_basename[soname].keys()
  runpath_tuple = (
      tuple(binary_info["runpath"])
      + tuple(checkpkg.SYS_DEFAULT_RUNPATH))
  runpath_history = []
  first_lib = None
  already_resolved_paths = set()
  for runpath in runpath_tuple:
    runpath = ldd_emulator.SanitizeRunpath(runpath)
    runpath_list = ldd_emulator.ExpandRunpath(runpath, isalist, binary_path)
    runpath_list = ldd_emulator.Emulate64BitSymlinks(runpath_list)
    # To accumulate all the runpaths that we were looking at
    runpath_history += runpath_list
    resolved_path = ldd_emulator.ResolveSoname(runpath_list,
                                               soname,
                                               isalist,
                                               path_list,
                                               binary_path)
    if resolved_path:
      if resolved_path in already_resolved_paths:
        continue
      already_resolved_paths.add(resolved_path)
      resolved = True
      reason = ("%s needs the %s soname"
                % (binary_info["path"], soname))
      logger.debug("soname %s found in %s for %s"
                   % (soname, resolved_path, binary_info["path"]))
      error_mgr.NeedFile(pkgname, os.path.join(resolved_path, soname), reason)
      # Looking for deprecated libraries.  However, only alerting if the
      # deprecated library is the first one found in the RPATH.  For example,
      # libdb-4.7.so is found in CSWbdb and CSWbdb47, and it's important to
      # throw an error if the RPATH is ("/opt/csw/lib", "/opt/csw/bdb47/lib"),
      # and not to throw an error if RPATH is ("/opt/csw/bdb47/lib",
      # "/opt/csw/lib")
      if not first_lib:
        first_lib = (resolved_path, soname)
        for bad_path, bad_soname, msg in DEPRECATED_LIBRARY_LOCATIONS:
          if resolved_path == bad_path and soname == bad_soname:
            logger.debug("Bad lib found: %s/%s", bad_path, bad_soname)
            error_mgr.ReportError(
                pkgname,
                "deprecated-library",
                ("file=%s lib=%s/%s"
                 % (binary_info["path"], resolved_path, soname)))
            messenger.Message(
                "Binary %s links to a deprecated library %s/%s. %s"
                % (binary_info["path"], resolved_path, soname, msg))
  if not resolved:
    orphan_sonames.append((soname, binary_info["path"]))
    if path_list:
      path_msg = "was available at the following paths: %s." % path_list
    else:
      path_msg = ("was not present on the filesystem, "
                  "nor in the packages under examination.")
    if soname not in ALLOWED_ORPHAN_SONAMES:
      messenger.Message(
          "%s could not be resolved for %s, with rpath %s, expanded to %s, "
          "while the file %s"
          % (soname, binary_info["path"],
             runpath_tuple, runpath_history, path_msg))
  return orphan_sonames


def Libraries(pkg_data, error_mgr, logger, messenger, path_and_pkg_by_basename,
              pkg_by_path):
  """Checks shared libraries.

  Returns:
    [
      (u"CSWfoo", "why is this needed"),
    ]

  New idea, a list of reasons:
    [
      [(u"CSWfoo", "why is it needed"),
       (u"CSWfooalt", "there must be a reason"),
       (u"CSWfooyetanother", "here's another one")],
      [(u"CSWbar", "this serves another purpose")],
    ]
  """
  pkgname = pkg_data["basic_stats"]["pkgname"]
  logger.debug("Libraries(): pkgname = %s", repr(pkgname))
  isalist = pkg_data["isalist"]
  ldd_emulator = ldd_emul.LddEmulator()
  orphan_sonames = []
  for binary_info in pkg_data["binaries_dump_info"]:
    binary_path, binary_basename = os.path.split(binary_info["path"])
    for soname in binary_info["needed sonames"]:
      orphan_sonames_tmp = ProcessSoname(
          ldd_emulator,
          soname, path_and_pkg_by_basename, binary_info, isalist, binary_path, logger,
          error_mgr,
          pkgname, messenger)
      orphan_sonames.extend(orphan_sonames_tmp)


    ldd_info = pkg_data['ldd_info'][binary_info["path"]]
    for ldd_response in ldd_info:
      if ldd_response['state'] == 'soname-unused' and ldd_response['soname'] not in BASE_SOLARIS_LIBRARIES:
        messenger.Message(
          "Binary %s links to library %s but doesn't seem to use any of its symbols. "
          "It usually happens because superfluous libraries were added to the linker options, "
          "either because of the configure script itself or because of the \"pkg-config --libs\""
          " output of one the dependency."
          % ("/" + binary_info["path"], ldd_response['soname']))
        error_mgr.ReportError(
            pkgname, "soname-unused",
            "%s is needed by %s but never used" % (ldd_response['soname'], "/" + binary_info["path"]))

    # Even when direct binding is enabled, some symbols might not be
    # directly bound because the library explicitely requested the symbol
    # not to be drectly bound to.
    # For example, libc.so.1 does it for symbol sigaction, free, malloc and realloc
    # So we consider that direct binding is enabled if at least one symbol is directly
    # bound to because that definitely means that -B direct or -z direct was used.
    directly_binded = set()
    for syminfo in pkg_data["binaries_elf_info"][binary_info["path"]]['symbol table']:
      if syminfo['external'] and syminfo['flags'] and 'D' in syminfo['flags'] and 'B' in syminfo['flags']:
          directly_binded.add(syminfo['soname'])
    not_directly_binded = directly_binded.symmetric_difference(binary_info["needed sonames"])

    if not_directly_binded:
      messenger.Message(
        "No symbol of binary %s is directly binded against the following libraries: %s. "
        "Please make sure the binaries are compiled using the \"-Bdirect\" linker option."
        % ("/" + binary_info["path"], ", ".join(not_directly_binded)))
      for soname in not_directly_binded:
        error_mgr.ReportError(
          pkgname, "no-direct-binding",
          "%s is not directly binded to soname %s" % ("/" + binary_info["path"], soname))


    for version_dep in pkg_data["binaries_elf_info"][binary_info["path"]]['version needed']:
      if (version_dep['soname'] in ALLOWED_VERSION_DEPENDENCIES and
        not version_dep['version'] in ALLOWED_VERSION_DEPENDENCIES[version_dep['soname']]):
        messenger.Message(
          "Binary %s requires interface version %s in library %s which is only available "
          "in recent Solaris releases."
          % ("/" + binary_info["path"], version_dep['version'], version_dep['soname']))
        error_mgr.ReportError(
          pkgname, "forbidden-version-interface-dependencies",
          "%s requires forbidden interface version %s in library %s"
          % ("/" + binary_info["path"], version_dep['version'], version_dep['soname']))


  orphan_sonames = set(orphan_sonames)
  for soname, binary_path in orphan_sonames:
    if soname not in ALLOWED_ORPHAN_SONAMES:
      error_mgr.ReportError(
          pkgname, "soname-not-found",
          "%s is needed by %s" % (soname, binary_path))


def ByFilename(pkg_data, error_mgr, logger, messenger,
               path_and_pkg_by_basename, pkg_by_path):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  dep_regexes = [(re.compile(x), x, y)
                 for x, y in DEPENDENCY_FILENAME_REGEXES]
  for regex, regex_str, dep_pkgnames in dep_regexes:
    for pkgmap_entry in pkg_data["pkgmap"]:
      if pkgmap_entry["path"] and regex.match(pkgmap_entry["path"]):
        reason = ("found file(s) matching %s, e.g. %s"
               % (regex_str, repr(pkgmap_entry["path"])))
        for dep_pkgname in dep_pkgnames:
          error_mgr.NeedPackage(pkgname, dep_pkgname, reason)
        break


def ByDirectory(pkg_data, error_mgr, logger, messenger,
                path_and_pkg_by_basename, pkg_by_path):
  """Finds packages that provide each directory's parent.

  1. For each directory
    1.1. Find the parent
    1.2. Add the parent to the list of packages to depend on.

  This check is currently disabled, because of false positives that it
  generates.
  """
  pkgname = pkg_data["basic_stats"]["pkgname"]
  req_pkgs_reasons = []
  needed_dirs = set()
  # Adding base dirs of all the files to the dirs that need to be checked.
  for pkgmap_entry in pkg_data["pkgmap"]:
    if "path" in pkgmap_entry and pkgmap_entry["path"]:
      base_dir, dirname = os.path.split(pkgmap_entry["path"])
      needed_dirs.add(base_dir)
  for needed_dir in needed_dirs:
    reason_group = []
    # TODO: The preferred directory providers should not depend on other packages to
    # provide directories.
    if pkgname not in PREFERRED_DIRECTORY_PROVIDERS:
      # If the path is provided by CSWcommon or other preferred package, don't
      # mention other packages.
      pkgs_to_mention = []
      preferred_mentioned = False
      for preferred_pkg in PREFERRED_DIRECTORY_PROVIDERS:
        if preferred_pkg in pkg_by_path[needed_dir]:
          pkgs_to_mention.append(preferred_pkg)
          preferred_mentioned = True
      if not preferred_mentioned:
        if not pkg_by_path[needed_dir]:
          # There's no sense in reporting '/' and ''.
          if needed_dir and needed_dir != '/':
            error_mgr.ReportError(pkgname, "base-dir-not-found", repr(needed_dir))
        elif len(pkg_by_path[needed_dir]) < 5:
          pkgs_to_mention = pkg_by_path[needed_dir]
        else:
          pkgs_to_mention = pkg_by_path[needed_dir][:5] + ["and/or others"]
      msg = (u"%s provides directory %s is needed by the package %s"
             % (pkgs_to_mention, needed_dir, pkgname))
      for pkg_to_mention in pkgs_to_mention:
        reason_group.append((pkg_to_mention, msg))
      if reason_group:
        req_pkgs_reasons.append(reason_group)
    else:
      error_mgr.ReportError(pkgname, "base-dir-not-provided-by-any-package", needed_dir)
  return req_pkgs_reasons


def GetPathAndPkgByBasename(error_mgr, logger, basenames,
                            path_and_pkg_by_basename=None):
  """{"<basename>": {"/path/1": ["CSWfoo1"], "/path/2": ["CSWfoo2"]}}"""
  if not path_and_pkg_by_basename:
    path_and_pkg_by_basename = {}
  for basename in basenames:
    path_and_pkg_by_basename[basename] = (
        error_mgr.GetPathsAndPkgnamesByBasename(basename))
  return path_and_pkg_by_basename

def GetPkgByFullPath(error_mgr, logger, paths_to_verify, pkg_by_path):
  """Resolves a list of paths to a mapping between paths and packages.

  Returns: {"/opt/csw/lib": ["CSWcommon", "CSWfoo"]}
  """
  if not pkg_by_path:
    pkg_by_path = {}
  for path in paths_to_verify:
    if path not in pkg_by_path:
      result = error_mgr.GetPkgByPath(path)
      # logger.warning("error_mgr.GetPkgByPath(%s) => %s", repr(path), repr(result))
      pkg_by_path[path] = result
  # logger.warning("New paths: %s" % pprint.pformat(pkg_by_path))
  return pkg_by_path

def SuggestLibraryPackage(error_mgr, messenger,
    pkgname, catalogname,
    description,
    lib_path, lib_basename, soname,
    base_pkgname):
  escaped_soname = sharedlib_utils.EscapeRegex(soname)
  escaped_basename = sharedlib_utils.EscapeRegex(lib_basename)
  messenger.SuggestGarLine("# The following lines define a new package: "
                           "%s" % pkgname)
  messenger.SuggestGarLine("PACKAGES += %s" % pkgname)
  messenger.SuggestGarLine(
      "CATALOGNAME_%s = %s"
      % (pkgname, catalogname))
  # The exact library file (which can be different from what soname suggests)
  messenger.SuggestGarLine(
      r'PKGFILES_%s += '
      r'$(call baseisadirs,$(libdir),%s)'
      % (pkgname, escaped_basename))
  # Name regex based on the soname, plus potential symlinks
  messenger.SuggestGarLine(
      r'PKGFILES_%s += '
      r'$(call baseisadirs,$(libdir),%s(\.\d+)*)'
      % (pkgname, escaped_soname))
  messenger.SuggestGarLine(
      "SPKG_DESC_%s += $(DESCRIPTION), %s"
      % (pkgname, soname))
  messenger.SuggestGarLine(
      "RUNTIME_DEP_PKGS_%s += %s"
      % (base_pkgname, pkgname))
  messenger.SuggestGarLine(
      "# The end of %s definition" % pkgname)
