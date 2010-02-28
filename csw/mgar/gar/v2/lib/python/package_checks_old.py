#!/opt/csw/bin/python2.6
# coding=utf-8
# $Id$

import checkpkg
import re

ARCH_RE = re.compile(r"(sparcv(8|9)|i386|amd64)")

MAX_CATALOGNAME_LENGTH = 20
MAX_PKGNAME_LENGTH = 20
MAX_DESCRIPTION_LENGTH = 100
ARCH_LIST = ["sparc", "i386", "all"]
VERSION_RE = r".*,REV=(20[01][0-9]\.[0-9][0-9]\.[0-9][0-9]).*"
ONLY_ALLOWED_IN_PKG = {
    "CSWcommon": ("/opt", "",)
}

def CatalognameLowercase(pkg_data, debug):
  errors = []
  # Here's how to report an error:
  catalogname = pkg_data["basic_stats"]["catalogname"]
  if catalogname != catalogname.lower():
    errors.append(checkpkg.CheckpkgTag(
      pkg_data["basic_stats"]["pkgname"],
      "catalogname-not-lowercase"))
  if not re.match(r"^\w+$", catalogname):
    errors.append(checkpkg.CheckpkgTag(
      pkg_data["basic_stats"]["pkgname"],
      "catalogname-is-not-a-simple-word"))
  return errors


def FileNameSanity(pkg_data, debug):
  errors = []
  basic_stats = pkg_data["basic_stats"]
  revision_info = basic_stats["parsed_basename"]["revision_info"]
  catalogname = pkg_data["basic_stats"]["catalogname"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  if "REV" not in revision_info:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "rev-tag-missing-in-filename"))
  if len(catalogname) > MAX_CATALOGNAME_LENGTH:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "catalogname-too-long"))
  if len(pkgname) > MAX_PKGNAME_LENGTH:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "pkgname-too-long"))
  if basic_stats["parsed_basename"]["osrel"] == "unspecified":
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "osrel-tag-not-specified"))
  return errors


def PkginfoSanity(pkg_data, debug):
  """pkginfo sanity checks.

if [ "$maintname" = "" ] ; then
  # the old format, in the DESC field
  maintname=`sed -n 's/^DESC=.*for CSW by //p' $TMPFILE`

  # Since the DESC field has been coopted, take
  # description from second half of NAME field now.
  desc=`sed -n 's/^NAME=[^ -]* - //p' $TMPFILE`
else
  if [ "$desc" = "" ] ; then
    desc=`sed -n 's/^NAME=[^ -]* - //p' $TMPFILE`
  fi
fi

software=`sed -n 's/^NAME=\([^ -]*\) -.*$/\1/p' $TMPFILE`
version=`sed -n 's/^VERSION=//p' $TMPFILE`
desc=`sed -n 's/^DESC=//p' $TMPFILE`
email=`sed -n 's/^EMAIL=//p' $TMPFILE`
maintname=`sed -n 's/^VENDOR=.*for CSW by //p' $TMPFILE`
hotline=`sed -n 's/^HOTLINE=//p' $TMPFILE`
basedir=`sed -n 's/^BASEDIR=//p' $TMPFILE`
pkgarch=`sed -n 's/^ARCH=//p' $TMPFILE|head -1`

if [ "$software" = "" ] ; then errmsg $f: software field not set properly in NAME ; fi
if [ "$pkgname" = "" ] ; then errmsg $f: pkgname field blank ; fi
if [ "$desc" = "" ] ; then errmsg $f: no description in either NAME or DESC field ; fi
if [ ${#desc} -gt 100 ] ; then errmsg $f: description greater than 100 chars ; fi
if [ "$version" = "" ] ; then errmsg $f: VERSION field blank ;  fi
if [ "$maintname" = "" ] ; then errmsg $f: maintainer name not detected. Fill out VENDOR field properly ; fi
if [ "$email" = "" ] ; then errmsg $f: EMAIL field blank ; fi
if [ "$hotline" = "" ] ; then errmsg $f: HOTLINE field blank ; fi
  """
  errors = []
  catalogname = pkg_data["basic_stats"]["catalogname"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  pkginfo = pkg_data["pkginfo"]
  if not catalogname:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "empty-catalogname"))
  if not pkgname:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "empty-pkgname"))
  if not "VERSION" in pkginfo or not pkginfo["VERSION"]:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "pkginfo-version-field-missing"))
  desc = checkpkg.ExtractDescription(pkginfo)
  if not desc:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "description-missing"))
  if len(desc) > MAX_DESCRIPTION_LENGTH:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "description-too-long"))
  # maintname=`sed -n 's/^VENDOR=.*for CSW by //p' $TMPFILE`
  maintname = checkpkg.ExtractMaintainerName(pkginfo)
  if not maintname:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "maintainer-name-not-set"))
  # email
  if not pkginfo["EMAIL"]:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "email-blank"))
  # hotline
  if not pkginfo["HOTLINE"]:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "hotline-blank"))
  pkginfo_version = pkg_data["basic_stats"]["parsed_basename"]["full_version_string"]
  if pkginfo_version != pkginfo["VERSION"]:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "filename-version-does-not-match-pkginfo-version"))
  if re.search(r"-", pkginfo["VERSION"]):
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "minus-not-allowed-in-version"))
  if not re.match(VERSION_RE, pkginfo["VERSION"]):
    msg = ("Version regex: %s, version value: %s."
           % (repr(VERSION_RE), repr(pkginfo["VERSION"])))
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "version-does-not-match-regex", msg=msg))
  if pkginfo["ARCH"] not in ARCH_LIST:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "non-standard-architecture", pkginfo["ARCH"]))
  if "PSTAMP" in pkginfo:
    if not re.match(checkpkg.PSTAMP_RE, pkginfo["PSTAMP"]):
      errors.append(checkpkg.CheckpkgTag(
        pkgname, "pkginfo-pkstamp-in-wrong-format",
        msg=("It should be 'username@hostname-timestamp', "
             "but it's %s." % repr(pkginfo["PSTAMP"]))))
  else:
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "pkginfo-pstamp-missing"))
  return errors


def ArchitectureSanity(pkg_data, debug):
  errors = []
  basic_stats = pkg_data["basic_stats"]
  pkgname = basic_stats["pkgname"]
  pkginfo = pkg_data["pkginfo"]
  filename = basic_stats["pkg_basename"]
  arch = pkginfo["ARCH"]
  filename_re = r"-%s-" % arch
  if not re.search(filename_re, filename):
    errors.append(checkpkg.CheckpkgTag(
      pkgname, "srv4-filename-architecture-mismatch", arch))
  return errors


def CheckArchitectureVsContents(pkg_data, debug):
  """Verifies the relationship between package contents and architecture."""
  errors = []
  binaries = pkg_data["binaries"]
  pkginfo = pkg_data["pkginfo"]
  pkgmap = pkg_data["pkgmap"]
  arch = pkginfo["ARCH"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  reasons_to_be_arch_specific = []
  pkgmap_paths = [x["path"] for x in pkgmap]
  for pkgmap_path in pkgmap_paths:
    if re.search(ARCH_RE, str(pkgmap_path)):
      reasons_to_be_arch_specific.append((
          "archall-with-arch-paths",
          pkgmap_path,
          "path %s looks arch-specific" % pkgmap_path))
  for binary in binaries:
    reasons_to_be_arch_specific.append((
        "archall-with-binaries",
        binary,
        "package contains binary %s" % binary))
  if arch == "all":
    for tag, param, desc in reasons_to_be_arch_specific:
      errors.append(checkpkg.CheckpkgTag(pkgname, tag, param))
  elif not reasons_to_be_arch_specific:
    # This is not a clean way of handling messages for the user, but there's
    # not better way at the moment.
    print "Package %s does not contain any binaries." % pkgname
    print "Consider making it ARCHALL = 1 instead of %s:" % arch
    print "ARCHALL_%s = 1" % pkgname
    print ("However, be aware that there might be other reasons "
           "to keep it architecture-specific.")
  return errors


def CheckForMissingSymbols(pkgs_data, debug):
  """Analyzes missing symbols reported by ldd -r.

  1. Collect triplets: pkgname, binary, missing symbol
  2. If there are any missing symbols, collect all the symbols that are provided
     by the set of packages.
  3. From the list of missing symbols, remove all symbols that are provided
     by the set of packages.
  4. Report any remaining symbols as errors.

  What indexes do we need?

  symbol -> (pkgname, binary)
  set(allsymbols)
  """
  errors = []
  missing_symbols = []
  all_symbols = set()
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    binaries = pkg_data["binaries"]
    for binary in binaries:
      for ldd_elem in pkg_data["ldd_dash_r"][binary]:
        if ldd_elem["state"] == "symbol-not-found":
          missing_symbols.append((pkgname,
                                  binary,
                                  ldd_elem["symbol"]))
      for symbol in pkg_data["defined_symbols"][binary]:
        all_symbols.add(symbol)
  # Remove symbols defined elsewhere.
  while missing_symbols:
    ms_pkgname, ms_binary, ms_symbol = missing_symbols.pop()
    if ms_symbol not in all_symbols:
      errors.append(checkpkg.CheckpkgTag(
        ms_pkgname, "symbol-not-found", "%s %s" % (ms_binary, ms_symbol)))
  return errors


def CheckBuildingUser(pkg_data, debug):
  errors = []
  pkgname = pkg_data["basic_stats"]["pkgname"]
  username = checkpkg.ExtractBuildUsername(pkg_data["pkginfo"])
  for entry in pkg_data["pkgmap"]:
    if entry["user"] and entry["user"] == username:
      errors.append(checkpkg.CheckpkgTag(
        pkgname,
        "file-owned-by-building-user",
        "%s, %s" % (entry["path"], entry["user"])))
  return errors

def CheckPkgmapPaths(pkg_data, debug):
  errors = []
  username = checkpkg.ExtractBuildUsername(pkg_data["pkginfo"])
  for entry in pkg_data["pkgmap"]:
    file_path = entry["path"]
    if file_path == "/opt":
      errors.append(checkpkg.CheckpkgTag(
        pkgname,
        ("wrong-path-in-pkgmap", file_path)))
  return errors

