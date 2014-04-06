#!/opt/csw/bin/python
# coding: utf-8

"""Retrieve catalog state and generate a HTML report of stale packages."""

import logging
import requests
import argparse
import dateutil.parser
import datetime
import jinja2

from collections import namedtuple

from lib.python import opencsw

INACTIVE_MAINTAINER_CUTOFF = 2
STALE_PACKAGE_CUTOFF = 4
REMOVE_SUGGESTION_CUTOFF = 4
REPORT_TMPL = u"""<html>
<head>
  <title>Packages to rebuild</title>
  <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
  <style TYPE="text/css">
    body, p, li {
      font-size: 14px;
      font-family: sans-serif;
    }
    li.inactive .maintainer {
      color: brown;
    }
    li.inactive .activity-tag {
      color: brown;
      font-weight: bold;
    }
    li.active .activity-tag {
      color: green;
      font-weight: bold;
    }
    .warning {
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Stale packages report</h1>
  <p>
  In this report maintainers are marked inactive if they haven't published
  any packages for {{ inactive_maint_cutoff }} years. Packages are marked stale
  after they've reached the age of {{ stale_pkg_cutoff }} years.
  </p>
  <p>
  This cleanup is done as part of <a
  href="https://docs.google.com/document/d/1a5aTPXk5qxnuOng6o2FaQtgr3uqqtEIbCN23WHQgaOc/edit#">OpenCSW Wintercamp in Zürich</a>.
  </p>
  <ul>
  {% for username in maintainers|sort %}
  <li class="{% if maintainers[username].active %}active{% else %}inactive{% endif %}">
  <a id="{{ username }}" class="maintainer" href="http://www.opencsw.org/maintainers/{{ username }}/">{{ username }}</a>
  {% if maintainers[username].active %}
  (<span class="activity-tag">active</span>,
  {% else %}
  (<span class="activity-tag">inactive</span>,
  {% endif %}
  last activity
  {{ maintainers[username].last_activity.strftime('%Y-%m-%d') }}
  <a href="http://buildfarm.opencsw.org/pkgdb/srv4/{{ maintainers[username].last_activity_pkg.md5_sum }}/">
  {{ maintainers[username].last_activity_pkg.catalogname }}</a>)
  <ul>
  {% for catalogname in maintainers[username].pkgs|sort %}
    {% if maintainers[username].pkgs[catalogname].old %}
    <li>
      <a href="http://www.opencsw.org/packages/{{ catalogname }}/"
      title="{{ maintainers[username].pkgs[catalogname].desc }}"
      >
      {{ catalogname }}</a>
      <span style="background: {{ maintainers[username].pkgs[catalogname].color }};">
      ({{ maintainers[username].pkgs[catalogname].age }}
      years{% if revdeps[maintainers[username].pkgs[catalogname].pkgname] %},
      {% if revdeps[maintainers[username].pkgs[catalogname].pkgname]|length > 5 %}
        {{ revdeps[maintainers[username].pkgs[catalogname].pkgname]|length }} revdeps
      {% else %}
        revdeps:
        {% for rd in revdeps[maintainers[username].pkgs[catalogname].pkgname] %}
          {{ rd }}
        {% endfor %}
        {% endif %}
      {% endif %})</span>
      {% if maintainers[username].pkgs[catalogname].rebuild %}
      <span class="warning">REBUILD</span> because newer packages depend on
      this one
      {% endif %}
    </li>
    {% endif %}
  {% endfor %}
  </ul>
  </li>
  {% endfor %}
  </ul>
  <h1>Packages that could be dropped now</h1>
  <p>
  Here's a list of packages that: (1) have inactive maintainers, (2) are older
  than {{ remove_suggestion_cutoff }} years, (3) have no reverse dependencies.
  </p>
<pre>
{% for entry in packages_to_drop|sort(attribute='catalogname') %}
# {{ entry.desc }} (by {{ entry.maintainer }})
./lib/python/safe_remove_package.py --os-releases=SunOS5.9,SunOS5.10,SunOS5.11 -c {{ entry.catalogname }}
{% endfor %}
</pre>
</body>
"""

class BadDateError(Exception):
  """There was a bad date tag."""


Maintainer = namedtuple('Maintainer',
    ['username', 'pkgs', 'last_activity', 'last_activity_pkg', 'active'])



def MakeColorTuple(hc):
  R, G, B = hc[1:3], hc[3:5], hc[5:7]
  R, G, B = int(R, 16), int(G, 16), int(B, 16)
  return R, G, B


def IntermediateColor(startcol, targetcol, frac):
  """Return an intermediate color.

  Fraction can be any rational number, but only the 0-1 range produces
  gradients.
  """
  if frac < 0:
    frac = 0
  if frac >= 1.0:
    frac = 1.0
  sc = MakeColorTuple(startcol)
  tc = MakeColorTuple(targetcol)
  dR = tc[0] - sc[0]
  dG = tc[1] - sc[1]
  dB = tc[2] - sc[2]
  R = sc[0] + dR * frac
  G = sc[1] + dG * frac
  B = sc[2] + dB * frac
  return "#%02x%02x%02x" % (R, G, B)


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('output', help='Output file')
  args = parser.parse_args()
  url = ('http://buildfarm.opencsw.org/pkgdb/rest/catalogs/'
         'unstable/i386/SunOS5.10/timing/')
  data = requests.get(url).json()

  bad_dates = []
  revdeps = {}
  maintainers = {}
  packages_to_drop = []
  for entry in data:
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
          active=True))
    if entry['catalogname'] not in maintainer.pkgs:
      maintainer.pkgs[entry['catalogname']] = entry
    if maintainer.last_activity < date:
      maintainer = maintainer._replace(last_activity=date)
      maintainer = maintainer._replace(last_activity_pkg=entry)
      maintainers[maintainer.username] = maintainer
    revdeps.setdefault(entry['pkgname'], set())
    for dep in entry['deps']:
      revdeps.setdefault(dep, set()).add(entry['pkgname'])
  del entry
  if bad_dates:
    logging.warning('Bad dates encountered. mtime used as fallback.')
  now = datetime.datetime.now()
  activity_cutoff = now - datetime.timedelta(days=INACTIVE_MAINTAINER_CUTOFF*365)
  stale_pkg_cutoff = now - datetime.timedelta(days=STALE_PACKAGE_CUTOFF*365)

  # Make an index by pkgname
  pkgs_by_pkgname = {}
  for maintainer in maintainers.itervalues():
    for catalogname in maintainer.pkgs:
      entry = maintainer.pkgs[catalogname]
      pkgs_by_pkgname[entry['pkgname']] = entry

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
      pkgs[catalogname]['age'] = years
      after_cutoff = stale_pkg_cutoff - pkgs[catalogname]['date'] 
      frac = after_cutoff.days / float(365 * 4)
      # frac = age.days / (365 * 4)
      pkgs[catalogname]['color'] = IntermediateColor('#FFCC00', '#F995A0', frac)
      
      # Package dropping logic
      entry = pkgs[catalogname]
      maintainer = maintainers[username]
      if (age > datetime.timedelta(days=REMOVE_SUGGESTION_CUTOFF*365) and
          not revdeps[entry['pkgname']] and
          not maintainer.active):
        packages_to_drop.append(entry)

  # Find packages to rebuild
  #
  for username in maintainers:
    pkgs = maintainers[username].pkgs
    for catalogname in pkgs:
      entry = pkgs[catalogname]
      entry['rebuild'] = False
      for revdep_pkgname in revdeps[entry['pkgname']]:
        revdep = pkgs_by_pkgname[revdep_pkgname]
        if not revdep['old'] and entry['old']:
          entry['rebuild'] = True
  with open(args.output, 'wb') as fd:
    template = jinja2.Template(REPORT_TMPL)
    fd.write(template.render(maintainers=maintainers, revdeps=revdeps,
             inactive_maint_cutoff=INACTIVE_MAINTAINER_CUTOFF,
             stale_pkg_cutoff=STALE_PACKAGE_CUTOFF,
             packages_to_drop=packages_to_drop,
             remove_suggestion_cutoff=REMOVE_SUGGESTION_CUTOFF).encode('utf-8'))


if __name__ == '__main__':
  main()
