"""A module for generic data structure processing functions."""

import os
import re

MD5_RE = re.compile(r"^[0123456789abcdef]{32}$")
PKGNAME_TICKER_RE = re.compile(r'^CSW')
PKGNAME_CHARS_RE = re.compile(r'[A-Za-z0-9\+]+')


def IndexDictsBy(list_of_dicts, field_key):
  """Creates an index of list of dictionaries by a field name.

  Returns a dictionary of lists.
  """
  index = {}
  for d in list_of_dicts:
    index.setdefault(d[field_key], [])
    index[d[field_key]].append(d)
  return index


def IndexNamedtuplesBy(list_of_namedtuples, field_key):
  """Creates an index of list of dictionaries by a field name.

  Returns a dictionary of lists.
  """
  index = {}
  for named_tuple in list_of_namedtuples:
    value = getattr(named_tuple, field_key)
    index.setdefault(value, []).append(named_tuple)
  return index


def OsReleaseToLong(osrel):
  if osrel.startswith("SunOS"):
    return osrel
  else:
    return "SunOS%s" % osrel


def ResolveSymlink(link_from, link_to):
  target = os.path.normpath(
      os.path.join(os.path.dirname(link_from), link_to))
  return target


def IsMd5(s):
  # For optimization, moving the compilation to the top level.
  return MD5_RE.match(s)


def MakeCatalognameByPkgname(pkgname):
  catalogname = re.sub(PKGNAME_TICKER_RE, '', pkgname)
  catalogname = "_".join(re.findall(PKGNAME_CHARS_RE, catalogname))
  return catalogname
