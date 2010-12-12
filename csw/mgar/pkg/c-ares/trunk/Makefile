NAME = c-ares
VERSION = 1.7.0
CATEGORIES = lib

DESCRIPTION = c-ares library to perform DNS requests and name resolves asynchronously
define BLURB
endef

MASTER_SITES = http://c-ares.haxx.se/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += ares_build.h

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibcares CSWlibcaresdevel

CATALOGNAME_CSWlibcares = libcares
CATALOGNAME_CSWlibcaresdevel = libcares_devel

SPKG_DESC_CSWlibcares = $(DESCRIPTION)
SPKG_DESC_CSWlibcaresdevel = c-ares library developer files

RUNTIME_DEP_PKGS_CSWlibcaresdevel = CSWlibcares

LICENSE = README.cares

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

EXTRA_PAX_ARGS_32 = -s ",^\.$(includedir)/ares_build.h$$,.$(includedir)/ares_build-32.h,p"
EXTRA_PAX_ARGS_64 = -s ",^\.$(includedir)/ares_build.h$$,.$(includedir)/ares_build-64.h,p"
EXTRA_PAX_ARGS = $(EXTRA_PAX_ARGS_$(MEMORYMODEL))

PKGFILES_CSWlibcaresdevel = $(PKGFILES_DEVEL)

include gar/category.mk

post-merge:
	ginstall $(FILEDIR)/ares_build.h $(PKGROOT)$(includedir)/ares_build.h
	@$(MAKECOOKIE)
