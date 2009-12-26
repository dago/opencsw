#!/bin/bash
####################################################
#
#  fixme2.sh
#  Intended to patch libtool so relink isn't
#  performend during install
# 
#  Loosely based on Mike Watters fixme.sh
#
#  Author: Roger Hakansson hson at opencsw.org
#  Initial Version: 0.1
#
####################################################

umask 0022
PATH=/opt/csw/bin

if [ $# -ne 1 ]; then
    gecho "USAGE: $(basename $0) WORKSRC"
    exit 1
fi
BASEPATH=$1

## Fix libtool Script
for lt in $(gfind ${BASEPATH} -name libtool -print); do
    gsed 's/test "$mode" != relink && rpath/rpath/' ${lt} > ${lt}.new
    gmv ${lt}.new ${lt}
    gchmod +x ${lt}
done
