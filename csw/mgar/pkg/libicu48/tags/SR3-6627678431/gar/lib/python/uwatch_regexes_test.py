#!/usr/bin/env python2.6

"""Tries to infer upstream watch regexes based on distnames."""

import unittest
import sqlobject
import pprint
from testdata import uwatch_regexes_data
import re
import uwatch


DB_URI = "mysql://maciej@localhost/spmtcsw_dev"


class UwatchPkgVersion(sqlobject.SQLObject):
  
  id_pkg = sqlobject.IntCol(dbName="ID_PKG")
  gar_path = sqlobject.UnicodeCol(length=255, dbName="PKG_GAR_PATH")
  pkgname = sqlobject.UnicodeCol(length=64, dbName="PKG_NAME")
  catalogname = sqlobject.UnicodeCol(length=64, dbName="PKG_CATALOGNAME")
  gar_version = sqlobject.UnicodeCol(length=255, dbName="PKG_GAR_VERSION")
  upstream_version = sqlobject.UnicodeCol(length=255, dbName="PKG_UPSTREAM_VERSION")
  master_sites = sqlobject.UnicodeCol(length=255, dbName="PKG_UPSTREAM_MASTER_SITES")
  distfiles = sqlobject.UnicodeCol(length=255, dbName="PKG_GAR_DISTFILES")
  regex = sqlobject.UnicodeCol(length=255, dbName="PKG_UFILES_REGEXP")

  class sqlmeta(object):
    table = "UWATCH_PKG_VERSION"
    idName = "id_pkg"
 

class FooTest(unittest.TestCase):
  
  def DisabledtestSave(self):
    res = UwatchPkgVersion.select()
    regex_list = []
    for r in res:
      regex_list.append({
        "pkgname": r.pkgname,
        "distfiles": r.distfiles,
        "gar_regex": r.regex,
        "target_regex": r.regex,
        "catalogname": r.catalogname})
    with open("testdata/uwatch_regexes_data.py", "w") as fd:
      fd.write("regex_list = ")
      fd.write(pprint.pformat(regex_list))
  
  def testRegexes(self):
    urg = uwatch.UwatchRegexGenerator()
    for d in uwatch_regexes_data.regex_list:
      if not d["distfiles"]: continue
      if not d["target_regex"]: continue
      if not d["distfiles"].strip(): continue
      if not d["target_regex"].strip(): continue
      auto_regex_list = urg.GenerateRegex(d["catalogname"], d["distfiles"])
      # self.assertEquals(
      #     d["target_regex"],
      #     urg.GenerateRegex(d["catalogname"], d["distfiles"]))
      if d["target_regex"] not in auto_regex_list:
        print repr(d["distfiles"]), repr(d["target_regex"]), repr(auto_regex_list)


if __name__ == '__main__':
  sqlobject.sqlhub.processConnection = sqlobject.connectionForURI(DB_URI)
  unittest.main()
