# $Id$
NAME = libicu
VERSION = 54.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = International Components for Unicode
define BLURB
endef

MASTER_SITES = http://download.icu-project.org/files/icu4c/$(VERSION)/
SOURCEFILES = icu4c-$(subst .,_,$(VERSION))-src.tgz
DISTFILES = $(SOURCEFILES)

VENDOR_URL = http://icu-project.org/

LICENSE#solaris 9 specific patch for missing PTR_MAX
PATCHFILES_5.9 += LETypes_ptr_sol9.patch

PATCHFILES += $(PATCHFILES_$(GAROSREL))SE = license.html

PACKAGES54
SPKG_DESC_CSWlibicudata54 = International Components for Unicode, libicudata.so.54
PKGFILES_CSWlibicudata54 += $(call pkgfiles_lib,libicudata.so.54)

PACKAGES += CSWlibicui18n54
SPKG_DESC_CSWlibicui18n54 = International Components for Unicode, libicui18n.so.54
PKGFILES_CSWlibicui18n54 += $(call pkgfiles_lib,libicui18n.so.54)
RUNTIME_DEP_PKGS_CSWlibicui18n54 += CSWlibicuuc54
RUNTIME_DEP_PKGS_CSWlibicui18n54 += CSWlibicudata54

PACKAGES += CSWlibicuio54
SPKG_DESC_CSWlibicuio54 = International Components for Unicode, libicuio.so.54
PKGFILES_CSWlibicuio54 += $(call pkgfiles_lib,libicuio.so.54)
RUNTIME_DEP_PKGS_CSWlibicuio54 += CSWlibicui18n54
RUNTIME_DEP_PKGS_CSWlibicuio54 += CSWlibicuuc54
RUNTIME_DEP_PKGS_CSWlibicuio54 += CSWlibicudata54

PACKAGES += CSWlibicule54
SPKG_DESC_CSWlibicule54 = International Components for Unicode, libicule.so.54
PKGFILES_CSWlibicule54 += $(call pkgfiles_lib,libicule.so.54)
RUNTIME_DEP_PKGS_CSWlibicule54 += CSWlibicuuc54
RUNTIME_DEP_PKGS_CSWlibicule54 += CSWlibicudata54

PACKAGES += CSWlibiculx54
SPKG_DESC_CSWlibiculx54 = International Components for Unicode, libiculx.so.54
PKGFILES_CSWlibiculx54 += $(call pkgfiles_lib,libiculx.so.54)
RUNTIME_DEP_PKGS_CSWlibiculx54 += CSWlibicuuc54
RUNTIME_DEP_PKGS_CSWlibiculx54 += CSWlibicule54
RUNTIME_DEP_PKGS_CSWlibiculx54 += CSWlibicudata54

PACKAGES += CSWlibicutest54
SPKG_DESC_CSWlibicutest54 = International Components for Unicode, libicutest.so.54
PKGFILES_CSWlibicutest54 += $(call pkgfiles_lib,libicutest.so.54)
RUNTIME_DEP_PKGS_CSWlibicutest54 += CSWlibicutu54
RUNTIME_DEP_PKGS_CSWlibicutest54 += CSWlibicuuc54
RUNTIME_DEP_PKGS_CSWlibicutest54 += CSWlibicui18n54
RUNTIME_DEP_PKGS_CSWlibicutest54 += CSWlibicudata54

PACKAGES += CSWlibicutu54
SPKG_DESC_CSWlibicutu54 = International Components for Unicode, libicutu.so.54
PKGFILES_CSWlibicutu54 += $(call pkgfiles_lib,libicutu.so.54)
RUNTIME_DEP_PKGS_CSWlibicutu54 += CSWlibicuuc54
RUNTIME_DEP_PKGS_CSWlibicutu54 += CSWlibicui18n54
RUNTIME_DEP_PKGS_CSWlibicutu54 += CSWlibicudata54

PACKAGES += CSWlibicuuc54
SPKG_DESC_CSWlibicuuc54 = International Components for Unicode, libicuuc.so.54
PKGFILES_CSWlibicuuc54 += $(call pkgfiles_lib,libicuuc.so.54)
RUNTIME_DEP_PKGS_CSWlibicuuc54 += CSWlibicudata54

# This is the presence of /usr/share/lib/zoneinfo which is ok
CHECKPKG_OVERRIDES_CSWlibicuuc54 += file-with-bad-content|/usr/share|root/opt/csw/lib/libicuuc.so.54.1
CHECKPKG_OVERRIDES_CSWlibicuuc54 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/libicuuc.so.54.1
CHECKPKG_OVERRIDES_CSWlibicuuc54 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/libicuuc.so.54.1

PACKAGES += CSWlibicu-dev
SPKG_DESC_CSWlibicu-dev = Development files for libicu.so.54
# This package is PKGFILES catchall
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicudata54
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicui18n54
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuio54
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicule54
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibiculx54
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutest54
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicutu54
RUNTIME_DEP_PKGS_CSWlibicu-dev += CSWlibicuuc54

# This is a false positive. Override until this is fixed:
#   http://lists.opencsw.org/pipermail/maintainers/2015-January/019612.html
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/sparcv9/icu/current/Makefile.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/sparcv9/icu/Makefile.inc|which|needs|the|target|file:|/opt/csw/lib/sparcv9/icu/current/Makefile.inc
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/sparcv9/icu/current/pkgdata.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/sparcv9/icu/pkgdata.inc|which|needs|the|target|file:|/opt/csw/lib/sparcv9/icu/current/pkgdata.inc
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/amd64/icu/current/Makefile.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/amd64/icu/Makefile.inc|which|needs|the|target|file:|/opt/csw/lib/amd64/icu/current/Makefile.inc
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/amd64/icu/current/pkgdata.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/amd64/icu/pkgdata.inc|which|needs|the|target|file:|/opt/csw/lib/amd64/icu/current/pkgdata.inc
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/icu/current/Makefile.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/icu/Makefile.inc|which|needs|the|target|file:|/opt/csw/lib/icu/current/Makefile.inc
CHECKPKG_OVERRIDES_CSWlibicu-dev += file-needed-but-no-package-satisfies-it|/opt/csw/lib/icu/current/pkgdata.inc|CSWlibicu-dev|contains|symlink|/opt/csw/lib/icu/pkgdata.inc|which|needs|the|target|file:|/opt/csw/lib/icu/current/pkgdata.inc

# For i386 due to different linker settings
CHECKPKG_OVERRIDES_CSWlibicule54 += surplus-dependency|CSWlibicudata54
CHECKPKG_OVERRIDES_CSWlibicutu54 += surplus-dependency|CSWlibicudata54
CHECKPKG_OVERRIDES_CSWlibiculx54 += surplus-dependency|CSWlibicudata54
CHECKPKG_OVERRIDES_CSWlibicuio54 += surplus-dependency|CSWlibicudata54
CHECKPKG_OVERRIDES_CSWlibicutest54 += surplus-dependency|CSWlibicudata54
CHECKPKG_OVERRIDES_CSWlibicutest54 += surplus-dependency|CSWlibicui18n54
CHECKPKG_OVERRIDES_CSWlibicui18n54 += surplus-dependency|CSWlibicudata54

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

