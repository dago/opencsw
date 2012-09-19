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


class Error(Exception):
  """A generic error."""

class RevDeps(object):

  def __init__(self):
    self.cached_catalogs = {}
    self.rest_client = rest.RestClient()
    self.cp = rest.CachedPkgstats("pkgstats")

  def MakeRevIndex(self, catrel, arch, osrel):
    key = (catrel, arch, osrel)
    if key in self.cached_catalogs:
      return
    fn = "revdeps-%s-%s-%s.json" % key
    if os.path.exists(fn):
      with open(fn, "r") as fd:
        self.cached_catalogs[key] = cjson.decode(fd.read())
      return
    catalog = self.rest_client.GetCatalog(*key)
    rev_deps = {}
    for pkg_simple in catalog:
      # pprint.pprint(pkg_simple)
      md5 = pkg_simple["md5_sum"]
      # pkg = self.cp.GetPkgstats(md5)
      short_data = self.cp.GetDeps(md5)
      pkgname = short_data["pkgname"]
      for dep_pkgname, _ in short_data["deps"]:
        rev_dep_set = rev_deps.setdefault(dep_pkgname, list())
        rev_dep_set.append((md5, pkgname))
    self.cached_catalogs[key] = rev_deps
    with open(fn, "w") as fd:
      fd.write(cjson.encode(self.cached_catalogs[key]))

  def RevDeps(self, catrel, arch, osrel, md5_sum):
    self.MakeRevIndex(catrel, arch, osrel)
    pkg = self.cp.GetPkgstats(md5_sum)
    pkgname = pkg["basic_stats"]["pkgname"]
    key = (catrel, arch, osrel)
    if pkgname in self.cached_catalogs[key]:
      return self.cached_catalogs[key][pkgname]
    else:
      return []


class PackageRemover(object):

  def RemovePackage(self, catalogname, execute=False, os_releases=None):
    if not os_releases:
      os_releases = common_constants.OS_RELS
    # Get md5 sums
    rest_client = rest.RestClient()
    rd = RevDeps()
    rev_deps = {}
    to_remove = {}
    for osrel in os_releases:
      if osrel not in common_constants.OS_RELS:
        logging.warning(
            "%s not found in common_constants.OS_RELS (%s). Skipping.",
            osrel, common_constants.OS_RELS)
        continue
      if osrel in common_constants.OBSOLETE_OS_RELS:
        logging.info("%s is an obsolete OS release. Skipping.", osrel)
        continue
      for arch in common_constants.PHYSICAL_ARCHITECTURES:
        pkg_simple = rest_client.Srv4ByCatalogAndCatalogname("unstable", arch, osrel, catalogname)
        md5 = pkg_simple["md5_sum"]
        pkg = rd.cp.GetPkgstats(md5)
        key = "unstable", arch, osrel
        cat_rev_deps = rd.RevDeps("unstable", arch, osrel, md5)
        if cat_rev_deps:
          rev_deps[key] = cat_rev_deps
        f = (
            "/home/mirror/opencsw/unstable/%s/%s/%s"
            % (arch, osrel.replace("SunOS", ""), pkg["basic_stats"]["pkg_basename"]))
        files = to_remove.setdefault(osrel, [])
        files.append(f)
    if rev_deps:
      print "Reverse dependencies found. Bailing out."
      pprint.pprint(rev_deps)
    else:
      for osrel in to_remove:
        args = ["csw-upload-pkg", "--remove", "--os-release",
            osrel] + to_remove[osrel]
        print " ".join(args)
        if execute:
          subprocess.call(args)



def main():
  parser = optparse.OptionParser()
  parser.add_option("-c", "--catalogname", dest="catalogname")
  parser.add_option("--os-releases", dest="os_releases",
                    help=("Comma separated OS releases, e.g. "
                          "SunOS5.9,SunOS5.10"))
  parser.add_option("--debug", dest="debug", action="store_true")
  parser.add_option("--execute", dest="execute", action="store_true",
                    help=("Don't just display, but execute and remove the "
                          "packages."))
  options, args = parser.parse_args()
  debug_level = logging.INFO
  if options.debug:
    debug_level = logging.DEBUG
  logging.basicConfig(level=debug_level)
  os_relases = None
  if options.os_releases:
    os_releases = options.os_releases.split(",")
  pr = PackageRemover()
  pr.RemovePackage(options.catalogname, options.execute, os_releases)


if __name__ == '__main__':
  main()
