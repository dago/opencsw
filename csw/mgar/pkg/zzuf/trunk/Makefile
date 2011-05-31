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

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
