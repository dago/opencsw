"""Functions for activity reporting."""

import datetime
import dateutil.parser
import logging

from collections import namedtuple

from lib.python import colors
from lib.python import opencsw

Maintainer = namedtuple('Maintainer',
    ['username', 'pkgs', 'last_activity', 'last_activity_pkg',
     'active', 'csw_db_status', 'fullname', 'date_created'])

INACTIVE_MAINTAINER_CUTOFF = 2
NEW_MAINTAINER_CUTOFF = 2
STALE_PACKAGE_CUTOFF = 4
STALE_FROM_COLOR = '#FFDDBB'
STALE_TO_COLOR = '#F995A0'

def RevDeps(pkgs):
  revdeps = {}
  for entry in pkgs:
    revdeps.setdefault(entry['pkgname'], set())
    for dep in entry['deps']:
      revdeps.setdefault(dep, set()).add(entry['pkgname'])
  return revdeps


def ByPkgname(pkgs):
  pkgs_by_pkgname = {}
  for entry in pkgs:
    pkgs_by_pkgname[entry['pkgname']] = entry
  return pkgs_by_pkgname


def ComputeMaintainerActivity(maintainers):
  now = datetime.datetime.now()
  activity_cutoff = now - datetime.timedelta(days=INACTIVE_MAINTAINER_CUTOFF*365)
  stale_pkg_cutoff = now - datetime.timedelta(days=STALE_PACKAGE_CUTOFF*365)

  for username in maintainers:
    if maintainers[username].last_activity < activity_cutoff:
      maintainers[username] = maintainers[username]._replace(active=False)
    pkgs = maintainers[username].pkgs
    for catalogname in pkgs:
      pkgs[catalogname]['old'] = pkgs[catalogname]['date'] < stale_pkg_cutoff
      # All packages by inactive maintainers are stale by definition
      if not maintainers[username].active:
        pkgs[catalogname]['old'] = True
      age = now - pkgs[catalogname]['date']
      years = '%.1f' % (age.days / 365.0)
      pkgs[catalogname]['age'] = age
      pkgs[catalogname]['years'] = years
      after_cutoff = stale_pkg_cutoff - pkgs[catalogname]['date'] 
      frac = after_cutoff.days / float(365 * 4)
      pkgs[catalogname]['color'] = colors.IntermediateColor(
          STALE_FROM_COLOR, STALE_TO_COLOR, frac)
  return maintainers
 

def Maintainers(pkgs):
  """Process a catalog and compile data structures with activity stats.

  Args:
    pkgs: a list of packages as returned by the catalog timing REST endpoint
  Returns:
    maintainers, bad_dates
  """
  bad_dates = []
  maintainers = {}
  for entry in pkgs:
    entry['maintainer'] = entry['maintainer'].split('@')[0]
    parsed_fn = opencsw.ParsePackageFileName(entry['basename'])
    dates_to_try = []
    if 'REV' in parsed_fn['revision_info']:
      dates_to_try.append(parsed_fn['revision_info']['REV'])
    else:
      logging.warning('{catalogname} did not have a REV=. '
                      'Falling back to mtime.'.format(**entry))
    dates_to_try.append(entry['mtime'])

    for date_str in dates_to_try:
      try:
        date = dateutil.parser.parse(date_str)
        break
      except ValueError as exc:
        logging.warning(exc)
        logging.warning(
            "WTF is {date} in {catalogname}? "
            "Go home {maintainer}, you're drunk.".format(
              catalogname=entry['catalogname'],
              maintainer=entry['maintainer'],
              date=date_str))
        bad_dates.append(date_str)
        continue
    entry['date'] = date
    maintainer = maintainers.setdefault(entry['maintainer'],
        Maintainer(username=entry['maintainer'], pkgs={},
          last_activity=datetime.datetime(1970, 1, 1, 0, 0),
          last_activity_pkg=None,
          active=True,
          csw_db_status=None,
          fullname=None,
          date_created=None))
    if entry['catalogname'] not in maintainer.pkgs:
      maintainer.pkgs[entry['catalogname']] = entry
    if maintainer.last_activity < date:
      maintainer = maintainer._replace(last_activity=date)
      maintainer = maintainer._replace(last_activity_pkg=entry)
      maintainers[maintainer.username] = maintainer

  maintainers = ComputeMaintainerActivity(maintainers)

  return maintainers, bad_dates
