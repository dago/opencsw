# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = dspam
VERSION = 3.10.2
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

REINPLACE_USRLOCAL += src/config.h

PACKAGES += CSWlibdspam7
CATALOGNAME_CSWlibdspam7 = libdspam7
PKGFILES_CSWlibdspam7 += $(call baseisadirs,$(libdir),libdspam\.so\.7\.0\.0)
PKGFILES_CSWlibdspam7 += $(call baseisadirs,$(libdir),libdspam\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibdspam7 += $(DESCRIPTION), libdspam.so.7
RUNTIME_DEP_PKGS_CSWdspam += CSWlibdspam7

PACKAGES += CSWdspam-dev
CATALOGNAME_CSWdspam-dev = dspam_dev
SPKG_DESC_CSWdspam-dev += $(DESCRIPTION), development files
PKGFILES_CSWdspam-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWdspam-dev += CSWlibdspam7

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-dspam-home=$(localstatedir)/dspam

include gar/category.mk

