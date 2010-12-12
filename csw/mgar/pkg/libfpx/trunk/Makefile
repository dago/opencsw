NAME = libfpx
VERSION = 1.3.0
GARSUBREV = 1
CATEGORIES = lib

DESCRIPTION = FlashPIX library
define BLURB
endef

MASTER_SITES = ftp://ftp.imagemagick.org/pub/ImageMagick/delegates/
DISTFILES  = $(NAME)-$(VERSION)-$(GARSUBREV).tar.bz2

PACKAGES = CSWlibfpx CSWlibfpxdevel
CATALOGNAME_CSWlibfpx = libfpx
CATALOGNAME_CSWlibfpxdevel = libfpx_devel

SPKG_DESC_CSWlibfpx += FlashPIX library
SPKG_DESC_CSWlibfpxdevel += FlashPIX library - developer package

RUNTIME_DEP_PKGS_CSWlibfpx +=
RUNTIME_DEP_PKGS_CSWlibfpxdevel += CSWlibfpx

PKGFILES_CSWlibfpxdevel = $(PKGFILES_DEVEL)

SPKG_SOURCEURL = http://www.imagemagick.org

PATCHFILES = olecomm.h.patch
PATCHFILES += tchar.patch

LICENSE = flashpix.h

DOCFILES = AUTHORS ChangeLog NEWS README

UFILES_REGEX = $(NAME)-((\d+(?:\.\d+)*)-(\d+)?).tar.bz2

# Fix for problem introduced between 12101[7-8]-17 and 12101[7-8]-20
CXXFLAGS += -D_RWSTD_NO_WSTR=1

CONFIGURE_ARGS  = $(DIRPATHS)

STRIP_LIBTOOL=1

TEST_TARGET = check

BUILD64 = 1

include gar/category.mk
