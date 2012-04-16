#!/usr/bin/env python2.6

"""Helps to safely remove a package (by catalogname) from the catalog.

Takes a catalog name and:

  - checks all the catalogs and gets the md5 sums for each catalog
  - checks for reverse dependencies; if there are any, stops
  - when there are no rev deps, prints a csw-upload-pkg --remove call
"""

import optparse
import rest
import common_constants
import pprint
import gdbm
import logging
import sys
import os
import cjson
import subprocess

catrel = 'unstable'

class FindBins(object):

  def __init__(self):
    self.cached_catalogs_bins = {}
    self.cached_catalogs_needed_bins = {}
    self.rest_client = rest.RestClient()
    self.cp = rest.CachedPkgstats("pkgstats.db")

  def MakeRevIndex(self, catrel, arch, osrel):
    key = (catrel, arch, osrel)
    if key in self.cached_catalogs_bins:
      return
    fn_bins = "bins-%s-%s-%s.json" % key
    if os.path.exists(fn_bins):
      with open(fn_bins, "r") as fd:
        self.cached_catalogs_bins[key] = cjson.decode(fd.read())
    fn_needed_bins = "needed-bins-%s-%s-%s.json" % key
    if os.path.exists(fn_needed_bins):
      with open(fn, "r") as fd:
        self.cached_catalogs_needed_bins[key] = cjson.decode(fd.read())
      return
    catalog = self.rest_client.GetCatalog(*key)
    bins = {}
    needed_bins = {}
    for pkg_simple in catalog:
      cb = []
      nb = []
      # pprint.pprint(pkg_simple)
      md5 = pkg_simple["md5_sum"]
      pkg = self.cp.GetPkgstats(md5)
      if not pkg:
        logging.warning("No package for %r", md5)
        continue
      try:   
        pkg_name = pkg["basic_stats"]["pkgname"]
        for p in pkg['binaries_dump_info']:
          for b in p['needed sonames']:
            if b not in needed_bins:
              nb.append(b)
        for b in pkg['binaries']:
            if b not in bins:
              cb.append(b)
        bins[pkg_name] = cb
        needed_bins[pkg_name] = nb
        sys.stdout.write(".")
        sys.stdout.flush()
      except KeyError:
        logging.warning("MakeRevIndex: no pkg structure: ")
        # logging.warning(pkg)
    sys.stdout.write("\n")
    self.cached_catalogs_bins[key] = bins
    self.cached_catalogs_needed_bins[key] = needed_bins
    with open(fn_bins, "w") as fd:
      fd.write(cjson.encode(self.cached_catalogs_bins[key]))
    with open(fn_needed_bins, "w") as fd:
      fd.write(cjson.encode(self.cached_catalogs_needed_bins[key]))

  def getBins(self, catrel, arch, osrel):
    self.MakeRevIndex(catrel, arch, osrel)
    key = (catrel, arch, osrel)
    return self.cached_catalogs_bins[key]

  def getNeededBins(self, catrel, arch, osrel):
    self.MakeRevIndex(catrel, arch, osrel)
    key = (catrel, arch, osrel)
    return self.cached_catalogs_needed_bins[key]

class PackageScanner(object):

  def scanPackage(self):
    # Get md5 sums
    rest_client = rest.RestClient()
    rd = FindBins()
    needed_bins = {}
    for osrel in common_constants.OS_RELS:
      if osrel in common_constants.OBSOLETE_OS_RELS:
        continue
      for arch in common_constants.PHYSICAL_ARCHITECTURES:
        bins = rd.getBins(catrel, arch, osrel)
        needed_bins = rd.getNeededBins(catrel, arch, osrel)
        for pkg in bins:
          print pkg, bins[pkg]
        

    print "found:"
    pprint.pprint(needed_bins)

def main():
  parser = optparse.OptionParser()
  parser.add_option("--debug", dest="debug", action="store_true")
  options, args = parser.parse_args()
  if options.debug:
    logging.basicConfig(level=logging.DEBUG)
  pr = PackageScanner()
  pr.scanPackage()


if __name__ == '__main__':
  main()
