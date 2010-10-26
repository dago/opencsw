#!/opt/csw/bin/bash
#
# A small script to run checkpkg against the whole catalog.  The results are
# stored in a sqlite database in ~/.checkpkg.
#
# Architecture
# sparc, i386
arch=sparc

# Solaris version
# 5.9, 5.10
ver=5.9

# OpenCSW release
# current, stable, testing, unstable
release=current

c="/home/mirror/opencsw/${release}/${arch}/${ver}"
readonly c

time \
bin/checkpkg \
  -q \
  -M "${c}/catalog" \
  "${c}/"*.pkg \
  "${c}/"*.pkg.gz
