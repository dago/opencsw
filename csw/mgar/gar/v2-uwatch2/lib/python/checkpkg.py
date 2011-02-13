# $Id$
#
# This is the checkpkg library, common for all checkpkg tests written in
# Python.

import itertools
import logging
import optparse
import os.path
import re
import pprint
import progressbar
import sqlobject
import subprocess
import database

import inspective_package
import models as m
import common_constants
import package_stats
import struct_util


DESCRIPTION_RE = r"^([\S]+) - (.*)$"

INSTALL_CONTENTS_AVG_LINE_LENGTH = 102.09710677919261
SYS_DEFAULT_RUNPATH = [
    "/usr/lib/$ISALIST",
    "/usr/lib",
    "/lib/$ISALIST",
    "/lib",
]

class Error(Exception):
  pass


class ConfigurationError(Error):
  pass


class PackageError(Error):
  pass


class StdoutSyntaxError(Error):
  pass


class SetupError(Error):
  pass


def ExtractDescription(pkginfo):
  desc_re = re.compile(DESCRIPTION_RE)
  m = re.match(desc_re, pkginfo["NAME"])
  return m.group(2) if m else None


def ExtractMaintainerName(pkginfo):
  maint_re = re.compile("^.*for CSW by (.*)$")
  m = re.match(maint_re, pkginfo["VENDOR"])
  return m.group(1) if m else None


def ExtractBuildUsername(pkginfo):
  m = re.match(common_constants.PSTAMP_RE, pkginfo["PSTAMP"])
  return m.group("username") if m else None


def GetPackageStatsByFilenamesOrMd5s(args, debug=False):
  filenames = []
  md5s = []
  for arg in args:
    if struct_util.IsMd5(arg):
      md5s.append(arg)
    else:
      filenames.append(arg)
  srv4_pkgs = [inspective_package.InspectiveCswSrv4File(x) for x in filenames]
  pkgstat_objs = []
  pbar = progressbar.ProgressBar()
  pbar.maxval = len(md5s) + len(srv4_pkgs)
  pbar.start()
  counter = itertools.count()
  for pkg in srv4_pkgs:
    pkgstat_objs.append(package_stats.PackageStats(pkg, debug=debug))
    pbar.update(counter.next())
  for md5 in md5s:
    pkgstat_objs.append(package_stats.PackageStats(None, md5sum=md5, debug=debug))
    pbar.update(counter.next())
  pbar.finish()
  return pkgstat_objs
