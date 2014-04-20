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
    .can-be-retired-True {
      background-color: #FED;
    }
  </style>
</head>
<body>
  <h1>Maintainer activity report</h1>
  <p>
  </p>
  <table>
  <tr>
    <th>username</th>
    <th>last activity</th>
    <th>years</th>
    <th>active?</th>
    <th>last pkg</th>
    <th># pkgs</th>
  </tr>
  {% for username in maintainers|sort %}
    <tr class="active-{{ maintainers[username].active }} can-be-retired-{{ analysis_by_username[username].can_be_retired }}">
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
    future_to_catrel = dict((executor.submit(Fetch, catrel), catrel)
                            for catrel in catrels)
    for future in concurrent.futures.as_completed(future_to_catrel):
      catrel = future_to_catrel[future]
      if future.exception() is not None:
        logging.warning('Fetching %r failed', url)
      else:
        results_by_catrel[catrel] = future.result()
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

  pkgs = [item for sublist in results_by_catrel.values() for item in sublist]
  maintainers, bad_dates = activity.Maintainers(pkgs)
  maintainers_in_unstable, _ = activity.Maintainers(results_by_catrel['unstable'])

  analysis_by_username = {}
  for username, maintainer in maintainers.iteritems():
    d = {'can_be_retired': False}
    if not maintainer.active:
      if username not in maintainers_in_unstable:
        d['can_be_retired'] = True
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
