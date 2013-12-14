# $Id$
NAME = libicu
VERSION = 51.2
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

PACKAGES51
SPKG_DESC_CSWlibicudata51 = International Components for Unicode, libicudata.so.51
PKGFILES_CSWlibicudata51 += $(call pkgfiles_lib,libicudata.so.51)

PACKAGES += CSWlibicui18n51
SPKG_DESC_CSWlibicui18n51 = International Components for Unicode, libicui18n.so.51
PKGFILES_CSWlibicui18n51 += $(call pkgfiles_lib,libicui18n.so.51)
RUNTIME_DEP_PKGS_CSWlibicui18n51 += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWlibicui18n51 += CSWlibicudata51

PACKAGES += CSWlibicuio51
SPKG_DESC_CSWlibicuio51 = International Components for Unicode, libicuio.so.51
PKGFILES_CSWlibicuio51 += $(call pkgfiles_lib,libicuio.so.51)
RUNTIME_DEP_PKGS_CSWlibicuio51 += CSWlibicui18n51
RUNTIME_DEP_PKGS_CSWlibicuio51 += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWlibicuio51 += CSWlibicudata51

PACKAGES += CSWlibicule51
SPKG_DESC_CSWlibicule51 = International Components for Unicode, libicule.so.51
PKGFILES_CSWlibicule51 += $(call pkgfiles_lib,libicule.so.51)
RUNTIME_DEP_PKGS_CSWlibicule51 += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWlibicule51 += CSWlibicudata51

PACKAGES += CSWlibiculx51
SPKG_DESC_CSWlibiculx51 = International Components for Unicode, libiculx.so.51
PKGFILES_CSWlibiculx51 += $(call pkgfiles_lib,libiculx.so.51)
RUNTIME_DEP_PKGS_CSWlibiculx51 += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWlibiculx51 += CSWlibicule51
RUNTIME_DEP_PKGS_CSWlibiculx51 += CSWlibicudata51

PACKAGES += CSWlibicutest51
SPKG_DESC_CSWlibicutest51 = International Components for Unicode, libicutest.so.51
PKGFILES_CSWlibicutest51 += $(call pkgfiles_lib,libicutest.so.51)
RUNTIME_DEP_PKGS_CSWlibicutest51 += CSWlibicutu51
RUNTIME_DEP_PKGS_CSWlibicutest51 += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWlibicutest51 += CSWlibicui18n51
RUNTIME_DEP_PKGS_CSWlibicutest51 += CSWlibicudata51

PACKAGES += CSWlibicutu51
SPKG_DESC_CSWlibicutu51 = International Components for Unicode, libicutu.so.51
PKGFILES_CSWlibicutu51 += $(call pkgfiles_lib,libicutu.so.51)
RUNTIME_DEP_PKGS_CSWlibicutu51 += CSWlibicuuc51
RUNTIME_DEP_PKGS_CSWlibicutu51 += CSWlibicui18n51
RUNTIME_DEP_PKGS_CSWlibicutu51 += CSWlibicudata51

PACKAGES += CSWlibicuuc51
SPKG_DESC_CSWlibicuuc51 = International Components for Unicode, libicuuc.so.51
PKGFILES_CSWlibicuuc51 += $(call pkgfiles_lib,libicuuc.so.51)
RUNTIME_DEP_PKGS_CSWlibicuuc51 += CSWlibicudata51

# This is the presence of /usr/share/lib/zoneinfo which is ok
CHECKPKG_OVERRIDES_CSWlibicuuc51 += file-with-bad-content|/usr/share|root/opt/csw/lib/libicuuc.so.51.2
CHECKPKG_OVERRIDES_CSWlibicuuc51 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libicuuc.so.51.2
CHECKPKG_OVERRIDES_CSWlibicuuc51 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libicuuc.so.51.2

PACKAGES += CSWlibicu-dev
SPKG_DESC_CSWlibicu-dev = Development files for libicu.so.51
# This package is PKGFILES catchall
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicudata51
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicui18n51
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuio51
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicule51
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibiculx51
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutest51
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutu51
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuuc51

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
# Remove Studio-specific arch references
post-install-modulated:
	gsed -i \
		-e '/^[^#]/s/-xO3[^ ]* //' \
		-e '/^[^#]/s/-xarch=[^ ]* //' \
		-e '/^[^#]/s/-xchip=[^ ]* //' \
		-e '/^[^#]/s/-norunpath[^ ]* //' \
		-e '/^[^#]/s/-lCrun[^ ]* //' \
		-e '/^[^#]/s/-lCstd[^ ]* //' \
		$(DESTDIR)$(bindir)/icu-config

