# Defining the checking functions.  They come in two flavors: individual
# package checks and set checks.

import checkpkg
import re

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
  # Here's how to report an error:
  basic_stats = pkg_data["basic_stats"]
  revision_info = basic_stats["parsed_basename"]["revision_info"]
  catalogname = pkg_data["basic_stats"]["catalogname"]
  if "REV" not in revision_info:
    errors.append(checkpkg.CheckpkgTag(
      pkg_data["basic_stats"]["pkgname"],
      "rev-tag-missing-in-filename"))
  return errors
