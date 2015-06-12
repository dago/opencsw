# $Id$
NAME = libicu
VERSION = 55.1
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

PACKAGES55
SPKG_DESC_CSWlibicudata55 = International Components for Unicode, libicudata.so.55
PKGFILES_CSWlibicudata55 += $(call pkgfiles_lib,libicudata.so.55)

PACKAGES += CSWlibicui18n55
SPKG_DESC_CSWlibicui18n55 = International Components for Unicode, libicui18n.so.55
PKGFILES_CSWlibicui18n55 += $(call pkgfiles_lib,libicui18n.so.55)
RUNTIME_DEP_PKGS_CSWlibicui18n55 += CSWlibicuuc55
RUNTIME_DEP_PKGS_CSWlibicui18n55 += CSWlibicudata55

PACKAGES += CSWlibicuio55
SPKG_DESC_CSWlibicuio55 = International Components for Unicode, libicuio.so.55
PKGFILES_CSWlibicuio55 += $(call pkgfiles_lib,libicuio.so.55)
RUNTIME_DEP_PKGS_CSWlibicuio55 += CSWlibicui18n55
RUNTIME_DEP_PKGS_CSWlibicuio55 += CSWlibicuuc55
RUNTIME_DEP_PKGS_CSWlibicuio55 += CSWlibicudata55

PACKAGES += CSWlibicule55
SPKG_DESC_CSWlibicule55 = International Components for Unicode, libicule.so.55
PKGFILES_CSWlibicule55 += $(call pkgfiles_lib,libicule.so.55)
RUNTIME_DEP_PKGS_CSWlibicule55 += CSWlibicuuc55
RUNTIME_DEP_PKGS_CSWlibicule55 += CSWlibicudata55

PACKAGES += CSWlibiculx55
SPKG_DESC_CSWlibiculx55 = International Components for Unicode, libiculx.so.55
PKGFILES_CSWlibiculx55 += $(call pkgfiles_lib,libiculx.so.55)
RUNTIME_DEP_PKGS_CSWlibiculx55 += CSWlibicuuc55
RUNTIME_DEP_PKGS_CSWlibiculx55 += CSWlibicule55
RUNTIME_DEP_PKGS_CSWlibiculx55 += CSWlibicudata55

PACKAGES += CSWlibicutest55
SPKG_DESC_CSWlibicutest55 = International Components for Unicode, libicutest.so.55
PKGFILES_CSWlibicutest55 += $(call pkgfiles_lib,libicutest.so.55)
RUNTIME_DEP_PKGS_CSWlibicutest55 += CSWlibicutu55
RUNTIME_DEP_PKGS_CSWlibicutest55 += CSWlibicuuc55
RUNTIME_DEP_PKGS_CSWlibicutest55 += CSWlibicui18n55
RUNTIME_DEP_PKGS_CSWlibicutest55 += CSWlibicudata55

PACKAGES += CSWlibicutu55
SPKG_DESC_CSWlibicutu55 = International Components for Unicode, libicutu.so.55
PKGFILES_CSWlibicutu55 += $(call pkgfiles_lib,libicutu.so.55)
RUNTIME_DEP_PKGS_CSWlibicutu55 += CSWlibicuuc55
RUNTIME_DEP_PKGS_CSWlibicutu55 += CSWlibicui18n55
RUNTIME_DEP_PKGS_CSWlibicutu55 += CSWlibicudata55

PACKAGES += CSWlibicuuc55
SPKG_DESC_CSWlibicuuc55 = International Components for Unicode, libicuuc.so.55
PKGFILES_CSWlibicuuc55 += $(call pkgfiles_lib,libicuuc.so.55)
RUNTIME_DEP_PKGS_CSWlibicuuc55 += CSWlibicudata55

# This is the presence of /usr/share/lib/zoneinfo which is ok
CHECKPKG_OVERRIDES_CSWlibicuuc55 += file-with-bad-content|/usr/share|root/opt/csw/lib/libicuuc.so.55.1
CHECKPKG_OVERRIDES_CSWlibicuuc55 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libicuuc.so.55.1
CHECKPKG_OVERRIDES_CSWlibicuuc55 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libicuuc.so.55.1

PACKAGES += CSWlibicu-dev
SPKG_DESC_CSWlibicu-dev = Development files for libicu.so.55
# This package is PKGFILES catchall
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicudata55
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicui18n55
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuio55
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicule55
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibiculx55
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutest55
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutu55
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuuc55

# This is a false positive. Override until this is fixed:
#   http://lists.opencsw.org/pipermail/maintainers/2015-January/019612.html
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/sparcv9/icu/current/Makefile.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/sparcv9/icu/Makefile.inc|which|needs|the|target|file:|/opt/csw/lib/sparcv9/icu/current/Makefile.inc
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/sparcv9/icu/current/pkgdata.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/sparcv9/icu/pkgdata.inc|which|needs|the|target|file:|/opt/csw/lib/sparcv9/icu/current/pkgdata.inc
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/amd64/icu/current/Makefile.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/amd64/icu/Makefile.inc|which|needs|the|target|file:|/opt/csw/lib/amd64/icu/current/Makefile.inc
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/amd64/icu/current/pkgdata.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/amd64/icu/pkgdata.inc|which|needs|the|target|file:|/opt/csw/lib/amd64/icu/current/pkgdata.inc
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/icu/current/Makefile.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/icu/Makefile.inc|which|needs|the|target|file:|/opt/csw/lib/icu/current/Makefile.inc
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/icu/current/pkgdata.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/icu/pkgdata.inc|which|needs|the|target|file:|/opt/csw/lib/icu/current/pkgdata.inc

# For i386 due to different linker settings
CHECKPKG_OVERRIDES_CSWlibicule55 += surplus-dependency|CSWlibicudata55
CHECKPKG_OVERRIDES_CSWlibicutu55 += surplus-dependency|CSWlibicudata55
CHECKPKG_OVERRIDES_CSWlibiculx55 += surplus-dependency|CSWlibicudata55
CHECKPKG_OVERRIDES_CSWlibicuio55 += surplus-dependency|CSWlibicudata55
CHECKPKG_OVERRIDES_CSWlibicutest55 += surplus-dependency|CSWlibicudata55
CHECKPKG_OVERRIDES_CSWlibicutest55 += surplus-dependency|CSWlibicui18n55
CHECKPKG_OVERRIDES_CSWlibicui18n55 += surplus-dependency|CSWlibicudata55

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

