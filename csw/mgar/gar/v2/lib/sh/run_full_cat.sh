#!/opt/csw/bin/bash

# A small script to run checkpkg against the whole catalog

c="/home/mirror/opencsw/current/sparc/5.9"
bin/checkpkg \
  -q \
  -M "${c}/catalog" \
  "${c}/"*.pkg \
  "${c}/"*.pkg.gz
