#!/opt/csw/bin/python2.6
# $Id$

"""Check for missing symbols in binaries.

http://sourceforge.net/tracker/?func=detail&aid=2939416&group_id=229205&atid=1075770
"""

import os.path
import re
import sys
import subprocess

CHECKPKG_MODULE_NAME = "missing symbols"

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.path.dirname(__file__),
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg

# Defining checking functions.

def CheckForMissingSymbols(pkg_data, debug):
  """Looks for "symbol not found" in ldd -r output."""
  errors = []
  binaries = pkg_data["binaries"]
  symbol_re = re.compile(r"symbol not found:")
  for binary in binaries:
    lines = pkg_data["ldd_dash_r"][binary]
    missing_symbols = False
    for line in lines:
      if re.search(symbol_re, line):
      	missing_symbols = True
    binary_base = os.path.basename(binary)
    if missing_symbols:
    	errors.append(checkpkg.CheckpkgTag(
    	  pkg_data["basic_stats"]["pkgname"],
    	  "symbol-not-found", binary_base))
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
  # Registering functions defined above.
  check_manager.RegisterIndividualCheck(CheckForMissingSymbols)
  # Running the checks, reporting and exiting.
  exit_code, screen_report, tags_report = check_manager.Run()
  f = open(options.output, "w")
  f.write(tags_report)
  f.close()
  print screen_report.strip()
  sys.exit(exit_code)


if __name__ == '__main__':
  main()
