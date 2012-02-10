#!/opt/csw/bin/bash

set -x
set -u
set -e

for f in $1/opt/csw/share/doc/ct-ng-1.13.2/*; do
  no_spaces=$(basename $(echo "$f" | gtr ' ' '_'))
  d=$1/opt/csw/share/doc/ct-ng-1.13.2
  gmv "${f}" "${d}/${no_spaces}"
done
