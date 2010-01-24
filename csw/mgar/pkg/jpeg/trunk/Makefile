GARNAME = jpeg
GARVERSION = 7
CATEGORIES = lib

DESCRIPTION = JPEG library and tools by the Independent JPEG Group
define BLURB
  Long description
endef

MASTER_SITES = http://www.ijg.org/files/
DISTFILES  = $(GARNAME)src.v$(GARVERSION).tar.gz

PACKAGES = CSWjpeg CSWjpegrt CSWjpegdevel
CATALOGNAME_CSWjpeg = jpeg
CATALOGNAME_CSWjpegrt = jpeg_rt
CATALOGNAME_CSWjpegdevel = jpeg_devel

SPKG_DESC_CSWjpeg += JPEG library and tools by the Independent JPEG Group
SPKG_DESC_CSWjpegrt += JPEG library and tools by the Independent JPEG Group - runtime package
SPKG_DESC_CSWjpegdevel += JPEG library and tools by the Independent JPEG Group - developer pa ckage

REQUIRED_PKGS_CSWjpeg += CSWjpegrt 
REQUIRED_PKGS_CSWjpegrt += 
REQUIRED_PKGS_CSWjpegdevel += CSWjpegrt

PKGFILES_CSWjpegrt = $(PKGFILES_RT)
PKGFILES_CSWjpegdevel = $(PKGFILES_DEVEL)

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.ijg.org

BUILD64 = 1

STRIP_LIBTOOL = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

include gar/category.mk
