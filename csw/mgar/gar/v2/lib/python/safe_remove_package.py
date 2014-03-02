#!/opt/csw/bin/python2.6

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
import urllib2

from lib.python import configuration

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
EVERY_N_DOTS = 100
datadir = configuration.CHECKPKG_DIR % os.environ
fn_revdeps = os.path.join(datadir, 'revdeps-%s-%s-%s.json')
fn_pkgstatsdb = os.path.join(datadir, 'pkgstats')


class Error(Exception):
  """A generic error."""

class DataError(Exception):
  """Wrong data encountered."""


class RevDeps(object):
  ''' 
  returns a list of [md5_sum,pkgname]
  in the moment not used, perhaps later usefull:
    RevDepsSet = namedtuple('RevDepsSet','md5_sum pkgname')
  '''

  def __init__(self, rest_client=None):
    self.cached_catalogs = {}
    self.cp = rest.CachedPkgstats(fn_pkgstatsdb)
    self.rest_client = rest_client
    if self.rest_client is None:
      config = configuration.GetConfig()
      username, password = rest.GetUsernameAndPassword()
      self.rest_client = rest.RestClient(
          pkgdb_url=config.get('rest', 'pkgdb'),
          releases_url=config.get('rest', 'releases'),
          username=username,
          password=password)

  def MakeRevIndex(self, catrel, arch, osrel, quiet=False):
    key = (catrel, arch, osrel)
    if key in self.cached_catalogs:
      return
    fn = fn_revdeps % key
    if os.path.exists(fn):
      with open(fn, "r") as fd:
        self.cached_catalogs[key] = cjson.decode(fd.read())
      return
    logging.info(
        "Building a database of reverse dependencies. "
        "This can take up to multiple hours.")
    catalog = self.rest_client.GetCatalog(*key)
    rev_deps = {}
    counter = 0
    for pkg_simple in catalog:
      md5 = pkg_simple["md5_sum"]
      # pkg = self.cp.GetPkgstats(md5)
      short_data = self.cp.GetDeps(md5)
      pkgname = short_data["pkgname"]
      for dep_pkgname, _ in short_data["deps"]:
        rev_dep_set = rev_deps.setdefault(dep_pkgname, [])
        rev_dep_set.append((md5, pkgname))
      if not quiet and not counter % EVERY_N_DOTS:
        sys.stdout.write(".")
        sys.stdout.flush()
      counter += 1
    sys.stdout.write("\n")
    self.cached_catalogs[key] = rev_deps
    with open(fn, "w") as fd:
      fd.write(cjson.encode(self.cached_catalogs[key]))

  def RevDepsByMD5(self, catrel, arch, osrel, md5_sum):
    self.MakeRevIndex(catrel, arch, osrel)
    pkg = self.cp.GetPkgstats(md5_sum)
    pkgname = pkg["basic_stats"]["pkgname"]
    key = (catrel, arch, osrel)
    if pkgname in self.cached_catalogs[key]:
      return self.cached_catalogs[key][pkgname]
    else:
      return []

  def RevDepsByPkg(self, catrel, arch, osrel, pkgname):
    self.MakeRevIndex(catrel, arch, osrel)
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
        try:
          pkg_simple = rest_client.Srv4ByCatalogAndCatalogname(UNSTABLE, arch, osrel, catalogname)
        except urllib2.HTTPError, e:
          logging.warning("could not fetch %r from %s/%s: %s",
                          catalogname, arch, osrel, e)
          pkg_simple = None
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
        # pkg = rd.cp.GetPkgstats(md5)
        key = UNSTABLE, arch, osrel
        cat_rev_deps = rd.RevDepsByMD5(UNSTABLE, arch, osrel, md5)
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
  parser.add_option("-c", "--catalogname", dest="catalogname", help='the name of the package in catalog')
  parser.add_option("--os-releases", dest="os_releases",
                    help=("Comma separated OS releases, e.g. "
                          "SunOS5.9,SunOS5.10"))
  parser.add_option("--debug", dest="debug", action="store_true")
  parser.add_option("--dry-run", dest="dry_run",
                    default=False, action="store_true",
                    help=("Don't apply changes (no REST calls)."))
  options, args = parser.parse_args()
  logging_level = logging.INFO
  if options.debug:
    logging_level = logging.DEBUG
  fmt = '%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(message)s'
  logging.basicConfig(format=fmt, level=logging_level)
  if not options.catalogname:
    logging.error('option catalogname required \n%s',USAGE)
    sys.exit(1)
  os_releases = common_constants.OS_RELS
  if options.os_releases:
    os_releases = options.os_releases.split(",")
  pr = PackageRemover()
  pr.RemovePackage(options.catalogname, not options.dry_run, os_releases)


if __name__ == '__main__':
  main()
