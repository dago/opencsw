#!/opt/csw/bin/python2.6
#
# $Id$
#
# A check for dependencies between shared libraries.
#
# This is currently more of a prototype than a mature program, but it has some
# unit tests and it appears to be working.  The main problem is that it's not
# divided into smaller testable sections.

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

def GetIsalist():
  args = ["isalist"]
  isalist_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
  stdout, stderr = isalist_proc.communicate()
  ret = isalist_proc.wait()
  if ret:
  	logging.error("Calling isalist has failed.")
  isalist = re.split(r"\s+", stdout.strip())
  return isalist


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
    for filename in checker.GetAllFilenames():
      pkg_by_any_filename[filename] = checker.pkgname
  # Making the binaries unique
  binaries = set(binaries)
  ws_re = re.compile(r"\s+")

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
    if checkpkg.NEEDED_SONAMES not in binary_data:
      binary_data[checkpkg.NEEDED_SONAMES] = []
    if RUNPATH not in binary_data:
      binary_data[RUNPATH] = []
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
        binary_data[checkpkg.NEEDED_SONAMES].append(fields[2])
      elif fields[1] == "RUNPATH":
        binary_data[RUNPATH].extend(fields[2].split(":"))
        # Adding the default runtime path search option.
        binary_data[RUNPATH].append("/usr/lib")
      elif fields[1] == "SONAME":
        binary_data[SONAME] = fields[2]
    if SONAME in binary_data:
      filenames_by_soname[binary_data[SONAME]] = binary_base_name
  # TODO: make it a unit test
  # print needed_sonames_by_binary
  isalist = GetIsalist()
  
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
        binaries_by_soname[soname] = set()
      binaries_by_soname[soname].add(binary_name)

  pkgmap = checkpkg.SystemPkgmap()
  logging.debug("Determining the soname-package relationships.")
  # lines by soname is an equivalent of $EXTRACTDIR/shortcatalog
  lines_by_soname = checkpkg.GetLinesBySoname(
      pkgmap, needed_sonames, runpath_by_needed_soname, isalist)
  pkgs_by_filename = {}
  for soname, line in lines_by_soname.iteritems():
    # TODO: Find all the packages, not just the last field.
    fields = re.split(ws_re, line.strip())
    # For now, we'll assume that the last field is the package.
    pkgname = fields[-1]
    pkgs_by_filename[soname] = pkgname

  # A shared object dependency/provisioning report, plus checking.
  # TODO: Rewrite this using cheetah
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

    if options.debug or True:
      data_file_name = "/var/tmp/checkpkg-dep-testing-data-%s.py" % pkgname
      logging.warn("Saving test data to %s." % repr(data_file_name))
      test_fd = open(data_file_name, "w")
      sanitized_pkgname = pkgname.replace("-", "_")
      print >>test_fd, "# Testing data for %s" % pkgname
      print >>test_fd, "DATA_PKGNAME =", repr(pkgname)
      print >>test_fd, "DATA_DECLARED_DEPENDENCIES =", repr(declared_dependencies)
      print >>test_fd, "DATA_BINARIES_BY_PKGNAME =", repr(binaries_by_pkgname)
      print >>test_fd, "DATA_NEEDED_SONAMES_BY_BINARY =", repr(needed_sonames_by_binary)
      print >>test_fd, "DATA_PKGS_BY_FILENAME =", repr(pkgs_by_filename)
      print >>test_fd, "DATA_FILENAMES_BY_SONAME =", repr(filenames_by_soname)
      print >>test_fd, "DATA_PKG_BY_ANY_FILENAME =", repr(pkg_by_any_filename)
      print >>test_fd, "DATA_LINES_BY_SONAME =", repr(lines_by_soname)
      test_fd.close()

    # TODO: Rewrite this using cheetah templates.
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
    print

  if errors:
    for error in errors:
      logging.error(error)
    sys.exit(1)
  else:
    sys.exit(0)


if __name__ == '__main__':
  main()

# vim:set sw=2 ts=2 sts=2 expandtab:
