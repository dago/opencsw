#!/bin/sh

VERSION=`cat $1/VERSION`

prefix='\/opt\/csw'
bindir=$prefix'\/bin'
libdir=$prefix'\/lib'
datadir=$prefix'\/share\/netpbm'
incdir=$prefix'\/include'
mandir=$prefix'\/man'

sed -e '
/^\@/d
s/\@VERSION\@/'"$VERSION"'/
s/\@BINDIR\@/'"$bindir"'/
s/\@LIBDIR\@/'"$libdir"'/
s/\@LINKDIR\@/'"$libdir"'/
s/\@DATADIR\@/'"$datadir"'/
s/\@INCLUDEDIR\@/'"$incdir"'/
s/\@MANDIR\@/'"$mandir"'/
' config_template > $1/bin/netpbm-config

chmod 0755 $1/bin/netpbm-config

