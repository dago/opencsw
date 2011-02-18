#!/usr/bin/env python2.6

import unittest
import uwatch

class UpstreamWatchCommandUnitTest(unittest.TestCase):

  V1 = "1.8.1,REV=2010.07.13"
  V2 = "1.8.2,REV=2011.01.17"

  def testCompareVersionAndGetNewest(self):
    uwc = uwatch.UpstreamWatchCommand("fake name")
    self.assertEquals(
        self.V2,
        uwc.CompareVersionAndGetNewest(self.V1, self.V2))


if __name__ == '__main__':
	unittest.main()
