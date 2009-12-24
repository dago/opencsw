#!/opt/csw/bin/python2.6
#
# $Id$
#
# A check for dependencies between shared libraries.

import checkpkg
import os
import os.path
import copy
import re
import subprocess
import logging
import sys

DUMP_BIN = "/usr/ccs/bin/dump"
NEEDED_SONAMES = "needed sonames"
RUNPATH = "runpath"
TYPICAL_DEPENDENCIES = set(["CSWcommon", "CSWcswclassutils"])

def main():
  options, args = checkpkg.GetOptions()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)
  result_ok = True
  pkgnames = args
  checkers = []
  for pkgname in pkgnames:
    checker = checkpkg.CheckpkgBase(options.extractdir, pkgname)
    checkers.append(checker)
  binaries = []
  binaries_by_pkgname = {}
  for checker in checkers:
    pkg_binary_paths = checker.ListBinaries()
    binaries_base = [os.path.split(x)[1] for x in pkg_binary_paths]
    binaries_by_pkgname[checker.pkgname] = binaries_base
    binaries.extend(pkg_binary_paths)
  # Making the binaries unique
  binaries = set(binaries)
  ws_re = re.compile(r"\s+")

  # man ld.so.1 for more info on this hack
  env = copy.copy(os.environ)
  env["LD_NOAUXFLTR"] = "1"
  needed_sonames_by_binary = {}
  # Assembling a data structure with the data about binaries.
  # {
  #   <binary1 name>: { NEEDED_SONAMES: [...],
  #                     RUNPATH:        [...]},
  #   <binary2 name>: ...,
  #   ...
  # }
  #
  for binary in binaries:
    binary_base_name = binary.split("/")[-1]
    if binary_base_name not in needed_sonames_by_binary:
      needed_sonames_by_binary[binary_base_name] = {}
    binary_data = needed_sonames_by_binary[binary_base_name]
    args = [DUMP_BIN, "-Lv", binary]
    dump_proc = subprocess.Popen(args, stdout=subprocess.PIPE, env=env)
    stdout, stderr = dump_proc.communicate()
    ret = dump_proc.wait()
    for line in stdout.splitlines():
      fields = re.split(ws_re, line)
      # TODO: Make it a unit test
      # logging.debug("%s says: %s", DUMP_BIN, fields)
      if len(fields) < 3:
        continue
      if fields[1] == "NEEDED":
        if NEEDED_SONAMES not in binary_data:
          binary_data[NEEDED_SONAMES] = []
        binary_data[NEEDED_SONAMES].append(fields[2])
      elif fields[1] == "RUNPATH":
        if RUNPATH not in binary_data:
          binary_data[RUNPATH] = []
        binary_data[RUNPATH].extend(fields[2].split(":"))
        # Adding the default runtime path search option.
        binary_data[RUNPATH].append("/usr/lib")
  # TODO: make it a unit test
  # print needed_sonames_by_binary

  # Building indexes
  runpath_by_needed_soname = {}
  # {"foo.so": ["/opt/csw/lib/gcc4", "/opt/csw/lib", ...],
  #  ...
  # }
  needed_sonames = set()
  binaries_by_soname = {}
  for binary_name, data in needed_sonames_by_binary.iteritems():
    for soname in data[NEEDED_SONAMES]:
      needed_sonames.add(soname)
      if soname not in runpath_by_needed_soname:
        runpath_by_needed_soname[soname] = []
      runpath_by_needed_soname[soname].extend(data[RUNPATH])
      if soname not in binaries_by_soname:
        binaries_by_soname[soname] = []
      binaries_by_soname[soname].append(binary_name)

  pkgmap = checkpkg.SystemPkgmap()
  logging.debug("Determining the soname-package relationships.")
  # lines by soname is an equivalent of $EXTRACTDIR/shortcatalog
  lines_by_soname = {}
  for soname in needed_sonames:
    try:
      for runpath in runpath_by_needed_soname[soname]:
        if runpath in pkgmap.GetPkgmapLineByBasename(soname):
          # logging.debug("%s found in %s", runpath, pkgmap.GetPkgmapLineByBasename(soname))
          # logging.debug("line found: %s", repr(pkgmap.GetPkgmapLineByBasename(soname)[runpath]))
          lines_by_soname[soname] = pkgmap.GetPkgmapLineByBasename(soname)[runpath]
          break
    except KeyError, e:
      logging.debug("KeyError: %s", soname, e)
  pkgs_by_soname = {}
  for soname, line in lines_by_soname.iteritems():
    # TODO: Find all the packages, not just the last field.
    fields = re.split(ws_re, line.strip())
    # For now, we'll assume that the last field is the package.
    pkgname = fields[-1]
    pkgs_by_soname[soname] = pkgname

  # A shared object dependency/provisioning report, plus checking.
  for soname in needed_sonames:
    if soname in needed_sonames_by_binary:
      print "%s is provided by the package itself" % soname
    elif soname in lines_by_soname:
      print ("%s is required by %s and provided by %s" 
             % (soname,
                binaries_by_soname[soname],
                repr(pkgs_by_soname[soname])))
    else:
      print ("%s is required by %s, but we don't know what provides it."
             % (soname, binaries_by_soname[soname]))
      result_ok = False

  dependent_pkgs = {}
  for checker in checkers:
    orphan_sonames = set()
    pkgname = checker.pkgname
    # logging.debug("Reporting package %s", pkgname)
    declared_dependencies = checker.GetDependencies()
    so_dependencies = set()
    for binary in binaries_by_pkgname[pkgname]:
      if binary in needed_sonames_by_binary:
        for soname in needed_sonames_by_binary[binary][NEEDED_SONAMES]:
          if soname in pkgs_by_soname:
            so_dependencies.add(pkgs_by_soname[soname])
          else:
            orphan_sonames.add(soname)
      else:
        logging.warn("%s not found in needed_sonames_by_binary (%s)",
                     binary, needed_sonames_by_binary.keys())
    declared_dependencies_set = set(declared_dependencies)
    print "You can consider including the following packages in the dependencies:"
    for dep_pkgname in sorted(so_dependencies.difference(declared_dependencies_set)):
      print "  ", dep_pkgname,
      if dep_pkgname.startswith("SUNW"):
        print "(it's safe to ignore this one)",
      print
    
    surplus_dependencies = declared_dependencies_set.difference(so_dependencies)
    surplus_dependencies = surplus_dependencies.difference(TYPICAL_DEPENDENCIES)
    if surplus_dependencies:
      print "The following packages might be unnecessary dependencies:"
      for dep_pkgname in surplus_dependencies:
        print "  ", dep_pkgname
    if orphan_sonames:
      print "The following sonames don't belong to any package:"
      for soname in sorted(orphan_sonames):
        print "  ", soname

  if result_ok:
    sys.exit(0)
  else:
    sys.exit(1)


if __name__ == '__main__':
  main()
