#!/opt/csw/bin/bash

PATH=/opt/csw/gnu:/opt/csw/bin:/usr/bin

CONF=$1

DATESTAMP_CONF=$(grep ^version "${CONF}" | cut -d= -f2 \
  | sed -e 's+[^0-9]*\([0-9\.]*\)[^0-9]*+\1+')
DATESTAMP_CLOCK=$(date '+0.%Y.%m')

if [[ "${DATESTAMP_CONF}" != "${DATESTAMP_CLOCK}" ]]; then
  echo >&2
  echo >&2 '*****'
  echo >&2 "Please update the version setting in trunk/files/conf.py to ${DATESTAMP_CLOCK}"
  echo >&2 'and run "mgar clean package"'
  echo >&2 'or "mgar clean install copy-to-web" for testing'
  echo >&2 '*****'
  echo >&2
  exit 1
fi

exit 0
