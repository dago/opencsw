#!/opt/csw/bin/bash

PATH=/opt/csw/bin
WORKSRC=$1

gcp $WORKSRC/Makefile $WORKSRC/Makefile.gcc
gcp $WORKSRC/libtool $WORKSRC/libtool.gcc


perl -i -pnle 's|^(LIBTOOL.*)/libtool$|$1/libtool.gcc|' \
    $WORKSRC/Makefile.gcc
perl -i -pnle 's/-xO3\s*//' $WORKSRC/*.gcc
perl -i -pnle 's/-xarch=v8\s*//' $WORKSRC/*.gcc
perl -i -pnle 's/-mt\|*\s*//' $WORKSRC/*.gcc
perl -i -pnle 's/-KPIC/-fPIC/' $WORKSRC/*.gcc
perl -i -pnle 's/.*CC=.*cc"/LTCC=\/opt\/csw\/gcc4\/bin\/gcc/' \
    $WORKSRC/libtool.gcc
perl -i -pnle 's/.*CC=.*CC"/LTCC=\/opt\/csw\/gcc4\/bin\/g\+\+/' \
    $WORKSRC/libtool.gcc
perl -i -pnle 's/CC =.*$/CC = \/opt\/csw\/gcc4\/bin\/gcc/' \
    $WORKSRC/Makefile.gcc
perl -i -pnle 's/CXX =.*$/CXX = \/opt\/csw\/gcc4\/bin\/g\+\+/' \
    $WORKSRC/Makefile.gcc

