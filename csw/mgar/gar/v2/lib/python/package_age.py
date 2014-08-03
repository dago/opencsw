#!/opt/csw/bin/python

"""Download and generate package age dataset for analysis with R.

It's a toy as of 2014-04-05.

To draw a histogram of package ages, run this in R:

data <- read.table(file="package-ages.txt", header=TRUE,
                   colClasses=c("factor", "factor", "Date"))

png(filename="package-ages.png", width=1024, height=1024)
plot(hist(data$date, breaks="quarters", labels=TRUE, xlab="Quarters",
          axes=FALSE), xaxt="n")
axis(1, data$date, format(data$date, "%Y"), cex.axis = 1.7)
dev.off()
"""

import argparse
import dateutil.parser
import logging
import requests

from lib.python import opencsw


class BadDateError(Exception):
  """There was a bad date tag."""


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('output', help='Output file')
  args = parser.parse_args()
  url = ('http://buildfarm.opencsw.org/pkgdb/rest/catalogs/'
         'unstable/i386/SunOS5.10/timing/')
  data = requests.get(url).json()
  with open(args.output, 'wb') as fd:
    fd.write('catalogname maintainer date\n')
    bad_dates = []
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
      entry['date'] = date.strftime('%Y-%m-%d')
      line = '{catalogname} {maintainer} {date}\n'.format(**entry)
      fd.write(line)
    if bad_dates:
      logging.warning('Bad dates encountered. mtime used as fallback.')


if __name__ == '__main__':
  main()
