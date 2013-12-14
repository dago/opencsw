# $Id$
NAME = libicu
VERSION = 52.1
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

PACKAGES52
SPKG_DESC_CSWlibicudata52 = International Components for Unicode, libicudata.so.52
PKGFILES_CSWlibicudata52 += $(call pkgfiles_lib,libicudata.so.52)

PACKAGES += CSWlibicui18n52
SPKG_DESC_CSWlibicui18n52 = International Components for Unicode, libicui18n.so.52
PKGFILES_CSWlibicui18n52 += $(call pkgfiles_lib,libicui18n.so.52)
RUNTIME_DEP_PKGS_CSWlibicui18n52 += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibicui18n52 += CSWlibicudata52

PACKAGES += CSWlibicuio52
SPKG_DESC_CSWlibicuio52 = International Components for Unicode, libicuio.so.52
PKGFILES_CSWlibicuio52 += $(call pkgfiles_lib,libicuio.so.52)
RUNTIME_DEP_PKGS_CSWlibicuio52 += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibicuio52 += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibicuio52 += CSWlibicudata52

PACKAGES += CSWlibicule52
SPKG_DESC_CSWlibicule52 = International Components for Unicode, libicule.so.52
PKGFILES_CSWlibicule52 += $(call pkgfiles_lib,libicule.so.52)
RUNTIME_DEP_PKGS_CSWlibicule52 += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibicule52 += CSWlibicudata52

PACKAGES += CSWlibiculx52
SPKG_DESC_CSWlibiculx52 = International Components for Unicode, libiculx.so.52
PKGFILES_CSWlibiculx52 += $(call pkgfiles_lib,libiculx.so.52)
RUNTIME_DEP_PKGS_CSWlibiculx52 += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibiculx52 += CSWlibicule52
RUNTIME_DEP_PKGS_CSWlibiculx52 += CSWlibicudata52

PACKAGES += CSWlibicutest52
SPKG_DESC_CSWlibicutest52 = International Components for Unicode, libicutest.so.52
PKGFILES_CSWlibicutest52 += $(call pkgfiles_lib,libicutest.so.52)
RUNTIME_DEP_PKGS_CSWlibicutest52 += CSWlibicutu52
RUNTIME_DEP_PKGS_CSWlibicutest52 += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibicutest52 += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibicutest52 += CSWlibicudata52

PACKAGES += CSWlibicutu52
SPKG_DESC_CSWlibicutu52 = International Components for Unicode, libicutu.so.52
PKGFILES_CSWlibicutu52 += $(call pkgfiles_lib,libicutu.so.52)
RUNTIME_DEP_PKGS_CSWlibicutu52 += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibicutu52 += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibicutu52 += CSWlibicudata52

PACKAGES += CSWlibicuuc52
SPKG_DESC_CSWlibicuuc52 = International Components for Unicode, libicuuc.so.52
PKGFILES_CSWlibicuuc52 += $(call pkgfiles_lib,libicuuc.so.52)
RUNTIME_DEP_PKGS_CSWlibicuuc52 += CSWlibicudata52

# This is the presence of /usr/share/lib/zoneinfo which is ok
CHECKPKG_OVERRIDES_CSWlibicuuc52 += file-with-bad-content|/usr/share|root/opt/csw/lib/libicuuc.so.52.1
CHECKPKG_OVERRIDES_CSWlibicuuc52 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libicuuc.so.52.1
CHECKPKG_OVERRIDES_CSWlibicuuc52 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libicuuc.so.52.1

PACKAGES += CSWlibicu-dev
SPKG_DESC_CSWlibicu-dev = Development files for libicu.so.52
# This package is PKGFILES catchall
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicudata52
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuio52
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicule52
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibiculx52
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutest52
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutu52
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuuc52

# For i386 due to different linker settings
CHECKPKG_OVERRIDES_CSWlibicule52 += surplus-dependency|CSWlibicudata52
CHECKPKG_OVERRIDES_CSWlibicutu52 += surplus-dependency|CSWlibicudata52
CHECKPKG_OVERRIDES_CSWlibiculx52 += surplus-dependency|CSWlibicudata52
CHECKPKG_OVERRIDES_CSWlibicuio52 += surplus-dependency|CSWlibicudata52
CHECKPKG_OVERRIDES_CSWlibicutest52 += surplus-dependency|CSWlibicudata52
CHECKPKG_OVERRIDES_CSWlibicutest52 += surplus-dependency|CSWlibicui18n52
CHECKPKG_OVERRIDES_CSWlibicui18n52 += surplus-dependency|CSWlibicudata52

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

