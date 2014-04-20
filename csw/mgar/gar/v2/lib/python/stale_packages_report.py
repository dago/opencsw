#!/opt/csw/bin/python2.7
# coding: utf-8

"""Retrieve catalog state and generate a HTML report of stale packages."""

import logging
import requests
import argparse
import datetime
import jinja2

from lib.python import activity

REMOVE_SUGGESTION_CUTOFF = 4
REPORT_TMPL = u"""<!DOCTYPE html>
<html>
<head>
  <title>Stale packages report</title>
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
    <li>
      <a href="#could-be-dropped">Package candidates for deleting from the catalog</a>
    </li>
  </ul>
  <h2>Stale packages by maintainer</h2>
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
      ({{ maintainers[username].pkgs[catalogname].years }}
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
  <a href="#" id="could-be-dropped"></a>
  <h2>Packages that could be dropped now</h2>
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


def StalePkgsReport(output_file_name, revdeps, maintainers, pkgs_by_pkgname):
  packages_to_drop = []
  for username in maintainers:
    pkgs = maintainers[username].pkgs
    for catalogname in pkgs:
      # Package dropping logic
      entry = pkgs[catalogname]
      maintainer = maintainers[username]
      if (entry['age'] > datetime.timedelta(days=REMOVE_SUGGESTION_CUTOFF*365) and
          not revdeps[entry['pkgname']] and
          not maintainer.active):
        packages_to_drop.append(entry)

  # Find packages to rebuild
  for username in maintainers:
    pkgs = maintainers[username].pkgs
    for catalogname in pkgs:
      entry = pkgs[catalogname]
      entry['rebuild'] = False
      for revdep_pkgname in revdeps[entry['pkgname']]:
        revdep = pkgs_by_pkgname[revdep_pkgname]
        if not revdep['old'] and entry['old']:
          entry['rebuild'] = True
  with open(output_file_name, 'wb') as fd:
    template = jinja2.Template(REPORT_TMPL)
    fd.write(template.render(maintainers=maintainers, revdeps=revdeps,
             inactive_maint_cutoff=activity.INACTIVE_MAINTAINER_CUTOFF,
             stale_pkg_cutoff=activity.STALE_PACKAGE_CUTOFF,
             packages_to_drop=packages_to_drop,
             remove_suggestion_cutoff=REMOVE_SUGGESTION_CUTOFF).encode('utf-8'))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('output', help='Output file')
  args = parser.parse_args()
  url = ('http://buildfarm.opencsw.org/pkgdb/rest/catalogs/'
         'unstable/i386/SunOS5.10/timing/')
  pkgs = requests.get(url).json()
  maintainers, bad_dates = activity.Maintainers(pkgs)
  revdeps = activity.RevDeps(pkgs)
  pkgs_by_pkgname = activity.ByPkgname(pkgs)
  StalePkgsReport(args.output, revdeps, maintainers, pkgs_by_pkgname)


if __name__ == '__main__':
  main()
