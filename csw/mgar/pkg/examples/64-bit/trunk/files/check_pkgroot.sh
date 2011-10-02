#!/opt/csw/bin/bash
# $Id$

set -u
set -e
set -x

declare -r PKGROOT="$1"

function must_not_exist {
local f="$1"
if [[ -e "$f" ]]; then
  echo "'$f' must not exist, but it does"
  return 1
else
  echo "good, '$f' does not exist"
  return 0
fi
}

function must_exist {
local f="$1"
if [[ -e "$f" ]]; then
  echo "good, '$f' exists"
  return 0
else
  echo "'$f' must exist, but it doesn't"
  return 1
fi
}

if [[ -z "${PKGROOT}" ]]
then
  echo "Please pass PKGROOT as an argument."
  exit 1
fi

tree ${PKGROOT}/opt/csw

must_not_exist ${PKGROOT}/opt/csw/foo/lib/sparcv9/libhello.so.0.0.0
must_exist ${PKGROOT}/opt/csw/lib/sparcv9/libhello.so.0.0.0
