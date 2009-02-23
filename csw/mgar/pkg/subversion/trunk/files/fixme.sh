#!/bin/bash

touch /tmp/mike-fixme

umask 0022
PATH=/opt/csw/bin:/usr/bin:/sbin

if [ $# -ne 1 ]; then
    echo "USAGE: $(basename $0) WORKSRC"
    exit 1
fi
BASEPATH=$1

## Fix Makefiles
for mk in $(gfind ${BASEPATH} -name Makefile -print); do
    LT_FILES=$(ggrep '/opt/csw.*/lib/.*.la' ${mk} | \
        gsed "s/^.*\(\/opt\/csw.*\/lib\/.*\.la\).*$/\1/")
    
    for file in ${LT_FILES}; do
        LIB_NAME=$(ggrep dlname= ${file} | \
            gsed -e "s/.*'\(.*\)'/\1/" \
                -e "s/^lib//" \
                -e "s/\.so.*$//")
        fixpath=$(echo $file |gsed 's/\//\\\//g')
        sed "s/${fixpath}/-l${LIB_NAME}/g" \
            ${mk} >Makefile.new
        mv Makefile.new ${mk}
    done
done

## Fix libtool
for lt in $(gfind ${BASEPATH} -name libtool -print); do
    gsed "/for search_ext in .*\.la/s/\.la//" ${lt} >${lt}.new
    mv ${lt}.new ${lt}
done

