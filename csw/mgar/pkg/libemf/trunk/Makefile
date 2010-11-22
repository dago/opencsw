# $Id$
GARNAME = libemf
GARVERSION = 1.0.4
CATEGORIES = lib

DESCRIPTION = Library implementation of ECMA-234 API for the generation of enhanced metafiles
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTNAME = libEMF-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES  = 0001-Add-__sparc-and-__i386-in-addition-to-__-__.patch
PATCHFILES += 0002-Remove-unneeded-definition-causing-link-errors.patch
PATCHFILES += 0003-Always-use-csw-libtool.patch
PATCHFILES += 0004-Do-not-use-link-against-libstdc.patch

VENDOR_URL = http://libemf.sourceforge.net/

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# *We* can do 64 bit, but the tests dump core in CSWglib2 2.23.5,REV=2010.03.09
# Re-enable when glib2 gets refreshed.
# BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

