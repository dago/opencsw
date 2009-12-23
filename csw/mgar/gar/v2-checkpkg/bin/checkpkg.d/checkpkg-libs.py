#!/opt/csw/bin/python2.6
#
# $Id$
#
# A check for dependencies between shared libraries.

import checkpkg
import os.path

def main():
  options, args = checkpkg.GetOptions()
  pkgpath = os.path.join(options.extractdir, options.pkgname)


if __name__ == '__main__':
	main()
