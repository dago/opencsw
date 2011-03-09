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

# This file was missing in file-5.05, and that broke py_libmagic.
test -f ${PKGROOT}/opt/csw/lib/python/site-packages/magic.so
