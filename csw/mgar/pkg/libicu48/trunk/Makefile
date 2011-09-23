# $Id$
NAME = libicu
VERSION = 4.8.1
CATEGORIES = lib

DESCRIPTION = International Components for Unicode
define BLURB
endef

MASTER_SITES = http://download.icu-project.org/files/icu4c/$(VERSION)/
SOURCEFILES = icu4c-$(subst .,_,$(VERSION))-src.tgz
DISTFILES = $(SOURCEFILES)

VENDOR_URL = http://icu-project.org/

LICENSE = license.html

PACKAGES += CSWlibicudata48
SPKG_DESC_CSWlibicudata48 = International Components for Unicode, libicudata.so.48
PKGFILES_CSWlibicudata48 += $(call pkgfiles_lib,libicudata.so.48)

PACKAGES += CSWlibicui18n48
SPKG_DESC_CSWlibicui18n48 = International Components for Unicode, libicui18n.so.48
PKGFILES_CSWlibicui18n48 += $(call pkgfiles_lib,libicui18n.so.48)
RUNTIME_DEP_PKGS_CSWlibicui18n48 += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWlibicui18n48 += CSWlibicudata48

PACKAGES += CSWlibicuio48
SPKG_DESC_CSWlibicuio48 = International Components for Unicode, libicuio.so.48
PKGFILES_CSWlibicuio48 += $(call pkgfiles_lib,libicuio.so.48)
RUNTIME_DEP_PKGS_CSWlibicuio48 += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibicuio48 += CSWlibicui18n
RUNTIME_DEP_PKGS_CSWlibicuio48 += CSWlibicuuc48

PACKAGES += CSWlibicule48
SPKG_DESC_CSWlibicule48 = International Components for Unicode, libicule.so.48
PKGFILES_CSWlibicule48 += $(call pkgfiles_lib,libicule.so.48)
RUNTIME_DEP_PKGS_CSWlibicule48 += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWlibicule48 += CSWlibicudata48

PACKAGES += CSWlibiculx48
SPKG_DESC_CSWlibiculx48 = International Components for Unicode, libiculx.so.48
PKGFILES_CSWlibiculx48 += $(call pkgfiles_lib,libiculx.so.48)
RUNTIME_DEP_PKGS_CSWlibiculx48 += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWlibiculx48 += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibiculx48 += CSWlibicule48

PACKAGES += CSWlibicutest48
SPKG_DESC_CSWlibicutest48 = International Components for Unicode, libicutest.so.48
PKGFILES_CSWlibicutest48 += $(call pkgfiles_lib,libicutest.so.48)
RUNTIME_DEP_PKGS_CSWlibicutest48 += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibicutest48 += CSWlibicui18n
RUNTIME_DEP_PKGS_CSWlibicutest48 += CSWlibicutu48
RUNTIME_DEP_PKGS_CSWlibicutest48 += CSWlibicuuc48

PACKAGES += CSWlibicutu48
SPKG_DESC_CSWlibicutu48 = International Components for Unicode, libicutu.so.48
PKGFILES_CSWlibicutu48 += $(call pkgfiles_lib,libicutu.so.48)
RUNTIME_DEP_PKGS_CSWlibicutu48 += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWlibicutu48 += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibicutu48 += CSWlibicui18n

PACKAGES += CSWlibicuuc48
SPKG_DESC_CSWlibicuuc48 = International Components for Unicode, libicuuc.so.48
PKGFILES_CSWlibicuuc48 += $(call pkgfiles_lib,libicuuc.so.48)
RUNTIME_DEP_PKGS_CSWlibicuuc48 += CSWlibicudata48

PACKAGES += CSWlibicu-dev
SPKG_DESC_CSWlibicu-dev = Development files for libicu.so.48
# This package is PKGFILES catchall
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicui18n
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuio48
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicule48
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibiculx48
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutest48
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutu48
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuuc48
OBSOLETED_BY_CSWlibicu-dev += CSWlibicu-devel

DISTNAME = icu
WORKSRC = $(WORKDIR)/$(DISTNAME)/source

# Using -I/opt/csw/include here puts it before the include of the newly built
# software which breaks definitions, so make sure it is empty.
CPPFLAGS = 

# libCrun is needed for all libs, libCstd for libicui18n.so only
# Not having these does not cause errors during build of libicu, but the
# packages using the libs will bail out as they assume the libs are self-contained.
LINKER_FLAGS = -lCrun -lCstd -norunpath

BUILD64 = 1
NOISALIST = 1

include gar/category.mk

post-extract-modulated:
	-perl -pi -e 's,/usr/local,$(prefix),' \
		$(WORKSRC)/source/config/icu-config-bottom
