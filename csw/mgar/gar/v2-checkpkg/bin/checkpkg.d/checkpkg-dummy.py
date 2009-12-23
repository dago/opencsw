#!/opt/csw/bin/python2.6
# $Id$

import checkpkg
import os.path

def main():
  options, args = checkpkg.GetOptions()
  pkgpath = os.path.join(options.extractdir, options.pkgname)
  if not os.path.isdir(pkgpath):
  	raise checkpkg.PackageError("The package directory doesn't exist: %s" % pkgpath)
  print ("Dummy plugin says the package %s is extracted to %s"
         % (options.pkgname, options.extractdir))


if __name__ == '__main__':
	main()
