# $Id$
NAME = libicu
VERSION = 49.1.2
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

PACKAGES += CSWlibicudata49
SPKG_DESC_CSWlibicudata49 = International Components for Unicode, libicudata.so.49
PKGFILES_CSWlibicudata49 += $(call pkgfiles_lib,libicudata.so.49)

PACKAGES += CSWlibicui18n49
SPKG_DESC_CSWlibicui18n49 = International Components for Unicode, libicui18n.so.49
PKGFILES_CSWlibicui18n49 += $(call pkgfiles_lib,libicui18n.so.49)
RUNTIME_DEP_PKGS_CSWlibicui18n49 += CSWlibicuuc49
RUNTIME_DEP_PKGS_CSWlibicui18n49 += CSWlibicudata49

PACKAGES += CSWlibicuio49
SPKG_DESC_CSWlibicuio49 = International Components for Unicode, libicuio.so.49
PKGFILES_CSWlibicuio49 += $(call pkgfiles_lib,libicuio.so.49)
RUNTIME_DEP_PKGS_CSWlibicuio49 += CSWlibicudata49
RUNTIME_DEP_PKGS_CSWlibicuio49 += CSWlibicui18n49
RUNTIME_DEP_PKGS_CSWlibicuio49 += CSWlibicuuc49

PACKAGES += CSWlibicule49
SPKG_DESC_CSWlibicule49 = International Components for Unicode, libicule.so.49
PKGFILES_CSWlibicule49 += $(call pkgfiles_lib,libicule.so.49)
RUNTIME_DEP_PKGS_CSWlibicule49 += CSWlibicuuc49
RUNTIME_DEP_PKGS_CSWlibicule49 += CSWlibicudata49

PACKAGES += CSWlibiculx49
SPKG_DESC_CSWlibiculx49 = International Components for Unicode, libiculx.so.49
PKGFILES_CSWlibiculx49 += $(call pkgfiles_lib,libiculx.so.49)
RUNTIME_DEP_PKGS_CSWlibiculx49 += CSWlibicuuc49
RUNTIME_DEP_PKGS_CSWlibiculx49 += CSWlibicudata49
RUNTIME_DEP_PKGS_CSWlibiculx49 += CSWlibicule49

PACKAGES += CSWlibicutest49
SPKG_DESC_CSWlibicutest49 = International Components for Unicode, libicutest.so.49
PKGFILES_CSWlibicutest49 += $(call pkgfiles_lib,libicutest.so.49)
RUNTIME_DEP_PKGS_CSWlibicutest49 += CSWlibicudata49
RUNTIME_DEP_PKGS_CSWlibicutest49 += CSWlibicui18n49
RUNTIME_DEP_PKGS_CSWlibicutest49 += CSWlibicutu49
RUNTIME_DEP_PKGS_CSWlibicutest49 += CSWlibicuuc49

PACKAGES += CSWlibicutu49
SPKG_DESC_CSWlibicutu49 = International Components for Unicode, libicutu.so.49
PKGFILES_CSWlibicutu49 += $(call pkgfiles_lib,libicutu.so.49)
RUNTIME_DEP_PKGS_CSWlibicutu49 += CSWlibicuuc49
RUNTIME_DEP_PKGS_CSWlibicutu49 += CSWlibicudata49
RUNTIME_DEP_PKGS_CSWlibicutu49 += CSWlibicui18n49

PACKAGES += CSWlibicuuc49
SPKG_DESC_CSWlibicuuc49 = International Components for Unicode, libicuuc.so.49
PKGFILES_CSWlibicuuc49 += $(call pkgfiles_lib,libicuuc.so.49)
RUNTIME_DEP_PKGS_CSWlibicuuc49 += CSWlibicudata49

PACKAGES += CSWlibicu-dev
SPKG_DESC_CSWlibicu-dev = Development files for libicu.so.49
# This package is PKGFILES catchall
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicudata49
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicui18n49
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuio49
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicule49
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibiculx49
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutest49
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutu49
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuuc49
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

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

include gar/category.mk

post-extract-modulated:
	-perl -pi -e 's,/usr/local,$(prefix),' \
		$(WORKSRC)/config/icu-config-bottom
