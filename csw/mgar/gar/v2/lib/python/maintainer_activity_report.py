#!/opt/csw/bin/python2.7
# coding: utf-8

"""Generate a HTML report of activity of OpenCSW maintainers.

It combines input from a few catalog releases to make sure we get a better
image of activity of a maintainer.
"""

import argparse
import cPickle
import datetime
import dateutil.parser
import jinja2
import json
import logging
import requests

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
    table.activity-report {
      border-collapse: collapse;
    }
    tr.border-bottom td {
      border-bottom: 1px gray;
    }
    .active-False .activity-tag {
      color: brown;
      font-weight: bold;
    }
    .active-True .activity-tag {
      color: green;
      font-weight: bold;
    }
    .retired-True .activity-tag {
      color: #DDD;
    }
    .warning {
      color: red;
      font-weight: bold;
    }
    .retired-True, .retired-True a {
      color: #DDD;
    }
    .action-needed-True, .action-needed-True a {
      background-color: MistyRose;
      color: brown;
    }
  </style>
</head>
<body>
  <h1>OpenCSW Maintainer activity report</h1>

  <h2>Summary</h2>

  <ul>
    <li>{{ counts.active }} active maintainers</li>
    <li>{{ counts.new }} new maintainers</li>
    <li>{{ counts.retired }} retired maintainers</li>
    <li>{{ counts.to_retire }} maintainers to retire</li>
    <li>{{ counts.bogus }} bogus maintainer entries;
        package contents does not match any maintainers in the CSW database</li>
  </ul>

  <h2>Maintainers to retire</h2>

  <p>The following list contains maintainers with no detected activity within
  the last {{ counts.inactive_maintainer_cutoff }} years.</p>

  <p>
  {% for username in analysis_by_username|sort %}
  {% if analysis_by_username[username].to_retire %}
    <a id="{{ username }}" class="maintainer"
    href="http://www.opencsw.org/maintainers/{{ username }}/"
    title="{{ maintainers[username].fullname }}">{{ username }}</a>
  {% endif %}
  {% endfor %}
  </p>
  <p>Bogus maintainers:
  {% for username in analysis_by_username|sort %}
  {% if analysis_by_username[username].bogus %}
    {{ username }}
  {% endif %}
  {% endfor %}
  </p>
  <h2>Activity</h2>
  <table class="activity-report">
  <tr>
    <th>username</th>
    <th>created</th>
    <th>last activity</th>
    <th>years</th>
    <th>new?</th>
    <th>active?</th>
    <th>status in db</th>
    <th>last pkg</th>
    <th># pkgs</th>
    <th>suggestions</th>
  </tr>
  {% for username in maintainers|sort %}
    <tr class="border-bottom active-{{ maintainers[username].active }} retired-{{ maintainers[username].csw_db_status != 'Active' }} action-needed-{{ analysis_by_username[username].to_retire }}">
      <td>
        <a id="{{ username }}" class="maintainer"
        href="http://www.opencsw.org/maintainers/{{ username }}/"
        title="{{ maintainers[username].fullname }}">{{ username }}</a>
      </td>
      <td>
        {% if maintainers[username].date_created %}
        {{ maintainers[username].date_created.strftime('%Y-%m-%d') }}
        {% endif %}
      </td>
      <td>
        {{ maintainers[username].last_activity.strftime('%Y-%m-%d') }}
      </td>
      <td>
        {{ maintainers[username].last_activity_pkg.years }}
      </td>
      <td>
        {% if analysis_by_username[username].new %}
        <span style="background-color: SlateBlue; color: white; padding: 2px;" class="activity-tag">new</span>
        {% else %}
        <span style="color: #AAA;" class="activity-tag">old</span>
        {% endif %}
      </td>
      <td class="activity-tag">
        {% if maintainers[username].active %}
        <span class="activity-tag">active</span>
        {% else %}
        <span class="activity-tag">inactive</span>
        {% endif %}
      </td>
      <td>
        {{ maintainers[username].csw_db_status }}
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
      <td>
        {% if maintainers[username].active and maintainers[username].csw_db_status != 'Active' %}
          <span style="color: brown;">
            inconsistent status
          </span>
        {% endif %}
        {% if analysis_by_username[username].new and not maintainers[username].pkgs %}
          maybe needs help
        {% endif %}
        {% if analysis_by_username[username].bogus %}
          bogus maintainer defined in a package?
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

    # Additional query: maintainers from CSW on the website
    csw_db_url = 'http://www.opencsw.org/buglist/maintainers'
    csw_db_future = executor.submit(lambda: requests.get(csw_db_url).json())
    key_by_future[csw_db_future] = 'csw_db'

    for future in concurrent.futures.as_completed(key_by_future):
      key = key_by_future[future]
      if future.exception() is not None:
        logging.warning('Fetching %r failed:', key, future.exception())
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
  # stable, testing, unstable
  # This has to be updated when a new stable is released.
  catrels = ['bratislava', 'munich', 'unstable']
  if args.load_from:
    with open(args.load_from, 'r') as fd:
      results_by_catrel = cPickle.load(fd)
  else:
    results_by_catrel = ConcurrentFetchResults(catrels)

  if args.save_as:
    with open(args.save_as, 'w') as fd:
      cPickle.dump(results_by_catrel, fd)

  # We need to remove the csw_db part.
  csw_db_maintainers = results_by_catrel['csw_db']
  del results_by_catrel['csw_db']

  # Flatten packages from all catalogs into a single list. For activity
  # detection, we don't care which catalog a maintainer submitted a package to.
  pkgs = [item for sublist in results_by_catrel.values() for item in sublist]

  # Shared code for activity detection. We're processing the unstable catalog
  # separately, so we can detect whether each maintainer has any packages in
  # the unstable catalog.
  maintainers, bad_dates = activity.Maintainers(pkgs)
  maintainers_in_unstable, _ = activity.Maintainers(results_by_catrel['unstable'])

  counts = {
      'active': 0,
      'to_retire': 0,
      'retired': 0,
      'bogus': 0,
      'new': 0,
  }

  for d in csw_db_maintainers:
    # maintainer, fullname, status, date_created
    username = d['maintainer']
    if username in activity.MAINTAINER_STOPLIST:
      continue
    status = d['status']
    date_created = None
    if d['date_created']:
      date_created = dateutil.parser.parse(d['date_created'])
    if username in maintainers:
      maintainers[username] = (
          maintainers[username]._replace(csw_db_status=status,
                                         date_created=date_created,
                                         fullname=d['fullname']))
    else:
      maintainers[username] = (
          activity.Maintainer(
            username=username,
            pkgs={},
            last_activity=datetime.datetime(1970, 1, 1, 0, 0),
            last_activity_pkg=None,
            active=False,
            csw_db_status=status,
            fullname=d['fullname'],
            date_created=date_created))

  csw_db_m_by_username = dict((m['maintainer'], m) for m in csw_db_maintainers)
  analysis_by_username = {}
  now = datetime.datetime.now()
  new_maint_cutoff = now - datetime.timedelta(days=activity.NEW_MAINTAINER_CUTOFF*365)
  for username in maintainers:
    d = {'to_retire': False,
         'bogus': False,
         'new': False}

    # Detect new maintainers. This could be also done in activity.py, because
    # similar functionality already exists there.
    if (maintainers[username].date_created is not None
        and maintainers[username].date_created > new_maint_cutoff
        and maintainers[username].csw_db_status != 'Retired'):
      maintainers[username] = maintainers[username]._replace(active=True)
      d['new'] = True
      counts['new'] += 1

    if username not in csw_db_m_by_username:
      d['bogus'] = True
      counts['bogus'] += 1

    # Some maintainers have bogus activity due to impersonation. If a
    # maintainer is retired in the database, don't count them as active.
    if maintainers[username].active and maintainers[username].csw_db_status != 'Retired':
      counts['active'] += 1
    else:
      if not d['bogus']:
        if maintainers[username].csw_db_status != 'Retired':
          d['to_retire'] = True
          counts['to_retire'] += 1
        else:
          counts['retired'] += 1
    analysis_by_username[username] = d

  counts['inactive_maintainer_cutoff'] = activity.INACTIVE_MAINTAINER_CUTOFF

  with open(args.output, 'w') as outfd:
    template = jinja2.Template(REPORT_TMPL)
    rendered = template.render(
        maintainers=maintainers,
        maintainers_in_unstable=maintainers_in_unstable,
        analysis_by_username=analysis_by_username,
        counts=counts)
    outfd.write(rendered.encode('utf-8'))

  # Save a JSON file too.
  json_out = args.output
  if json_out.endswith('.html'):
    json_out = json_out[:-5] + '.json'
  with open(json_out, 'w') as outfd:
    json.dump(dict(
      maintainers=maintainers,
      maintainers_in_unstable=maintainers_in_unstable,
      analysis_by_username=analysis_by_username,
      counts=counts
    ), outfd, cls=activity.DateTimeEncoder, indent=2)


if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)
  main()
