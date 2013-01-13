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

UPSTREAM_MASTER_SITES = http://code.google.com/p/leveld# AtomicPointer implementation is lacking for SPARC
PACKAGING_PLATFORMS = solaris10-i386ldb/TCHFILES += 0001-Set-Solaris-linker-flags-for-v1.9laris-linker-flags.patch

CONFIGURE_ARGS = $(DIRPATHS)

prefix = $(BUILD_PREFIX)/gxx

GARCOMPILER = GNU

BUILD64 = 1

CONFIGURE_SCRIPTS =
INSTALL_PACKAGES += CSWlibleveldb1-gxx
PKGFILES_CSWlibleveldb1-gxx += $(call baseisadirs,$(libdir),libleveldb\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibleveldb1-gxx += $(DESCRIPTION), libleveldb.so.1
RUNTIME_DEP_PKGS_CSWlibleveldb1-gxx += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibleveldb1-gxx += CSWlibstdc++6

PACKAGES += CSWlibleveldb1-gxx-dev
RUNTIME_DEP_PKGS_CSWleveldb-gxx-dev += CSWlibleveldb1-gxx
SPKG_DESC_CSWlibleveldb1-gxx-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibleveldb1-gxx-dev += CSWlibleveldb1-gxx

include gar/category.mk

install-custom:
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	rsync -rvl $(WORKSRC)/libleveldb.* $(DESTDIR)$(libdir)
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	rsync -rvl $(WORKSRC)/include/ $(DESTDIR)$(includedir)
	ginstall -d -m 755 $(DESTDIR)$(docdir)
	rsync -rvl $(WORKSRC)/doc/ $(DESTDIR)$(docdir)
	@$(MAKECOOKIE)

PATH := /opt/csw/gnu:$(PATH)
