# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libmng
VERSION = 1.0.10
GARTYPE = v2

DESCRIPTION = Library for Multiple-image Network Graphics format (MNG)

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.bz2

# Taken from https://github.com/freddix/libmng
PATCHFILES += libmng-automake.patch
PATCHFILES += libmng-gcc4.patch

PATCHFILES += 0001-Do-not-use-AM_C_PROTOTYPES-any-more.patch

VENDOR_URL = http://libmng.com

BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWliblcms-dev
BUILD_DEP_PKGS += CSWlibz-dev

PACKAGES += CSWlibmng1
SPKG_DESC_CSWlibmng1 = Library for Multiple-image Network Graphics format (MNG), libmng.so.1
PKGFILES_CSWlibmng1 += $(call pkgfiles_lib,libmng.so.1)
RUNTIME_DEP_PKGS_CSWlibmng1 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibmng1 += CSWliblcms1
RUNTIME_DEP_PKGS_CSWlibmng1 += CSWlibz1
OBSOLETED_BY_CSWlibmng1 += CSWlibmng

PACKAGES += CSWlibmng-dev
SPKG_DESC_CSWlibmng-dev = Development files for libmng.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibmng-dev += CSWlibmng1

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-jpeg
CONFIGURE_ARGS += --with-zlib

include gar/category.mk

pre-configure:
	cd $(WORKSRC) && cp makefiles/Makefile.am .
	cd $(WORKSRC) && cp makefiles/configure.in .
	cd $(WORKSRC) && cp doc/makefiles/Makefile.am doc
	cd $(WORKSRC) && cp doc/man/makefiles/Makefile.am doc/man
	cd $(WORKSRC) && bash unmaintained/autogen.sh
	@$(MAKECOOKIE)
