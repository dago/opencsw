#!/opt/csw/bin/python2.6
# $Id$

import checkpkg
import logging
import os.path
import sys

OBSOLETE_DEPS = {
    # "CSWfoo": {
    #   "reason": "Due to...",
    #   "url": "http://www.opencsw.org/bugtrack/view.php?id=..."
    # },
    "CSWpython-rt": {
      "reason": "CSWpython-rt is deprecated.",
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
        if "reason" in OBSOLETE_DEPS[pkg]:
          print "Reason:", OBSOLETE_DEPS[pkg]["reason"]
        if "url" in OBSOLETE_DEPS[pkg]:
          print "URL:", OBSOLETE_DEPS[pkg]["url"]
  if ok:
    sys.exit(0)
  else:
    sys.exit(1)

if __name__ == '__main__':
  main()
