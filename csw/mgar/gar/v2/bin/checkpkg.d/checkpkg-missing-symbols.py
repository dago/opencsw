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

def CheckForMissingSymbols(pkg, debug):
  """Looks for "symbol not found" in ldd -r output."""
  errors = []
  binaries = pkg.ListBinaries()
  symbol_re = re.compile(r"symbol not found:")
  for binary in binaries:
    # this could be potentially moved into the DirectoryFormatPackage class.
    args = ["ldd", "-r", binary]
    ldd_proc = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = ldd_proc.communicate()
    retcode = ldd_proc.wait()
    lines = stdout.splitlines()
    missing_symbols = False
    for line in lines:
      if re.search(symbol_re, line):
      	missing_symbols = True
    binary_base = os.path.basename(binary)
    if missing_symbols:
    	errors.append(checkpkg.CheckpkgTag("symbol-not-found", binary_base))
  return errors


def main():
  options, args = checkpkg.GetOptions()
  pkgnames = args
  # CheckpkgManager class abstracts away things such as the collection of
  # results.
  check_manager = checkpkg.CheckpkgManager(CHECKPKG_MODULE_NAME,
                                           options.extractdir,
                                           pkgnames,
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
