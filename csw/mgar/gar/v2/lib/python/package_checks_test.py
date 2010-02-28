#!/opt/csw/bin/python2.6
# coding=utf-8
# $Id$

import unittest
import package_checks as pc
import yaml
import os.path

BASE_DIR = os.path.dirname(__file__)
TESTDATA_DIR = os.path.join(BASE_DIR, "testdata")

class Foo(unittest.TestCase):
  pass
