#!/opt/csw/bin/python2.6

# Try to use unittest2, fall back to unittest
try:
  import unittest2 as unittest
except ImportError:
  import unittest

import mox
import os

from lib.python import util
from lib.python import shell
from lib.python import common_constants
from lib.python import representations


if __name__ == '__main__':
  unittest.main()
