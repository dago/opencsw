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

# The 5.05 version has a pure Python rewrite of the Python bindings.
# test -f ${PKGROOT}/opt/csw/lib/python/site-packages/magic.so
