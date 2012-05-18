# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Doesn't build, issue filed:
#   http://code.google.com/p/leveldb/issues/detail?id=88
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

PATCHFILES += 0001-Set-Solaris-linker-flags.patch

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

PATH := /opt/csw/gnu:$(PATH)
