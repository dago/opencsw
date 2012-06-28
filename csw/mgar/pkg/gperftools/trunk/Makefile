# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gperftools
VERSION = 2.0
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Fast, multi-threaded malloc() and nifty performance analysis tools

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solarsi10-sparc solarsi10-i386

PACKAGES += CSWmypkg
SPKG_DESC_CSWmypkg = My package
PKGFILES_CSWmypkg += $(call pkgfiles_lib,libabc.so.1)
PKGFILES_CSWmypkg += $(call baseisadirs,$(bindir),myexec)
PKGFILES_CSWmypkg += $(sysconfdir)/myconf

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

