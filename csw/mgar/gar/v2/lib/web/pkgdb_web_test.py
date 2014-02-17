#!/opt/csw/bin/python2.6

import cjson
import ConfigParser
import logging
import mock
import unittest
import webtest

from lib.python import configuration
from lib.python import database
from lib.web import pkgdb_web
from lib.web import releases_web
from lib.web import web_lib

from lib.python.testdata.neon_stats import pkgstats as neon_stats

class PkgdbWebUnitTest(unittest.TestCase):

  def GetConfigForTest(self):
    config = ConfigParser.SafeConfigParser(configuration.CONFIG_DEFAULTS)
    config.add_section("database")
    config.set("database", "type", "sqlite")
    config.set("database", "name", ":memory:")
    config.set("database", "host", "")
    config.set("database", "user", "")
    config.set("database", "password", "")
    return config

  def setUp(self):
    super(PkgdbWebUnitTest, self).setUp()
    with mock.patch('lib.python.configuration.GetConfig') as config_getter:
      config = self.GetConfigForTest()
      config_getter.return_value = config
      web_lib.ConnectToDatabase()
      database.InitDB(config)
    self.pkgdbapp = webtest.TestApp(pkgdb_web.app.wsgifunc())
    self.relapp = webtest.TestApp(releases_web.app.wsgifunc())

  def tearDown(self):
    super(PkgdbWebUnitTest, self).tearDown()
    configuration.TearDownSqlobjectConnection()


  def testGetRoot(self):
    resp = self.pkgdbapp.get('/')
    resp.mustcontain('<html>')

  def testGetCatalogList(self):
    # It still wants to connect to MySQL here.
    with mock.patch('lib.python.configuration.GetConfig') as config_getter:
      resp = self.pkgdbapp.get('/rest/catalogs/')
      resp.mustcontain('SunOS5.10')
      resp.mustcontain('unstable')

  def testGetCatalogDetail(self):
    # But we need to insert something first
    # resp = self.pkgdbapp.get('/rest/catalogs/unstable/sparc/SunOS5.10/')
    # resp.mustcontain('foo')
    pass

  def testPutBlobMissingField(self):
    # Missing data in the put request.
    self.assertRaises(
        webtest.AppError,
        self.relapp.put,
        '/blob/pkgstats/d3b07384d113edec49eaa6238ad5ff00/')

  def testPutBlobGood1(self):
    neon_json = cjson.encode(neon_stats)
    self.assertRaises(
        webtest.AppError,
        self.relapp.get,
        '/blob/pkgstats/ba3b78331d2ed321900e5da71f7714c5/')
    self.relapp.put(
        '/blob/pkgstats/ba3b78331d2ed321900e5da71f7714c5/',
        params={
          'json_data': neon_json,
          'md5_sum': 'ba3b78331d2ed321900e5da71f7714c5'})
    resp = self.relapp.get(
        '/blob/pkgstats/ba3b78331d2ed321900e5da71f7714c5/')
    self.assertEqual(resp.text, neon_json)
    resp = self.relapp.delete(
        '/blob/pkgstats/ba3b78331d2ed321900e5da71f7714c5/')


if __name__ == '__main__':
  logging.basicConfig(level=logging.ERROR)
  unittest.main()
