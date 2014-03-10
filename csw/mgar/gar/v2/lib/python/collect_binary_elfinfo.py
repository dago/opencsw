#!/opt/csw/bin/python2.6

import hashlib
import io
import json
import logging
import optparse
import os
import sys
import collections
import mmap

from elftools.elf.elffile import ELFFile
from elftools.elf.constants import SUNW_SYMINFO_FLAGS
from elftools.elf.enums import ENUM_E_MACHINE
from elftools.elf.descriptions import (
  describe_symbol_type, describe_symbol_bind,
  describe_symbol_shndx, describe_syminfo_flags
)
from elftools.common.exceptions import ELFParseError

from lib.python import configuration
from lib.python import errors
from lib.python import rest
from lib.python import representations


class ElfExtractor(object):

  sh_type2name = {'SHT_SUNW_syminfo': 'syminfo', 'SHT_DYNSYM': 'symbols',
                  'SHT_GNU_verneed': 'verneed', 'SHT_GNU_verdef': 'verdef',
                  'SHT_GNU_versym': 'versym', 'SHT_DYNAMIC': 'dynamic'}

  def __init__(self, binary_path, debug=False):
    self.debug = debug
    self._binary_path = binary_path
    self.config = configuration.GetConfig()
    username, password = rest.GetUsernameAndPassword()
    self.rest_client = rest.RestClient(
        pkgdb_url=self.config.get('rest', 'pkgdb'),
        releases_url=self.config.get('rest', 'releases'),
        username=username,
        password=password)
    fd = open(self._binary_path, 'rb')
    self._mmap = mmap.mmap(fd.fileno(), 0, access=mmap.PROT_READ)
    self._elffile = ELFFile(self._mmap)

  def _compute_md5_sum(self):
    md5_hash = hashlib.md5()
    md5_hash.update(self._mmap)
    return md5_hash.hexdigest()

  def _get_sections_of_interest(self, *names):
    """ Find and returns the given sections based on their short names
    """
    sections = {}
    for section in self._elffile.iter_sections():
      if section.header['sh_type'] in ElfExtractor.sh_type2name:
        name = ElfExtractor.sh_type2name[section.header['sh_type']]
        if name in names:
          sections[name] = section

    return sections

  def _describe_symbol_shndx(self, shndx):
    """ We use our own instead of the one provided by pyelftools.
        This one resolves the section name if shndx is a section index
        and it outputs the same string as elfdump in the other cases.
    """
    if isinstance(shndx, int):
      try:
        return self._elffile.get_section(shndx).name
      except (ELFParseError, ValueError):
        # The elf file is a bit corrupt, the shndx refers
        # to a non-existing section. There are some existing
        # binaries with this issue is the repository so
        # we just skip the problem and return the section number
        return str(shndx)
    else:
      return shndx[4:]

  def _describe_symbol_boundto(self, syminfo):
    """ We use our own instead of the one provided by pyelftools.
        because we only want here to display the related library
        referenced in the dynamic section.
    """
    dynamic_section = self._elffile.get_section_by_name('.dynamic')
    if syminfo['si_flags'] & SUNW_SYMINFO_FLAGS.SYMINFO_FLG_FILTER:
      return dynamic_section.get_tag(syminfo['si_boundto']).sunw_filter
    else:
      return dynamic_section.get_tag(syminfo['si_boundto']).needed

  def CollectBinaryElfinfo(self):
    """Returns various informations symbol and versions present in elf header
    We will analyse 5 sections:
     - version definitions and
       version needed: contains version interface defined for this binary
                       and for each required soname, the version interfaces
                       required
     - symbol table: contains list of symbol name
     - version symbol table: maps the symbol against version interface
     - syminfo: contains special linking flags for each symbol
    The amount of data might be too large for it to fit in memory at one time,
    therefore the rest_client is passed to facilitate saving data.
    """
    md5_sum = self._compute_md5_sum()
    if self.rest_client.BlobExists('elfdump', md5_sum):
      logging.debug('We already have info about %r.', self._binary_path)
      return md5_sum

    sections = self._get_sections_of_interest('verneed', 'verdef',
                                              'syminfo', 'symbols')
    versions_needed = []
    if 'verneed' in sections:
      for verneed, vernaux_iter in sections['verneed'].iter_versions():
        versions_needed.extend([{'index': vernaux['vna_other'],
                                 'soname': verneed.name,
                                 'version': vernaux.name}
                                for vernaux in vernaux_iter])

      versions_needed.sort(key=lambda x: x['index'])
      for version in versions_needed:
        del version['index']

    version_definitions = []
    if 'verdef' in sections:
      for verdef, verdaux_iter in sections['verdef'].iter_versions():
        version_name = verdaux_iter.next().name
        dependencies = [x.name for x in verdaux_iter]
        version_definitions.append({'index': verdef['vd_ndx'],
                                    'version': version_name,
                                    'dependencies': dependencies})

      if version_definitions:
        version_definitions.sort(key=lambda x: x['index'])
        # the first "version definition" entry is the base soname
        # we don't care about this information
        version_definitions.pop(0)
        for version in version_definitions:
          del version['index']

    symbols = []
    if 'symbols' in sections:
      versions_info = (version_definitions + versions_needed)
      symbol_iter = sections['symbols'].iter_symbols()
      # We skip the first symbol which is always the 'UNDEF' symbol entry
      symbol_iter.next()
      for index, sym in enumerate(symbol_iter, start=1):

        symbol = {'bind': describe_symbol_bind(sym['st_info']['bind']),
                  'shndx': self._describe_symbol_shndx(sym['st_shndx']),
                  'symbol': sym.name,
                  'flags': None, 'soname': None, 'version': None}

        if 'versym' in sections:
          versym = sections['versym'].get_symbol(index)
          if not versym['ndx'] in ['VER_NDX_LOCAL', 'VER_NDX_GLOBAL']:
            # if versym is 2 or more, it's an index on the version
            # definition and version needed tables
            version = versions_info[versym['ndx'] - 2]
            symbol['version'] = version['version']
            if 'soname' in version:
              symbol['soname'] = version['soname']

        if 'syminfo' in sections:
          syminfo = sections['syminfo'].get_symbol(index)
          # We only use the information from syminfo if:
          # - there is at least one flag that uses the boundto value,
          # - boundto is an index and not special value (SYMINFO_BT_SELF...)
          if (syminfo['si_flags'] & (
                SUNW_SYMINFO_FLAGS.SYMINFO_FLG_DIRECT |
                SUNW_SYMINFO_FLAGS.SYMINFO_FLG_DIRECTBIND |
                SUNW_SYMINFO_FLAGS.SYMINFO_FLG_LAZYLOAD |
                SUNW_SYMINFO_FLAGS.SYMINFO_FLG_FILTER)
              and isinstance(syminfo['si_boundto'], int)):
            symbol['flags'] = describe_syminfo_flags(syminfo['si_flags'])
            symbol['soname'] = self._describe_symbol_boundto(syminfo)

        symbols.append(representations.ElfSymInfo(**symbol))

      symbols.sort(key=lambda m: m.symbol)

    binary_info = {'version definition': version_definitions,
                   'version needed': versions_needed,
                   'symbol table': symbols}
    self.rest_client.SaveBlob('elfdump', md5_sum, binary_info)
    return md5_sum

  def CollectBinaryDumpinfo(self):
    """Returns informations about soname and runpath located in
       the dynamic section.
    """
    binary_dump_info = {'needed_sonames': [],
                        'runpath': [],
                        'rpath': [],
                        'soname': None}

    sections = self._get_sections_of_interest('dynamic')
    if 'dynamic' in sections:

      for dyn_tag in sections['dynamic'].iter_tags():
        if dyn_tag['d_tag'] == 'DT_NEEDED':
          binary_dump_info['needed_sonames'].append(dyn_tag.needed)
        elif dyn_tag['d_tag'] == 'DT_RUNPATH':
          binary_dump_info['runpath'].extend(dyn_tag.runpath.split(':'))
        elif dyn_tag['d_tag'] == 'DT_RPATH':
          binary_dump_info['rpath'].extend(dyn_tag.rpath.split(':'))
        elif dyn_tag['d_tag'] == 'DT_SONAME':
          binary_dump_info['soname'] = dyn_tag.soname

    return binary_dump_info

  def GetMachineIdOfBinary(self):
    e_machine = self._elffile.header['e_machine']
    if e_machine not in ENUM_E_MACHINE:
      logging.warning('%r not found in ENUM_E_MACHINE in elftools; '
                      'resetting to EM_NONE', e_machine)
      e_machine = 'EM_NONE'
    return ENUM_E_MACHINE[e_machine]


if __name__ == '__main__':
  parser = optparse.OptionParser()
  parser.add_option("-i", "--input", dest="input_file",
                    help="Input file")
  parser.add_option("--debug", dest="debug",
                    action="store_true", default=False)
  options, args = parser.parse_args()
  if not options.input_file:
    sys.stdout.write("Please provide input file name. See --help\n")
    sys.exit(1)
  logging_level = logging.INFO
  if options.debug:
    logging_level = logging.DEBUG
  fmt = '%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(message)s'
  logging.basicConfig(format=fmt, level=logging_level)
  extractor = ElfExtractor(options.input_file, debug=options.debug)
  md5_sum = extractor.CollectBinaryElfinfo()
  return_struct = {
      'md5_sum': md5_sum,
  }
  print(json.dumps(return_struct, indent=2))
