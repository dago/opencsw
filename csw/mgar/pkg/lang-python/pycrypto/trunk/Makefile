# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Build fails
#   "src/RIPEMD160.c", line 47: cannot find include file: <stdint.h>
#   "/opt/csw/include/python2.6/pyconfig.h", line 1016: warning: macro redefined: _FILE_OFFSET_BITS
#   cc: acomp failed for src/RIPEMD160.c
#   error: command '/opt/SUNWspro/bin/cc' failed with exit status 2
#

NAME = pycrypto
VERSION = 2.3
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = The Python Cryptography Toolkit
define BLURB
  The Python cryptography toolkit is intended to provide a reliable and
  stable base for writing Python programs that require cryptographic
  functions.
endef

MASTER_SITES = http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/
DISTFILES    = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
