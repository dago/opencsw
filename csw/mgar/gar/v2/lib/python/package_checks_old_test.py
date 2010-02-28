#!/opt/csw/bin/python2.6
# coding=utf-8
# $Id$

import unittest
import package_checks_old as pc
import yaml
import os.path

BASE_DIR = os.path.dirname(__file__)
TESTDATA_DIR = os.path.join(BASE_DIR, "testdata")

class PackageChecksUnitTest(unittest.TestCase):

  def setUp(self):
    self.pkg_data_1 = {
          "basic_stats": {
                "pkgname": "CSWfoo"
        }
    }
    self.pkg_data_2 = {
        'basic_stats': {
          'parsed_basename':
              {'revision_info': {'REV': '2010.02.15'},
               'catalogname': 'python_tk',
               'full_version_string': '2.6.4,REV=2010.02.15',
               'version': '2.6.4',
               'version_info': {
                 'minor version': '6',
                 'major version': '2',
                 'patchlevel': '4'},
               'osrel': 'SunOS5.8',
               'arch': 'sparc',
               'vendortag': 'CSW',
              },
          'pkgname': 'CSWpython-tk',
          'stats_version': 1,
          'pkg_basename': 'python_tk-2.6.4,REV=2010.02.15-SunOS5.8-sparc-CSW.pkg.gz',
          'pkg_path': '/tmp/pkg_lL0HDH/python_tk-2.6.4,REV=2010.02.15-SunOS5.8-sparc-CSW.pkg.gz',
          'catalogname': 'python_tk'}}

  def LoadData(self, name):
    file_name = os.path.join(TESTDATA_DIR, "%s.yml" % name)
    f = open(file_name, "rb")
    data = yaml.safe_load(f)
    f.close()
    return data

  def testCatalogName_1(self):
    self.pkg_data_1["basic_stats"]["catalogname"] = "Foo"
    errors = pc.CatalognameLowercase(self.pkg_data_1, False)
    self.failUnless(errors)

  def testCatalogName_2(self):
    self.pkg_data_1["basic_stats"]["catalogname"] = "foo"
    errors = pc.CatalognameLowercase(self.pkg_data_1, False)
    self.failIf(errors)

  def testCatalogNameSpecialCharacters(self):
    self.pkg_data_1["basic_stats"]["catalogname"] = "foo+abc&123"
    errors = pc.CatalognameLowercase(self.pkg_data_1, False)
    self.failUnless(errors)

  def testFileNameSanity(self):
    del(self.pkg_data_2["basic_stats"]["parsed_basename"]["revision_info"]["REV"])
    errors = pc.FileNameSanity(self.pkg_data_2, False)
    self.failUnless(errors)

  def testCheckArchitectureVsContents(self):
    self.pkg_data_2["pkgmap"] = self.LoadData("example-1-pkgmap")
    self.pkg_data_2["binaries"] = []
    self.pkg_data_2["pkginfo"] = self.LoadData("example-1-pkginfo")
    errors = pc.CheckArchitectureVsContents(self.pkg_data_2, False)
    self.failIf(errors)

  def testCheckForMissingSymbols(self):
    ldd_dash_r_yml = """opt/csw/lib/postgresql/8.4/_int.so:
- {path: /usr/lib/libc.so.1, soname: libc.so.1, state: OK, symbol: null}
- {path: /usr/lib/libdl.so.1, soname: libdl.so.1, state: OK, symbol: null}
- {path: /tmp/pkg_W8UcnK/CSWlibpq-84/root/opt/csw/lib/postgresql/8.4/_int.so, soname: null,
  state: symbol-not-found, symbol: CurrentMemoryContext}
- {path: /tmp/pkg_W8UcnK/CSWlibpq-84/root/opt/csw/lib/postgresql/8.4/_int.so, soname: null,
  state: symbol-not-found, symbol: MemoryContextAlloc}
- {path: /tmp/pkg_W8UcnK/CSWlibpq-84/root/opt/csw/lib/postgresql/8.4/_int.so, soname: null,
  state: symbol-not-found, symbol: errstart}
- {path: /tmp/pkg_W8UcnK/CSWlibpq-84/root/opt/csw/lib/postgresql/8.4/_int.so, soname: null,
  state: symbol-not-found, symbol: errcode}
opt/csw/lib/postgresql/8.4/_int2.so:
- {path: /usr/lib/libdl.so.1, soname: libdl.so.1, state: OK, symbol: null}"""
    defined_symbols_yml = """opt/csw/lib/postgresql/8.4/_int.so: [Pg_magic_func, _fini, _init, _int_contained,
  _int_contains, _int_different, _int_inter, _int_overlap, _int_same, _int_union,
  _int_unique, _intbig_in, _intbig_out, boolop, bqarr_in, bqarr_out, compASC, compDESC,
  copy_intArrayType, execconsistent, g_int_compress, g_int_consistent, g_int_decompress,
  g_int_penalty, g_int_picksplit, g_int_same, g_int_union, g_intbig_compress, g_intbig_consistent,
  g_intbig_decompress, g_intbig_penalty, g_intbig_picksplit, g_intbig_same, g_intbig_union,
  gensign, ginconsistent, ginint4_consistent, ginint4_queryextract, icount, idx, inner_int_contains,
  inner_int_inter, inner_int_overlap, inner_int_union, int_to_intset, intarray_add_elem,
  intarray_concat_arrays, intarray_del_elem, intarray_match_first, intarray_push_array,
  intarray_push_elem, internal_size, intset, intset_subtract, intset_union_elem, isort,
  new_intArrayType, pg_finfo__int_contained, pg_finfo__int_contains, pg_finfo__int_different,
  pg_finfo__int_inter, pg_finfo__int_overlap, pg_finfo__int_same, pg_finfo__int_union,
  pg_finfo__intbig_in, pg_finfo__intbig_out, pg_finfo_boolop, pg_finfo_bqarr_in, pg_finfo_bqarr_out,
  pg_finfo_g_int_compress, pg_finfo_g_int_consistent, pg_finfo_g_int_decompress, pg_finfo_g_int_penalty,
  pg_finfo_g_int_picksplit, pg_finfo_g_int_same, pg_finfo_g_int_union, pg_finfo_g_intbig_compress,
  pg_finfo_g_intbig_consistent, pg_finfo_g_intbig_decompress, pg_finfo_g_intbig_penalty,
  pg_finfo_g_intbig_picksplit, pg_finfo_g_intbig_same, pg_finfosc, subarray, uniq]
opt/csw/lib/postgresql/8.4/adminpack.so: [Pg_magic_func, _fini, _init, pg_file_rename,
  pg_file_unlink, pg_file_write, pg_finfo_pg_file_rename, pg_finfo_pg_file_unlink,
  pg_finfo_pg_file_write, pg_finfo_pg_logdir_ls, pg_logdir_ls]
opt/csw/lib/postgresql/8.4/_int2.so: []
  """

    self.pkg_data_2["ldd_dash_r"] = yaml.safe_load(ldd_dash_r_yml)
    self.pkg_data_2["defined_symbols"] = yaml.safe_load(defined_symbols_yml)
    self.pkg_data_2["binaries"] = ["opt/csw/lib/postgresql/8.4/_int.so",
                                   "opt/csw/lib/postgresql/8.4/_int2.so"]
    errors = pc.CheckForMissingSymbols([self.pkg_data_2], False)
    self.failUnless(errors)


  def testArchitectureSanity(self):
    self.pkg_data_2["pkginfo"] = {}
    self.pkg_data_2["pkginfo"]["ARCH"] = "i386"
    errors = pc.ArchitectureSanity(self.pkg_data_2, False)
    self.failUnless(errors)


if __name__ == '__main__':
  unittest.main()
