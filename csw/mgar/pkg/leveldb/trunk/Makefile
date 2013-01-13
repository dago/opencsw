# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Doesn't build, issue filed:
#   http://code.google.com/p/leveldb/issues/detail?id=88
NAME = leveldb
VERSION = 1.9.0
GARTYPE = v2

DESCRIPTION = A fast and lightweight key/value database library by Google
define BLURB  Long description
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

UPSTREAM_MASTER_SITES = http://code.google.com/p/leveldb/TCHFILES += 0001-Set-Solaris-linker-flags-for-v1.9laris-linker-flags.patch

CONFIGURE_ARGS = $(DIRPATHS)

prefix = $(BUILD_PREFIX)/gxx

GARCOMPILER = GNU

BUILD64 = 1

CONFIGURE_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	for f in $(WORKSRC)/libleveldb.*; do \
	  gcp -v $${f} $(DESTDIR)$(libdir); \
	done
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	rsync -rv $(WORKSRC)/include/ $(DESTDIR)$(includedir)
	@$(MAKECOOKIE)

PATH := /op