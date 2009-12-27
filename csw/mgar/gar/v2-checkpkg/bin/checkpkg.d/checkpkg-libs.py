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
RUNPATH = "runpath"
SONAME = "soname"

def main():
  errors = []
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
  sonames_by_pkgname = {}
  pkg_by_any_filename = {}
  for checker in checkers:
    pkg_binary_paths = checker.ListBinaries()
    binaries_base = [os.path.split(x)[1] for x in pkg_binary_paths]
    binaries_by_pkgname[checker.pkgname] = binaries_base
    binaries.extend(pkg_binary_paths)
    for f in checker.GetAllFilenames():
    	pkg_by_any_filename[f] = checker.pkgname
  # Making the binaries unique
  binaries = set(binaries)
  ws_re = re.compile(r"\s+")

  # TODO: map from binaries_by_pkgname to sonames_by_pkgname
  #
  # Essentially, we must look at libfoo.so.1.2.3 and map it to libfoo.so.1,
  # whatever soname it has

  # man ld.so.1 for more info on this hack
  env = copy.copy(os.environ)
  env["LD_NOAUXFLTR"] = "1"
  needed_sonames_by_binary = {}
  filenames_by_soname = {}
  # Assembling a data structure with the data about binaries.
  # {
  #   <binary1 name>: { checkpkg.NEEDED_SONAMES: [...],
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
        if checkpkg.NEEDED_SONAMES not in binary_data:
          binary_data[checkpkg.NEEDED_SONAMES] = []
        binary_data[checkpkg.NEEDED_SONAMES].append(fields[2])
      elif fields[1] == "RUNPATH":
        if RUNPATH not in binary_data:
          binary_data[RUNPATH] = []
        binary_data[RUNPATH].extend(fields[2].split(":"))
        # Adding the default runtime path search option.
        binary_data[RUNPATH].append("/usr/lib")
      elif fields[1] == "SONAME":
        binary_data[SONAME] = fields[2]
    if SONAME in binary_data:
      filenames_by_soname[binary_data[SONAME]] = binary_base_name
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
    for soname in data[checkpkg.NEEDED_SONAMES]:
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
      # This is the critical part of the algorithm: it iterates over the
      # runpath and finds the first matching one.
      # 
      # TODO: Expand $ISALIST to whatever the 'isalist' command outputs for
      # better matching.
      for runpath in runpath_by_needed_soname[soname]:
      	soname_runpath_data = pkgmap.GetPkgmapLineByBasename(soname)
        if runpath in soname_runpath_data:
          lines_by_soname[soname] = soname_runpath_data[runpath]
          break
    except KeyError, e:
      logging.debug("couldn't find %s in the needed sonames list: %s",
                    soname, e)
  pkgs_by_filename = {}
  for soname, line in lines_by_soname.iteritems():
    # TODO: Find all the packages, not just the last field.
    fields = re.split(ws_re, line.strip())
    # For now, we'll assume that the last field is the package.
    pkgname = fields[-1]
    pkgs_by_filename[soname] = pkgname

  # A shared object dependency/provisioning report, plus checking.
  if needed_sonames:
    print "Analysis of sonames needed by the package set:"
    for soname in needed_sonames:
      if soname in filenames_by_soname:
        print "%s is provided by the package itself" % soname
      elif soname in lines_by_soname:
        print ("%s is required by %s and provided by %s" 
               % (soname,
                  binaries_by_soname[soname],
                  repr(pkgs_by_filename[soname])))
      else:
        print ("%s is required by %s, but we don't know what provides it."
               % (soname, binaries_by_soname[soname]))
        errors.append(checkpkg.Error("%s is required by %s, but we don't know what provides it."
                                     % (soname, binaries_by_soname[soname])))
    print

  # Data needed for this section:
  # - pkgname
  # - declared dependencies
  # - binaries_by_pkgname
  # - needed_sonames_by_binary
  # - pkgs_by_filename
  dependent_pkgs = {}
  for checker in checkers:
    orphan_sonames = set()
    pkgname = checker.pkgname
    print "%s:" % pkgname
    declared_dependencies = checker.GetDependencies()
    missing_deps, surplus_deps, orphan_sonames = checkpkg.AnalyzeDependencies(
        pkgname,
        declared_dependencies,
        binaries_by_pkgname,
        needed_sonames_by_binary,
        pkgs_by_filename,
        filenames_by_soname,
        pkg_by_any_filename)

    save_testing_data = True
    if save_testing_data:
      test_fd = open("/var/tmp/checkpkg-dep-testing-data-%s.py" % pkgname, "w")
      sanitized_pkgname = pkgname.replace("-", "_")
      print >>test_fd, "# Testing data for %s" % pkgname
      print >>test_fd, "DATA_PKGNAME =" % sanitized_pkgname, repr(pkgname)
      print >>test_fd, "DATA_DECLARED_DEPENDENCIES =" % sanitized_pkgname, repr(declared_dependencies)
      print >>test_fd, "DATA_BINARIES_BY_PKGNAME =" % sanitized_pkgname, repr(binaries_by_pkgname)
      print >>test_fd, "DATA_NEEDED_SONAMES_BY_BINARY =" % sanitized_pkgname, repr(needed_sonames_by_binary)
      print >>test_fd, "DATA_PKGS_BY_FILENAME =" % sanitized_pkgname, repr(pkgs_by_filename)
      print >>test_fd, "DATA_FILENAMES_BY_SONAME =" % sanitized_pkgname, repr(filenames_by_soname)
      print >>test_fd, "DATA_PKG_BY_ANY_FILENAME =" % sanitized_pkgname, repr(pkg_by_any_filename)
      test_fd.close()

    if missing_deps:
      print "SUGGESTION: you may want to add some or all of the following as depends:"
      print "   (Feel free to ignore SUNW or SPRO packages)"
      for dep_pkgname in sorted(missing_deps):
        print ">", dep_pkgname
    if surplus_deps:
      print "The following packages might be unnecessary dependencies:"
      for dep_pkgname in surplus_deps:
        print "? ", dep_pkgname
    if orphan_sonames:
      print "The following sonames don't belong to any package:"
      for soname in sorted(orphan_sonames):
        errors.append(checkpkg.Error("The following soname does't belong to "
                                     "any package: %s" % soname))
        print "! ", soname

  if errors:
    for error in errors:
      logging.error(error)
    sys.exit(1)
  else:
    sys.exit(0)


if __name__ == '__main__':
  main()
