#!/opt/csw/bin/python2.6
# $Id$

"""This is a dummy check. You can use it as a boilerplate for your own checks.

Copy it and modify.
"""

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

def main():
  options, args = checkpkg.GetOptions()
  if not os.path.isdir(options.extractdir):
  	raise checkpkg.PackageError("The extract base directory doesn't exist: %s" % options.extractdir)
  for pkgname in args:
    pkgpath = os.path.join(options.extractdir, pkgname)
    if not os.path.isdir(pkgpath):
      raise checkpkg.PackageError("The package directory doesn't exist: %s" % pkgpath)
    logging.debug("Dummy plugin says the package %s is extracted to %s",
                  pkgname, options.extractdir)


if __name__ == '__main__':
  main()
