#!/usr/bin/env python2.6

# Try to use unittest2, fall back to unittest
try:
  import unittest2 as unittest
except ImportError:
  import unittest

import submit_to_newpkgs as stn

# FileSetChecker class and unit tests have been moved to a separate
# file.


if __name__ == '__main__':
	unittest.main()
