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

def CheckSharedLibraryConsistency(pkgs_data, debug):
  ws_re = re.compile(r"\s+")
  result_ok = True
  errors = []
  binaries = []
  binaries_by_pkgname = {}
  sonames_by_pkgname = {}
  pkg_by_any_filename = {}
  needed_sonames_by_binary = {}
  filenames_by_soname = {}
  for pkg_data in pkgs_data:
    binaries_base = [os.path.basename(x) for x in pkg_data["binaries"]]
    pkgname = pkg_data["basic_stats"]["pkgname"]
    binaries_by_pkgname[pkgname] = binaries_base
    binaries.extend(pkg_data["binaries"])
    for filename in pkg_data["all_filenames"]:
      pkg_by_any_filename[filename] = pkgname
    for binary_data in pkg_data["binaries_dump_info"]:
      binary_base_name = os.path.basename(binary_data["base_name"])
      needed_sonames_by_binary[binary_base_name] = binary_data
      filenames_by_soname[binary_data[checkpkg.SONAME]] = binary_base_name
    
  # Making the binaries unique
  binaries = set(binaries)
  isalist = pkg_data["isalist"]

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
  # same bit of code would do both checking and reporting.
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
  for checker in pkgs_data:
    pkgname = checker["basic_stats"]["pkgname"]
    declared_dependencies = checker["depends"]
    if debug and False:
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
        "pkgname": pkgname,
        "missing_deps": missing_deps,
        "surplus_deps": surplus_deps,
        "orphan_sonames": orphan_sonames,
    }
    t = Template.Template(checkpkg.REPORT_TMPL, searchList=[namespace])
    print unicode(t)

    for soname in orphan_sonames:
      errors.append(
          checkpkg.CheckpkgTag(
            pkgname,
            "orphan-soname",
            soname))
    for missing_dep in missing_deps:
      errors.append(
          checkpkg.CheckpkgTag(
            pkgname,
            "missing-dependency",
            missing_dep))
  return errors


def main():
  options, args = checkpkg.GetOptions()
  md5sums = args
  # CheckpkgManager class abstracts away things such as the collection of
  # results.
  check_manager = checkpkg.CheckpkgManager(CHECKPKG_MODULE_NAME,
                                           options.stats_basedir,
                                           md5sums,
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
