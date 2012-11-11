#!/usr/bin/env python2.6

"""Helps to safely remove a package (by catalogname) from the catalog.

Takes a catalog name and:

  - checks all the catalogs and gets the md5 sums for each catalog
  - checks for reverse dependencies; if there are any, stops
  - when there are no rev deps, makes a REST call to remove the package

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

USAGE = """%prog --os-releases=SunOS5.10,SunOS5.11 -c <catalogname>

A practical usage example - let's say we have a list of packages to remove in
a file named 'pkg-list.txt'. We'll also have a cache of packages already
removed in packages_dropped_cache.txt. The following call will remove the
listed packages:

for p in $(cat pkg-list.txt)
do
	if ! ggrep "^$p\$" packages_dropped_cache.txt > /dev/null
  then
    ./safe_remove_package.py \\
        --os-releases=SunOS5.10,SunOS5.11 \\
        -c "$p"
  fi
done
"""


UNSTABLE = "unstable"

class Error(Exception):
  """A generic error."""

class DataError(Exception):
  """Wrong data encountered."""

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

  def CachePackageIsGone(self, catalogname):
    with open("packages_dropped_cache.txt", "ab") as fd:
      fd.write("{0}\n".format(catalogname))

  def RemovePackage(self, catalogname, execute=False, os_releases=None):
    if not os_releases:
      os_releases = common_constants.OS_RELS
    username, password = rest.GetUsernameAndPassword()
    rest_client = rest.RestClient(username=username, password=password)
    rd = RevDeps()
    rev_deps = {}
    # md5 sums to remove
    to_remove = []
    found_anywhere = False
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
        pkg_simple = rest_client.Srv4ByCatalogAndCatalogname(UNSTABLE, arch, osrel, catalogname)
        if not pkg_simple:
          # Maybe we were given a pkgname instead of a catalogname? We can try
          # that before failing.
          pkg_simple = rest_client.Srv4ByCatalogAndPkgname(
              UNSTABLE, arch, osrel, catalogname)
          if not pkg_simple:
            msg = "{0} was not in the unstable {1} {2} catalog."
            logging.debug(msg.format(repr(catalogname), arch, osrel))
            continue
        if pkg_simple:
          found_anywhere = True
        md5 = pkg_simple["md5_sum"]
        pkg = rd.cp.GetPkgstats(md5)
        key = UNSTABLE, arch, osrel
        cat_rev_deps = rd.RevDeps(UNSTABLE, arch, osrel, md5)
        if cat_rev_deps:
          rev_deps[key] = cat_rev_deps
        to_remove.append((UNSTABLE, arch, osrel, md5))
    if not found_anywhere:
      self.CachePackageIsGone(catalogname)
    if rev_deps:
      print "Not removing, rev-deps present: ",
      print pkg_simple["catalogname"], ":", " ; ".join(
          ["%s %s %s %s"
            % (x[0], x[1], x[2], ",".join(y[1] for y in rev_deps[x]))
            for x in rev_deps])
    else:
      for catrel, arch, osrel, md5_sum in to_remove:
        print "# [%s]" % pkg_simple["catalogname"], catrel, arch, osrel, md5_sum
        if execute:
          rest_client.RemoveSvr4FromCatalog(catrel, arch, osrel, md5_sum)
      if found_anywhere:
        self.CachePackageIsGone(catalogname)


def main():
  parser = optparse.OptionParser(USAGE)
  parser.add_option("-c", "--catalogname", dest="catalogname")
  parser.add_option("--os-releases", dest="os_releases",
                    help=("Comma separated OS releases, e.g. "
                          "SunOS5.9,SunOS5.10"))
  parser.add_option("--debug", dest="debug", action="store_true")
  parser.add_option("--dry-run", dest="dry_run",
                    default=False, action="store_true",
                    help=("Don't remove the packages packages."))
  options, args = parser.parse_args()
  debug_level = logging.INFO
  if options.debug:
    debug_level = logging.DEBUG
  logging.basicConfig(level=debug_level)
  os_relases = None
  if options.os_releases:
    os_releases = options.os_releases.split(",")
  pr = PackageRemover()
  pr.RemovePackage(options.catalogname, not options.dry_run, os_releases)


if __name__ == '__main__':
  main()
