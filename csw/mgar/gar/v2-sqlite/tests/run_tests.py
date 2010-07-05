#!/opt/csw/bin/python2.6
# $Id$

import unittest
import sys
import os.path
module_path = [os.path.dirname(__file__),
               "..", "lib", "python"]
sys.path.append(os.path.join(*module_path))

# To add more test files, create <name>.py file and add a corresponding line
# here:
from checkpkg_test           import *
from example_test            import *
from opencsw_test            import *
from overrides_test          import *
from tag_test                import *
from package_checks_test     import *

if __name__ == '__main__':
  unittest.main()

# vim:set ts=2 sts=2 sw=2 expandtab:
