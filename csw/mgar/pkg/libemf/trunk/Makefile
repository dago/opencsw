# $Id$
NAME = libemf
VERSION = 1.0.4
CATEGORIES = lib

DESCRIPTION = Library implementation of ECMA-234 API for the generation of enhanced metafiles
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTNAME = libEMF-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES  = 0001-Add-__sparc-and-__i386-in-addition-to-__-__.patch
PATCHFILES += 0002-Remove-unneeded-definition-causing-link-errors.patch
PATCHFILES += 0003-Always-use-csw-libtool.patch
PATCHFILES += 0004-Do-not-use-link-against-libstdc.patch

PACKAGES = CSWlibemf CSWlibemf1 CSWlibemf-devel

CATALOGNAME_CSWlibemf = libemf
CAtALOGNAME_CSWlibemf1 = libemf1
CATALOGNAME_CSWlibemf-devel = libemf_devel

SPKG_DESC_CSWlibemf = $(DESCRIPTION)
SPKG_DESC_CSWlibemf1 = Runtime library for libEMF 1.x
SPKG_DESC_CSWlibemf-devel = Development files for libEMF

RUNTIME_DEP_PKGS_CSWlibemf = CSWlibemf1 CSWlibemf-devel
RUNTIME_DEP_PKGS_CSWlibemf-devel = CSWlibemf1

VENDOR_URL = http://libemf.sourceforge.net/

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# *We* can do 64 bit, but the tests dump core in CSWglib2 2.23.5,REV=2010.03.09
# Re-enable when glib2 gets refreshed.
# BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibemf1 = $(PKGFILES_RT)
PKGFILES_CSWlibemf-devel = $(PKGFILES_DEVEL)

CHECKPKG_OVERRIDES_CSWlibemf += surplus-dependency|CSWlibemf-devel

# This needs a fixed libtool first
CHECKPKG_OVERRIDES_CSWlibemf1 += bad-rpath-entry|/lib|opt/csw/lib/libEMF.so.1.0.0
CHECKPKG_OVERRIDES_CSWlibemf1 += bad-rpath-entry|/opt/SUNWspro/lib|opt/csw/lib/libEMF.so.1.0.0
CHECKPKG_OVERRIDES_CSWlibemf1 += bad-rpath-entry|/opt/SUNWspro/lib/rw7|opt/csw/lib/libEMF.so.1.0.0
CHECKPKG_OVERRIDES_CSWlibemf1 += bad-rpath-entry|/opt/SUNWspro/lib/v8|opt/csw/lib/libEMF.so.1.0.0

include gar/category.mk

