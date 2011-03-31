NAME = c-ares
VERSION = 1.7.4
CATEGORIES = lib

DESCRIPTION = C-ares library to perform DNS requests and name resolves asynchronously
define BLURB
endef

MASTER_SITES = http://c-ares.haxx.se/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += ares_build.h

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWlibcares2
CATALOGNAME_CSWlibcares2 = libcares2
SPKG_DESC_CSWlibcares2 = C-ares library to perform DNS requests and name resolves asynchronously
PKGFILES_CSWlibcares2 = $(call pkgfiles_lib,libcares.so.2)
OBSOLETED_BY_CSWlibcares2 = CSWlibcares

PACKAGES += CSWlibcares-dev
CATALOGNAME_CSWlibcares-dev = libcares_dev
SPKG_DESC_CSWlibcares-dev = Development files for libcares.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibcares-dev += CSWlibcares2
OBSOLETED_BY_CSWlibcares-dev = CSWlibcaresdevel

RUNTIME_DEP_PKGS_CSWlibcaresdevel = CSWlibcares

LICENSE = README.cares

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_PAX_ARGS_32 = -s ",^\.$(includedir)/ares_build.h$$,.$(includedir)/ares_build-32.h,p"
EXTRA_PAX_ARGS_64 = -s ",^\.$(includedir)/ares_build.h$$,.$(includedir)/ares_build-64.h,p"
EXTRA_PAX_ARGS = $(EXTRA_PAX_ARGS_$(MEMORYMODEL))

include gar/category.mk

post-merge:
	ginstall $(FILEDIR)/ares_build.h $(PKGROOT)$(includedir)/ares_build.h
	@$(MAKECOOKIE)
