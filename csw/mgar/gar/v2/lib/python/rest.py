#!/usr/bin/env python2.6

import logging
import urllib2
import json

BASE_URL = "http://buildfarm.opencsw.org/pkgdb/rest"


class Error(Exception):
  """Generic error."""


class ArgumentError(Error):
  """Wrong arguments passed."""


class RestClient(object):

  def GetPkgByMd5(self, md5_sum):
    url = BASE_URL + "/srv4/%s/" % md5_sum
    logging.debug("GetPkgByMd5(): GET %s", url)
    try:
      data = urllib2.urlopen(url).read()
      return json.loads(data)
    except urllib2.HTTPError, e:
      logging.warning("%s -- %s", url, e)
      return {
          "maintainer_email": "Unknown",
      }

  def GetMaintainerByMd5(self, md5_sum):
    pkg = self.GetPkgByMd5(md5_sum)
    return {
        "maintainer_email": pkg["maintainer_email"],
    }

  def GetCatalog(self, catrel, arch, osrel):
    if not catrel:
      raise ArgumentError("Missing catalog release.")
    url = BASE_URL + "/catalogs/%s/%s/%s/" % (catrel, arch, osrel)
    logging.debug("GetCatalog(): GET %s", url)
    try:
      data = urllib2.urlopen(url).read()
      return json.loads(data)
    except urllib2.HTTPError, e:
      logging.warning("%s -- %s", url, e)
      return None

  def Srv4ByCatalogAndCatalogname(self, catrel, arch, osrel, catalogname):
    """Returns a srv4 data structure or None if not found."""
    url = BASE_URL + (
        "/catalogs/%s/%s/%s/catalognames/%s/"
        % (catrel, arch, osrel, catalogname))
    logging.debug("Srv4ByCatalogAndCatalogname(): GET %s", url)
    try:
      data = urllib2.urlopen(url).read()
      return json.loads(data)
    except urllib2.HTTPError, e:
      logging.warning("%s -- %s", url, e)
      return None
