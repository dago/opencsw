#!/opt/csw/bin/python2.6
# coding=utf-8
#
# $Id$
#
# The idea is to remove the package stats entries (and their blobs, and files)
# for packages that aren't part of any catalogs.
#
# The main query can take a couple minutes. Please be careful with editing
# this script, because if you screw up the main query, it can obliterate the
# whole database. Make backups!

import logging
import sys

import configuration
import models as m
from sqlobject import sqlbuilder

def main():
  configuration.SetUpSqlobjectConnection()
  total_pkgs = m.Srv4FileStats.select().count()
  logging.info("There are {0} packages to inspect.".format(total_pkgs))
  res = m.Srv4FileStats.select(
      sqlbuilder.NOTEXISTS(
        sqlbuilder.Select(m.Srv4FileInCatalog.q.id,
                          where=(
            sqlbuilder.Outer(m.Srv4FileStats).q.id == m.Srv4FileInCatalog.q.srv4file))
      )
    ).orderBy('id')
  deleted_pkgs = 0
  for stats in res:
    # logging.info("Package {0} ({1}) is not in any catalogs. Removing.".format(stats.basename, stats.md5_sum))
    stats.DeleteAllDependentObjects()
    stats.destroySelf()
    deleted_pkgs += 1
    sys.stdout.write(".")
    sys.stdout.flush()
  logging.info("Deleted {0} unused packages.".format(deleted_pkgs))

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  main()
