#!/opt/csw/bin/python2.6
# $Id$

"""This is a dummy check. You can use it as a boilerplate for your own checks.

Copy it and modify.
"""

import checkpkg
import logging
import os.path

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
