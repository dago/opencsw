# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! doesn't build yet
#
#   "libzzuf/lib-stream.c", line 284: warning: implicit function declaration: _zz_init
#   ...
#   "libzzuf/lib-stream.c", line 1044: warning: assignment type mismatch:
#        pointer to function(pointer to struct __FILE {int _cnt, pointer to unsigned char _ptr, pointer to unsigned char _base, unsigned char _flag, unsigned char _file, unsigned int __orientation :2, unsigned int __ionolock :1, unsigned int __seekable :1, unsigned int __filler :4}) returning int "=" pointer to void
#cc: acomp failed for libzzuf/lib-stream.c
#   gmake[4]: *** [libzzuf_la-lib-stream.lo] Error 1
#
# Builds fine with gcc, linking fails though
#
# libtool: link: /opt/csw/gcc4/bin/gcc -DLIBDIR=\"/opt/csw/lib/zzuf\" -I./common -O2 -pipe -mcpu=v8 -g -O2 -Wall -W -Wpointer-arith -Wcast-align -Wcast-qual -Wstrict-prototypes -Wshadow -Waggregate-return -Wmissing-prototypes -Wnested-externs -Wsign-compare -mcpu=v8 -o zzuf zzuf-zzuf.o zzuf-opts.o zzuf-md5.o zzuf-timer.o zzuf-myfork.o zzuf-random.o zzuf-ranges.o zzuf-fd.o zzuf-fuzz.o  -lm -L/opt/csw/gcc4/lib/. -L/opt/csw/lib
#Undefined                       first referenced
# symbol                             in file
#getopt_long                         zzuf-zzuf.o


NAME = zzuf
VERSION = 0.13
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Transparent application input fuzzer
define BLURB
  zzuf is a transparent application input fuzzer. It works by intercepting
  file operations and changing random bits in the program's input. zzuf's
  behaviour is deterministic, making it easy to reproduce bugs.
endef

VENDOR_URL   = http://caca.zoy.org/wiki/zzuf
MASTER_SITES = http://caca.zoy.org/files/zzuf/
DISTFILES    = $(DISTNAME).tar.gz

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
