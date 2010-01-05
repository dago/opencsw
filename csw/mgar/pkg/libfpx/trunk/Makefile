GARNAME = libfpx
GARVERSION = 1.3.0
GARSUBREV = 1
CATEGORIES = lib

DESCRIPTION = FlashPIX library
define BLURB
endef

MASTER_SITES = ftp://ftp.imagemagick.org/pub/ImageMagick/delegates/
DISTFILES  = $(GARNAME)-$(GARVERSION)-$(GARSUBREV).tar.bz2

#PACKAGES = CSWlibfpx CSWlibfpxdevel CSWlibfpxdoc
PACKAGES = CSWlibfpx CSWlibfpxdevel
CATALOGNAME_CSWlibfpx = libfpx
CATALOGNAME_CSWlibfpxdevel = libfpx_devel
#CATALOGNAME_CSWlibfpxdoc = libfpx_doc

SPKG_DESC_CSWlibfpx += FlashPIX library
SPKG_DESC_CSWlibfpxdevel += FlashPIX library - developer package
#SPKG_DESC_CSWlibfpxdoc += FlashPIX library - documentation

REQUIRED_PKGS_CSWlibfpx +=
REQUIRED_PKGS_CSWlibfpxdevel += CSWlibfpx
#REQUIRED_PKGS_CSWlibfpxdoc += CSWlibfpx

PKGFILES_CSWlibfpxdevel = $(PKGFILES_DEVEL)
#PKGFILES_CSWlibfpxdoc = $(sharedstatedir)/doc/.*

#ARCHALL_CSWlibfpxdoc = 1

SPKG_SOURCEURL = http://www.imagemagick.org

PATCHFILES = olecomm.h.patch
#PATCHFILES += tchar.patch

LICENSE = flashpix.h

DOCFILES = AUTHORS ChangeLog NEWS README

UFILES_REGEX = $(GARNAME)-((\d+(?:\.\d+)*)-(\d+)?).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)

STRIP_LIBTOOL=1

TEST_TARGET = check

BUILD64 = 1

# libfpx have some problems with rw/trait
GARCOMPILER = GCC4

include gar/category.mk
