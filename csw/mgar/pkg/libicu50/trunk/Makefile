# $Id$
NAME = libicu
VERSION = 50.1.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = International Components for Unicode
define BLURB
endef

MASTER_SITES = http://download.icu-project.org/files/icu4c/$(VERSION)/
SOURCEFILES = icu4c-$(subst .,_,$(VERSION))-src.tgz
DISTFILES = $(SOURCEFILES)

VENDOR_URL = http://icu-project.org/

LICENSE = license.html

PACKAGES50
SPKG_DESC_CSWlibicudata50 = International Components for Unicode, libicudata.so.50
PKGFILES_CSWlibicudata50 += $(call pkgfiles_lib,libicudata.so.50)

PACKAGES += CSWlibicui18n50
SPKG_DESC_CSWlibicui18n50 = International Components for Unicode, libicui18n.so.50
PKGFILES_CSWlibicui18n50 += $(call pkgfiles_lib,libicui18n.so.50)
RUNTIME_DEP_PKGS_CSWlibicui18n50 += CSWlibicuuc50

PACKAGES += CSWlibicuio50
SPKG_DESC_CSWlibicuio50 = International Components for Unicode, libicuio.so.50
PKGFILES_CSWlibicuio50 += $(call pkgfiles_lib,libicuio.so.50)
RUNTIME_DEP_PKGS_CSWlibicuio50 += CSWlibicui18n50
RUNTIME_DEP_PKGS_CSWlibicuio50 += CSWlibicuuc50

PACKAGES += CSWlibicule50
SPKG_DESC_CSWlibicule50 = International Components for Unicode, libicule.so.50
PKGFILES_CSWlibicule50 += $(call pkgfiles_lib,libicule.so.50)
RUNTIME_DEP_PKGS_CSWlibicule50 += CSWlibicuuc50

PACKAGES += CSWlibiculx50
SPKG_DESC_CSWlibiculx50 = International Components for Unicode, libiculx.so.50
PKGFILES_CSWlibiculx50 += $(call pkgfiles_lib,libiculx.so.50)
RUNTIME_DEP_PKGS_CSWlibiculx50 += CSWlibicuuc50
RUNTIME_DEP_PKGS_CSWlibiculx50 += CSWlibicule50

PACKAGES += CSWlibicutest50
SPKG_DESC_CSWlibicutest50 = International Components for Unicode, libicutest.so.50
PKGFILES_CSWlibicutest50 += $(call pkgfiles_lib,libicutest.so.50)
RUNTIME_DEP_PKGS_CSWlibicutest50 += CSWlibicutu50
RUNTIME_DEP_PKGS_CSWlibicutest50 += CSWlibicuuc50

PACKAGES += CSWlibicutu50
SPKG_DESC_CSWlibicutu50 = International Components for Unicode, libicutu.so.50
PKGFILES_CSWlibicutu50 += $(call pkgfiles_lib,libicutu.so.50)
RUNTIME_DEP_PKGS_CSWlibicutu50 += CSWlibicuuc50
RUNTIME_DEP_PKGS_CSWlibicutu50 += CSWlibicui18n50

PACKAGES += CSWlibicuuc50
SPKG_DESC_CSWlibicuuc50 = International Components for Unicode, libicuuc.so.50
PKGFILES_CSWlibicuuc50 += $(call pkgfiles_lib,libicuuc.so.50)
RUNTIME_DEP_PKGS_CSWlibicuuc50 += CSWlibicudata50= CSWlibicudata49

PACKAGES += CSWlibicu-dev
SPKG_DESC_CSWlibicu-dev = Development fil50
# This package is PKGFILES catchall
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicudata50
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicui18n50
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuio50
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicule50
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibiculx50
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutest50
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutu50
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuuc50

DISTNAME = icu
WORKSRC = $(WORKDIR)/$(DISTNAME)/source

REINPLACE_USRLOCAL += config/icu-config-bottom(DISTNAME)/source

# Using -I/opt/csw/include here puts it before the include of the newly built
# software which breaks definitions, so make sure it is empty.
CPPFLAGS = 

# libCrun is needed for all libs, libCstd for libicui18n.so only
# Not having these does not cause errors during build of libicu, but the
# packages using the libs will bail out as they assume the libs are self-contained.
LINKER_FLAGS = -lCrun -lCstd -norunpath

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

include