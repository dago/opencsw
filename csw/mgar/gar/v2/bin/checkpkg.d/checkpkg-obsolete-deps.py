#!/opt/csw/bin/python2.6
# $Id$

import logging
import os.path
import sys

# The following bit of code sets the correct path to Python libraries
# distributed with GAR.
path_list = [os.getcwd(),
             os.path.split(sys.argv[0])[0],
             "..", "..", "lib", "python"]
sys.path.append(os.path.join(*path_list))
import checkpkg

OBSOLETE_DEPS = {
    # "CSWfoo": {
    #   "hint": "Do this...",
    #   "url": "http://www.opencsw.org/bugtrack/view.php?id=..."
    # },
    "CSWpython-rt": {
      "hint": "CSWpython-rt is deprecated, use CSWpython instead.",
      "url": "http://www.opencsw.org/bugtrack/view.php?id=4031"
    },
}

def main():
  options, args = checkpkg.GetOptions()
  ok = True
  for pkgname in args:
    pkgpath = os.path.join(options.extractdir, pkgname)
    checker = checkpkg.CheckpkgBase(options.extractdir, pkgname)
    deps = set(checker.GetDependencies())
    obsolete_pkg_deps = deps.intersection(set(OBSOLETE_DEPS))
    if obsolete_pkg_deps:
      ok = False
      for pkg in obsolete_pkg_deps:
        print ("ERROR: Package %s should not depend on %s."
               % (checker.pkgname, pkg))
        if "hint" in OBSOLETE_DEPS[pkg]:
          print "Hint:", OBSOLETE_DEPS[pkg]["hint"]
        if "url" in OBSOLETE_DEPS[pkg]:
          print "URL:", OBSOLETE_DEPS[pkg]["url"]
  if ok:
    sys.exit(0)
  else:
    sys.exit(1)


if __name__ == '__main__':
  main()
