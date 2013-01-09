#!/usr/bin/env python2.6

import unittest
import mox
import catalog_notifier
import catalog
import catalog_test
import copy
import pprint
import rest


class NotificationFormatterTest(mox.MoxTestBase):
  
  def disabled_testOne(self):
    """This tested too much."""
    f = catalog_notifier.NotificationFormatter()
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    url = "http://www.example.com/opencsw/"
    cat_a = self.mox.CreateMock(catalog.OpencswCatalog)
    cat_b = self.mox.CreateMock(catalog.OpencswCatalog)
    catalogs = [
        ("fossil", "amd65", "SolarOS5.12", cat_a, cat_b),
    ]
    maintainers = {
        "cfe40c06e994f6e8d3b191396d0365cb": {"maintainer_email": "joe@example.com"},
    }
    cat_a.GetDataByCatalogname().AndReturn({})
    cat_b.GetDataByCatalogname().AndReturn({"syslog_ng": catalog_test.PKG_STRUCT_1})
    self.mox.ReplayAll()
    self.assertEqual(
        "report here",
        f.FormatNotification(url, catalogs, rest_client_mock))

  def test_GetPkgsByMaintainerNew(self):
    f = catalog_notifier.NotificationFormatter()
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    cat_a = self.mox.CreateMock(catalog.OpencswCatalog)
    cat_b = self.mox.CreateMock(catalog.OpencswCatalog)
    catalogs = [
        ("fossil", "amd65", "SolarOS5.12", cat_a, cat_b),
        ("fossil", "amd65", "SolarOS5.13", cat_a, cat_b),
        ("fossil", "amd67", "SolarOS5.12", cat_a, cat_b),
        ("rock",   "amd65", "SolarOS5.12", cat_a, cat_b),
    ]
    rest_client_mock.GetMaintainerByMd5('cfe40c06e994f6e8d3b191396d0365cb').AndReturn(
        {"maintainer_email": "joe@example.com"}
    )
    rest_client_mock.GetMaintainerByMd5('cfe40c06e994f6e8d3b191396d0365cb').AndReturn(
        {"maintainer_email": "joe@example.com"}
    )
    rest_client_mock.GetMaintainerByMd5('cfe40c06e994f6e8d3b191396d0365cb').AndReturn(
        {"maintainer_email": "joe@example.com"}
    )
    rest_client_mock.GetMaintainerByMd5('cfe40c06e994f6e8d3b191396d0365cb').AndReturn(
        {"maintainer_email": "joe@example.com"}
    )
    cat_a.GetDataByCatalogname().AndReturn({})
    cat_b.GetDataByCatalogname().AndReturn({
      "syslog_ng": catalog_test.PKG_STRUCT_1,
    })
    cat_a.GetDataByCatalogname().AndReturn({})
    cat_b.GetDataByCatalogname().AndReturn({
      "syslog_ng": catalog_test.PKG_STRUCT_1,
    })
    cat_a.GetDataByCatalogname().AndReturn({})
    cat_b.GetDataByCatalogname().AndReturn({
      "syslog_ng": catalog_test.PKG_STRUCT_1,
    })
    cat_a.GetDataByCatalogname().AndReturn({})
    cat_b.GetDataByCatalogname().AndReturn({
      "syslog_ng": catalog_test.PKG_STRUCT_1,
    })
    self.mox.ReplayAll()
    expected = {'joe@example.com': {
      'new_pkgs': {
        catalog_test.PKG_STRUCT_1["file_basename"]: {
          "pkg": catalog_test.PKG_STRUCT_1,
          "catalogs": [
            ("fossil", "amd65", "SolarOS5.12"),
            ("fossil", "amd65", "SolarOS5.13"),
            ("fossil", "amd67", "SolarOS5.12"),
            ("rock",   "amd65", "SolarOS5.12"),
          ],
        },
      }}
    }
    result = f._GetPkgsByMaintainer(catalogs, rest_client_mock)
    self.assertEqual(expected, result)
    # Uncomment to see rendered template
    # print f._RenderForMaintainer(
    #     result["joe@example.com"], "joe@example.com",
    #     "http://mirror.example.com")

  def test_GetPkgsByMaintainerRemoved(self):
    f = catalog_notifier.NotificationFormatter()
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    cat_a = self.mox.CreateMock(catalog.OpencswCatalog)
    cat_b = self.mox.CreateMock(catalog.OpencswCatalog)
    catalogs = [
        ("fossil", "amd65", "SolarOS5.12", cat_a, cat_b),
    ]
    rest_client_mock.GetMaintainerByMd5('cfe40c06e994f6e8d3b191396d0365cb').AndReturn(
        {"maintainer_email": "joe@example.com"}
    )
    cat_a.GetDataByCatalogname().AndReturn({
      "syslog_ng": catalog_test.PKG_STRUCT_1,
    })
    cat_b.GetDataByCatalogname().AndReturn({})
    self.mox.ReplayAll()
    expected = {'joe@example.com': {
      'removed_pkgs': {
        catalog_test.PKG_STRUCT_1["file_basename"]: {
          "pkg": catalog_test.PKG_STRUCT_1,
          "catalogs": [
            ("fossil", "amd65", "SolarOS5.12"),
          ],
        },
      }}
    }
    self.assertEqual(
        expected,
        f._GetPkgsByMaintainer(catalogs, rest_client_mock))
    expected_text = u"""aa"""
    # Uncomment to see rendered template
    # print f._RenderForMaintainer(
    #     expected["joe@example.com"],
    #     "joe@example.com",
    #     "http://mirror.example.com")

  def test_GetPkgsByMaintainerTakeover(self):
    f = catalog_notifier.NotificationFormatter()
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    cat_a = self.mox.CreateMock(catalog.OpencswCatalog)
    cat_b = self.mox.CreateMock(catalog.OpencswCatalog)
    catalogs = [
        ("fossil", "amd65", "SolarOS5.12", cat_a, cat_b),
    ]
    previous_pkg = copy.deepcopy(catalog_test.PKG_STRUCT_1)
    previous_pkg["version"] = "previous_version"
    previous_pkg["md5sum"] = "previous_md5"
    cat_a.GetDataByCatalogname().AndReturn({
      "syslog_ng": previous_pkg,
    })
    cat_b.GetDataByCatalogname().AndReturn({
      "syslog_ng": catalog_test.PKG_STRUCT_1,
    })
    rest_client_mock.GetMaintainerByMd5('previous_md5').AndReturn(
        {"maintainer_email": "jack@example.com"}
    )
    rest_client_mock.GetMaintainerByMd5('cfe40c06e994f6e8d3b191396d0365cb').AndReturn(
        {"maintainer_email": "joe@example.com"}
    )
    self.mox.ReplayAll()
    result = f._GetPkgsByMaintainer(catalogs, rest_client_mock)
    self.assertTrue("jack@example.com" in result)
    self.assertEqual({"lost_pkg": {
      catalog_test.PKG_STRUCT_1["file_basename"]: {
        "from_pkg": {previous_pkg["file_basename"]: previous_pkg},
        "to_pkg": catalog_test.PKG_STRUCT_1,
        "catalogs": [("fossil", "amd65", "SolarOS5.12")],
        }}},
      result["jack@example.com"])
    self.assertEqual({"got_pkg": {
      catalog_test.PKG_STRUCT_1["file_basename"]: {
        "from_pkg": {previous_pkg["file_basename"]: previous_pkg},
        "to_pkg": catalog_test.PKG_STRUCT_1,
        "catalogs": [("fossil", "amd65", "SolarOS5.12")],
        }}},
      result["joe@example.com"])
    # Uncomment to see rendered templates
    # print f._RenderForMaintainer(
    #     result["jack@example.com"], "jack@example.com",
    #     "http://mirror.example.com")
    # print f._RenderForMaintainer(
    #     result["joe@example.com"], "joe@example.com",
    #     "http://mirror.example.com")

  def test_GetPkgsByMaintainerUpgrade(self):
    f = catalog_notifier.NotificationFormatter()
    rest_client_mock = self.mox.CreateMock(rest.RestClient)
    cat_a = self.mox.CreateMock(catalog.OpencswCatalog)
    cat_b = self.mox.CreateMock(catalog.OpencswCatalog)
    catalogs = [
        ("fossil", "amd65", "SolarOS5.12", cat_a, cat_b),
    ]
    previous_pkg = copy.deepcopy(catalog_test.PKG_STRUCT_1)
    previous_pkg["version"] = "previous_version"
    previous_pkg["md5sum"] = "previous_md5"
    cat_a.GetDataByCatalogname().AndReturn({
      "syslog_ng": previous_pkg,
    })
    cat_b.GetDataByCatalogname().AndReturn({
      "syslog_ng": catalog_test.PKG_STRUCT_1,
    })
    rest_client_mock.GetMaintainerByMd5('previous_md5').AndReturn(
        {"maintainer_email": "jack@example.com"}
    )
    rest_client_mock.GetMaintainerByMd5('cfe40c06e994f6e8d3b191396d0365cb').AndReturn(
        {"maintainer_email": "jack@example.com"}
    )
    self.mox.ReplayAll()
    result = f._GetPkgsByMaintainer(catalogs, rest_client_mock)
    # pprint.pprint(result)
    self.assertTrue("jack@example.com" in result)
    # In this scenario, we group packages by the target package (after upgrade)
    self.assertEqual({"upgraded_pkg": {
      catalog_test.PKG_STRUCT_1["file_basename"]: {
        "from_pkg": {previous_pkg["file_basename"]: previous_pkg},
        "to_pkg": catalog_test.PKG_STRUCT_1,
        "catalogs": [("fossil", "amd65", "SolarOS5.12")],
        }}},
      result["jack@example.com"])
    # print f._RenderForMaintainer(
    #     result["jack@example.com"], "jack@example.com",
    #     "http://mirror.example.com")


if __name__ == '__main__':
  unittest.main()
