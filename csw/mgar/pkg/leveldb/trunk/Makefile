# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = leveldb
VERSION = 1.4.0
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

UPSTREAM_MASTER_SITES = http://code.google.com/p/leveldb/downloads/list

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

CONFIGURE_ARGS = $(DIRPATHS)

prefix = $(BUILD_PREFIX)/gxx

GARCOMPILER = GNU

BUILD64 = 1

CONFIGURE_SCRIPTS =

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
