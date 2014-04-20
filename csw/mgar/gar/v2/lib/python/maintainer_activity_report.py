#!/opt/csw/bin/python2.7
# coding: utf-8

"""Generate a HTML report of activity of OpenCSW maintainers.

It combines input from a few catalog releases to make sure we get a better
image of activity of a maintainer.
"""

import logging
import requests
import argparse
import datetime
import jinja2
import cPickle

import concurrent.futures

from lib.python import activity
from lib.python import colors

REPORT_TMPL = u"""<!DOCTYPE html>
<html>
<head>
  <title>Maintainer activity report</title>
  <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
  <style TYPE="text/css">
    body, p, li {
      font-size: 14px;
      font-family: sans-serif;
    }
    .active-False .maintainer {
      color: brown;
    }
    .active-False .activity-tag {
      color: brown;
      font-weight: bold;
    }
    .active-True .activity-tag {
      color: green;
      font-weight: bold;
    }
    .warning {
      color: red;
      font-weight: bold;
    }
    .retired-True {
      background-color: #DDD;
      color: #AAA;
    }
    .action-needed-True {
      background-color: #FA8;
    }
  </style>
</head>
<body>
  <h1>OpenCSW Maintainer activity report</h1>
  <h2>Maintainers to retire</h2>

  <p>Limitations: This report doesn't know which maintainers are new and which ones are old.
  New maintainers are reported as "to retire" until they release their first
  package. The script only detects activity in the package catalogs. There are
  people who are active in the project, even though they don't release
  packages. They might be wrongly listed here as "to retire". Incorporating the
  mailing list activity should help, but is not implemented right now.</p>

  <p>The following list contains maintainers with no detected activity within
  the last 2 years.</p>

  <p>
  {% for username in analysis_by_username|sort %}
  {% if analysis_by_username[username].to_retire %}
    <a id="{{ username }}" class="maintainer"
    href="http://www.opencsw.org/maintainers/{{ username }}/"
    title="{{ maintainers[username].fullname }}">{{ username }}</a>
  {% endif %}
  {% endfor %}
  </p>
  <h2>Activity</h2>
  <table>
  <tr>
    <th>username</th>
    <th>last activity</th>
    <th>years</th>
    <th>active?</th>
    <th>mantis</th>
    <th>last pkg</th>
    <th># pkgs</th>
  </tr>
  {% for username in maintainers|sort %}
    <tr class="active-{{ maintainers[username].active }} retired-{{ maintainers[username].mantis_status != 'Active' }} action-needed-{{ analysis_by_username[username].to_retire }}">
      <td>
        <a id="{{ username }}" class="maintainer"
        href="http://www.opencsw.org/maintainers/{{ username }}/">{{ username }}</a>
      </td>
      <td>
        {{ maintainers[username].last_activity.strftime('%Y-%m-%d') }}
      </td>
      <td>
        {{ maintainers[username].last_activity_pkg.years }}
      </td>
      <td class="activity-tag">
        {% if maintainers[username].active %}
        <span class="activity-tag">active</span>
        {% else %}
        <span class="activity-tag">inactive</span>
        {% endif %}
      </td>
      <td>
        {{ maintainers[username].mantis_status }}
      </td>
      <td>
        <a href="http://buildfarm.opencsw.org/pkgdb/srv4/{{ maintainers[username].last_activity_pkg.md5_sum }}/">
        {{ maintainers[username].last_activity_pkg.catalogname }}</a>
      </td>
      <td>
        {% if username in maintainers_in_unstable %}
        {{ maintainers_in_unstable[username].pkgs|length }}
        {% endif %}
      </td>
    </tr>
  {% endfor %}
  </table>
</body>
</html>
"""

def ConcurrentFetchResults(catrels):
  def Fetch(catrel):
    url = ('http://buildfarm.opencsw.org/pkgdb/rest/catalogs/'
           '{}/i386/SunOS5.10/timing/'.format(catrel))
    logging.debug('GetPkgs(%r)', url)
    return requests.get(url).json()
  results_by_catrel = {}
  with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    key_by_future = dict((executor.submit(Fetch, catrel), catrel)
                         for catrel in catrels)

    # Additional query: maintainers from Mantis
    mantis_url = 'http://www.opencsw.org/buglist/maintainers'
    mantis_future = executor.submit(lambda: requests.get(mantis_url).json())
    key_by_future[mantis_future] = 'mantis'

    for future in concurrent.futures.as_completed(key_by_future):
      key = key_by_future[future]
      if future.exception() is not None:
        logging.warning('Fetching %r failed', url)
      else:
        results_by_catrel[key] = future.result()
  return results_by_catrel


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('output', help='Output file (HTML)')
  parser.add_argument('--save-as', dest="save_as",
      help="Save data to file; useful when you're modifying the program and "
           "you want to re-run quickly without fetching all the data again.")
  parser.add_argument('--load-from', dest="load_from",
                      help='Load data from file')
  args = parser.parse_args()
  catrels = ['kiel', 'bratislava', 'unstable']
  if args.load_from:
    with open(args.load_from, 'r') as fd:
      results_by_catrel = cPickle.load(fd)
  else:
    results_by_catrel = ConcurrentFetchResults(catrels)

  if args.save_as:
    with open(args.save_as, 'w') as fd:
      cPickle.dump(results_by_catrel, fd)

  # We need to remove the mantis part.
  mantis_maintainers = results_by_catrel['mantis']
  del results_by_catrel['mantis']

  # Flatten packages from all catalogs into a single list. For activity
  # detection, we don't care which catalog a maintainer submitted a package to.
  pkgs = [item for sublist in results_by_catrel.values() for item in sublist]

  # Shared code for activity detection. We're processing the unstable catalog
  # separately, so we can detect whether each maintainer has any packages in
  # the unstable catalog.
  maintainers, bad_dates = activity.Maintainers(pkgs)
  maintainers_in_unstable, _ = activity.Maintainers(results_by_catrel['unstable'])

  for d in mantis_maintainers:
    # maintainer, fullname, status
    username = d['maintainer']
    status = d['status']
    if username in maintainers:
      maintainers[username] = (
          maintainers[username]._replace(mantis_status=status))
    else:
      maintainers[username] = (
          activity.Maintainer(
            username=username,
            pkgs={},
            last_activity=datetime.datetime(1970, 1, 1, 0, 0),
            last_activity_pkg=None,
            active=False,
            mantis_status=status,
            fullname=d['fullname']))

  mantis_m_by_username = dict((m['maintainer'], m) for m in mantis_maintainers)
  analysis_by_username = {}
  for username, maintainer in maintainers.iteritems():
    d = {'can_be_retired': False,
         'to_retire': False,
         'bogus': False}
    if username not in mantis_m_by_username:
      d['bogus'] = True
    if not maintainer.active:
      if username not in maintainers_in_unstable:
        d['can_be_retired'] = True
      if maintainer.mantis_status != 'Retired' and not d['bogus']:
        d['to_retire'] = True
    analysis_by_username[username] = d

  with open(args.output, 'w') as outfd:
    template = jinja2.Template(REPORT_TMPL)
    rendered = template.render(
        maintainers=maintainers,
        maintainers_in_unstable=maintainers_in_unstable,
        analysis_by_username=analysis_by_username)
    outfd.write(rendered.encode('utf-8'))


if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  main()
