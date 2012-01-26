NAME = libfpx
VERSION = 1.3.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = FlashPIX library
define BLURB
endef

MASTER_SITES = ftp://ftp.imagemagick.org/pub/ImageMagick/delegates/
DISTFILES  = $(DISTNAME).tar.xz

PATCHFILES += olecomm.h.patch
# PATCHFILES += tchar.patch

# PATCHFILES += 0001-Force-one-signature-for-CExposedDocFile-RenameElemen.patch

PATCHFILES += 0002-Fix-unresolved-symbols-part-1.patch
PATCHFILES += 0003-Fix-unresolved-symbols-part-2.patch

VENDOR_URL = http://www.imagemagick.org
LICENSE = flashpix.h

PACKAGES += CSWlibfpx1
SPKG_DESC_CSWlibfpx1 = FlashPIX library, libfpx.so.1
PKGFILES_CSWlibfpx1 += $(call pkgfiles_lib,libfpx.so.1)
OBSOLETED_BY_CSWlibfpx1 += CSWlibfpx

PACKAGES += CSWlibfpx-dev
SPKG_DESC_CSWlibfpx-dev = Development files for libfpx.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibfpx-dev += CSWlibfpx1
OBSOLETED_BY_CSWlibfpx-dev += CSWlibfpxdevel
CATALOGNAME_CSWlibfpxdevel = libfpx_devel_stub

DOCFILES += AUTHORS
DOCFILES += ChangeLog
DOCFILES += NEWS
DOCFILES += README

# Fix for problem introduced between 12101[7-8]-17 and 12101[7-8]-20
EXTRA_CPPFLAGS += -D_RWSTD_NO_WSTR=1

COMPILERLIBS-sparc-32 = /opt/SUNWspro/lib
COMPILERLIBS-sparc-64 = /opt/SUNWspro/lib/v9
COMPILERLIBS-i386-32 = /opt/SUNWspro/lib
COMPILERLIBS-i386-64 = /opt/SUNWspro/lib/amd64

# Make sure to include path or we link against libCrun.a
EXTRA_LINKER_FLAGS += -L$(COMPILERLIBS-$(GARCH)-$(MEMORYMODEL)) -lCrun -lCstd

# For sqrt, atan2, pow
EXTRA_LINKER_FLAGS += -lm

BUILD64_LIBS_ONLY = 1

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(docdir)/libfpx_dev
	cd $(WORKSRC) && ginstall -m 0644 $(DOCFILES) $(DESTDIR)$(docdir)/libfpx_dev
	@$(MAKECOOKIE)
