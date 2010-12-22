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


DO_NOT_REPORT_SURPLUS = set([u"CSWcommon", u"CSWcswclassutils", u"CSWisaexec"])
DO_NOT_REPORT_MISSING = set([])
DO_NOT_REPORT_MISSING_RE = [r"\*?SUNW.*"]
DUMP_BIN = "/usr/ccs/bin/dump"
PSTAMP_RE = r"(?P<username>\w+)@(?P<hostname>[\w\.-]+)-(?P<timestamp>\d+)"
DESCRIPTION_RE = r"^([\S]+) - (.*)$"
BAD_CONTENT_REGEXES = (
    # Slightly obfuscating these by using concatenation of strings.
    r'/export' r'/medusa',
    r'/opt' r'/build',
)

INSTALL_CONTENTS_AVG_LINE_LENGTH = 102.09710677919261
SYS_DEFAULT_RUNPATH = [
    "/usr/lib/$ISALIST",
    "/usr/lib",
    "/lib/$ISALIST",
    "/lib",
]

MD5_RE = re.compile(r"^[0123456789abcdef]{32}$")

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


def GetOptions():
  parser = optparse.OptionParser()
  parser.add_option("-d", "--debug", dest="debug",
                    default=False, action="store_true",
                    help="Turn on debugging messages")
  parser.add_option("-p", "--profile", dest="profile",
                    default=False, action="store_true",
                    help=("Turn on profiling"))
  parser.add_option("-q", "--quiet", dest="quiet",
                    default=False, action="store_true",
                    help=("Print less messages"))
  (options, args) = parser.parse_args()
  # Using set() to make the arguments unique.
  return options, set(args)


def ExtractDescription(pkginfo):
  desc_re = re.compile(DESCRIPTION_RE)
  m = re.match(desc_re, pkginfo["NAME"])
  return m.group(2) if m else None


def ExtractMaintainerName(pkginfo):
  maint_re = re.compile("^.*for CSW by (.*)$")
  m = re.match(maint_re, pkginfo["VENDOR"])
  return m.group(1) if m else None


def ExtractBuildUsername(pkginfo):
  m = re.match(PSTAMP_RE, pkginfo["PSTAMP"])
  return m.group("username") if m else None


def IsMd5(s):
  # For optimization, move the compilation elsewhere.
  return MD5_RE.match(s)

def GetPackageStatsByFilenamesOrMd5s(args, debug=False):
  filenames = []
  md5s = []
  for arg in args:
    if IsMd5(arg):
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
