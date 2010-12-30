#!/usr/bin/env python2.6

import unittest
import struct_util

class IndexByUnitTest(unittest.TestCase):

  def testIndexDictsBy_1(self):
    list_of_dicts = [
        {"a": 1},
        {"a": 2},
        {"a": 3},
    ]
    expected = {
        1: [{'a': 1}],
        2: [{'a': 2}],
        3: [{'a': 3}],
    }
    self.assertEquals(expected, struct_util.IndexDictsBy(list_of_dicts, "a"))

  def testIndexDictsBy_2(self):
    list_of_dicts = [
        {"a": 1, "b": 1},
        {"a": 1, "b": 2},
        {"a": 1, "b": 3},
    ]
    expected = {
        1: [
          {'a': 1, 'b': 1},
          {'a': 1, 'b': 2},
          {'a': 1, 'b': 3},
        ]
    }
    self.assertEquals(expected, struct_util.IndexDictsBy(list_of_dicts, "a"))


if __name__ == '__main__':
	unittest.main()
