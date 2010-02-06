#!/opt/csw/bin/python2.6
#
# $Id$

"""A check for dependencies between shared libraries.
This is currently more of a prototype than a mature program, but it has some
unit tests and it appears to be working.  The main problem is that it's not
divided into smaller testable sections.
"""

import os
import os.path
import copy
import re
import subprocess
import logging
import sys
import textwrap
from Cheetah import Template

CHECKPKG_MODULE_NAME = "shared library linking consistency"

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg
import opencsw

DUMP_BIN = "/usr/ccs/bin/dump"

def GetIsalist():
  args = ["isalist"]
  isalist_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
  stdout, stderr = isalist_proc.communicate()
  ret = isalist_proc.wait()
  if ret:
    logging.error("Calling isalist has failed.")
  isalist = re.split(r"\s+", stdout.strip())
  return isalist


def CheckSharedLibraryConsistency(pkgs, debug):
  result_ok = True
  errors = []
  binaries = []
  binaries_by_pkgname = {}
  sonames_by_pkgname = {}
  pkg_by_any_filename = {}
  for checker in pkgs:
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
  #                     checkpkg.RUNPATH:        [...]},
  #   <binary2 name>: ...,
  #   ...
  # }
  #
  for binary in binaries:
    binary_base_name = binary.split("/")[-1]
    args = [DUMP_BIN, "-Lv", binary]
    dump_proc = subprocess.Popen(args, stdout=subprocess.PIPE, env=env)
    stdout, stderr = dump_proc.communicate()
    ret = dump_proc.wait()
    binary_data = checkpkg.ParseDumpOutput(stdout)
    needed_sonames_by_binary[binary_base_name] = binary_data
    if checkpkg.SONAME not in binary_data:
      logging.debug("The %s binary doesn't provide a SONAME. "
                    "(It might be an executable)",
                   binary_base_name)
      # The shared library doesn't tell its SONAME.  We're guessing it's the
      # same as the base file name.
      binary_data[checkpkg.SONAME] = binary_base_name
    filenames_by_soname[binary_data[checkpkg.SONAME]] = binary_base_name

  isalist = GetIsalist()

  # Building indexes by soname to simplify further processing
  # These are indexes "by soname".
  (needed_sonames,
   binaries_by_soname,
   runpath_by_needed_soname) = checkpkg.BuildIndexesBySoname(
       needed_sonames_by_binary)

  pkgmap = checkpkg.SystemPkgmap()
  logging.debug("Determining the soname-package relationships.")
  # lines by soname is an equivalent of $EXTRACTDIR/shortcatalog
  lines_by_soname = checkpkg.GetLinesBySoname(
      pkgmap, needed_sonames, runpath_by_needed_soname, isalist)

  # Creating a map from files to packages.
  pkgs_by_filename = {}
  for soname, line in lines_by_soname.iteritems():
    # TODO: Find all the packages, not just the last field.
    fields = re.split(ws_re, line.strip())
    # For now, we'll assume that the last field is the package.
    pkgname = fields[-1]
    pkgs_by_filename[soname] = pkgname

  # A shared object dependency/provisioning report, plus checking.
  #
  # This section is somewhat overlapping with checkpkg.AnalyzeDependencies(),
  # it has a different purpose: it reports the relationships between shared
  # libraries, binaries using them and packages providing them.  Ideally, the
  # same bit of code with do checking and reporting.
  #
  # TODO: Rewrite this using cheetah templates
  if debug and needed_sonames:
    print "Analysis of sonames needed by the package set:"
    binaries_with_missing_sonames = set([])
    for soname in needed_sonames:
      logging.debug("Analyzing: %s", soname)
      if soname in filenames_by_soname:
        print "%s is provided by the package itself" % soname
      elif soname in lines_by_soname:
        print ("%s is provided by %s and required by:" 
               % (soname,
                  pkgs_by_filename[soname]))
        filename_lines = " ".join(sorted(binaries_by_soname[soname]))
        for line in textwrap.wrap(filename_lines, 70):
          print " ", line
      else:
        print ("%s is required by %s, but we don't know what provides it."
               % (soname, binaries_by_soname[soname]))
        for binary in binaries_by_soname[soname]:
          binaries_with_missing_sonames.add(binary)
        if soname in checkpkg.ALLOWED_ORPHAN_SONAMES:
          print "However, it's a whitelisted soname."
        else:
          pass
          # The error checking needs to be unified: done in one place only.
          # errors.append(
          #     checkpkg.CheckpkgTag(
          #       "%s is required by %s, but "
          #       "we don't know what provides it."
          #       % (soname, binaries_by_soname[soname])))
    if binaries_with_missing_sonames:
      print "The following are binaries with missing sonames:"
      binary_lines = " ".join(sorted(binaries_with_missing_sonames))
      for line in textwrap.wrap(binary_lines, 70):
        print " ", line
    print

  dependent_pkgs = {}
  for checker in pkgs:
    pkgname = checker.pkgname
    dir_format_pkg = opencsw.DirectoryFormatPackage(checker.pkgpath)
    declared_dependencies = dir_format_pkg.GetDependencies()
    if debug:
      sanitized_pkgname = pkgname.replace("-", "_")
      data_file_name = "/var/tmp/checkpkg_test_data_%s.py" % sanitized_pkgname
      logging.warn("Saving test data to %s." % repr(data_file_name))
      test_fd = open(data_file_name, "w")
      print >>test_fd, "# Testing data for %s" % pkgname
      print >>test_fd, "# $Id$"
      print >>test_fd, "DATA_PKGNAME                  =", repr(pkgname)
      print >>test_fd, "DATA_DECLARED_DEPENDENCIES    =", repr(declared_dependencies)
      print >>test_fd, "DATA_BINARIES_BY_PKGNAME      =", repr(binaries_by_pkgname)
      print >>test_fd, "DATA_NEEDED_SONAMES_BY_BINARY =", repr(needed_sonames_by_binary)
      print >>test_fd, "DATA_PKGS_BY_FILENAME         =", repr(pkgs_by_filename)
      print >>test_fd, "DATA_FILENAMES_BY_SONAME      =", repr(filenames_by_soname)
      print >>test_fd, "DATA_PKG_BY_ANY_FILENAME      =", repr(pkg_by_any_filename)
      print >>test_fd, "DATA_LINES_BY_SONAME          =", repr(lines_by_soname)
      print >>test_fd, "DATA_PKGMAP_CACHE             =", repr(pkgmap.cache)
      print >>test_fd, "DATA_BINARIES_BY_SONAME       =", repr(binaries_by_soname)
      print >>test_fd, "DATA_ISALIST                  =", repr(isalist)
      test_fd.close()

    missing_deps, surplus_deps, orphan_sonames = checkpkg.AnalyzeDependencies(
        pkgname,
        declared_dependencies,
        binaries_by_pkgname,
        needed_sonames_by_binary,
        pkgs_by_filename,
        filenames_by_soname,
        pkg_by_any_filename)
    namespace = {
        "pkgname": checker.pkgname,
        "missing_deps": missing_deps,
        "surplus_deps": surplus_deps,
        "orphan_sonames": orphan_sonames,
    }
    t = Template.Template(checkpkg.REPORT_TMPL, searchList=[namespace])
    print unicode(t)

    for soname in orphan_sonames:
      errors.append(
          checkpkg.CheckpkgTag(
            "orphan-soname",
            soname))
    for missing_dep in missing_deps:
    	errors.append(
    	    checkpkg.CheckpkgTag(
    	      "missing-dependency",
    	      missing_dep))
  return errors


def main():
  options, args = checkpkg.GetOptions()
  pkgnames = args
  check_manager = checkpkg.CheckpkgManager(CHECKPKG_MODULE_NAME,
                                           options.extractdir,
                                           pkgnames,
                                           options.debug)

  check_manager.RegisterSetCheck(CheckSharedLibraryConsistency)

  exit_code, screen_report, tags_report = check_manager.Run()
  f = open(options.output, "w")
  f.write(tags_report)
  f.close()
  print screen_report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()

# vim:set sw=2 ts=2 sts=2 expandtab:
