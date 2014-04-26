# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = avl
VERSION = 2.0.3
GARTYPE = v2

DESCRIPTION = Binary search tree and balanced tree library

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://adtinfo.org

BUILD64 = 1

# There is no configure
CONFIGURE_SCRIPTS =

BUILD_ARGS += CC=$(CC)
BUILD_ARGS += CFLAGS="$(CFLAGS)"
BUILD_ARGS += LDFLAGS="$(LDFLAGS)"

include gar/category.mk

