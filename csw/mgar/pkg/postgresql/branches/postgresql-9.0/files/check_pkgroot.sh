#!/opt/csw/bin/bash
# $Id$

declare -r PKGROOT="$1"

if [[ -z "${PKGROOT}" ]]
then
  echo "Please give an argument."
  exit 1
fi

set -u
set -e
set -x

# Look for unexpanded variables
! grep @sysconfdir@ ${PKGROOT}/etc/opt/csw/init.d/cswpostgres_9_0


! test -h ${PKGROOT}/opt/csw/lib/postgresql/9.0/lib/libecpg.so
