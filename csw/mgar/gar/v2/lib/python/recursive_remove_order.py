#!/opt/csw/bin/python
# coding: utf-8

"""Display in which order to remove packages with safe_remove_pkg.

We do not build this into safe_remove_pkg on purpose: we want the list of
packages to be reviewed by a human before removal.
"""

import logging
import requests
import argparse
import dateutil.parser
import datetime
import jinja2

from collections import namedtuple

from lib.python import opencsw


def RemoveDFS(fd, pkgs_by_pkgname, revdeps, removed, pkgname):
  pkg = pkgs_by_pkgname[pkgname]
  for revdep_pkgname in revdeps[pkgname]:
    RemoveDFS(fd, pkgs_by_pkgname, revdeps, removed, revdep_pkgname)
  c = pkg['catalogname']
  if c not in removed:
    fd.write('./lib/python/safe_remove_package.py --os-releases=SunOS5.9,SunOS5.10,SunOS5.11 -c %s\n' % c)
    removed.add(c)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('pkgname', help='Package to remove (pkgname)')
  parser.add_argument('output', help='output file')
  args = parser.parse_args()
  url = ('http://buildfarm.opencsw.org/pkgdb/rest/catalogs/'
         'unstable/i386/SunOS5.10/timing/')
  data = requests.get(url).json()
  revdeps = {}
  pkgs_by_pkgname = {}
  removed = set()
  for entry in data:
    pkgs_by_pkgname[entry['pkgname']] = entry
    revdeps.setdefault(entry['pkgname'], set())
    for dep in entry['deps']:
      revdeps.setdefault(dep, set()).add(entry['pkgname'])
  with open(args.output, 'wb') as fd:
    RemoveDFS(fd, pkgs_by_pkgname, revdeps, removed, args.pkgname)

if __name__ == '__main__':
  main()
