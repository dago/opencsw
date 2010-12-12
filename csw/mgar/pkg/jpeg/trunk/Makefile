NAME = jpeg
VERSION = 7
CATEGORIES = lib

DESCRIPTION = JPEG library and tools by the Independent JPEG Group
define BLURB
  Long description
endef

MASTER_SITES = http://www.ijg.org/files/
DISTFILES  = $(NAME)src.v$(VERSION).tar.gz

PACKAGES = CSWjpeg CSWjpegrt CSWjpegdevel
CATALOGNAME_CSWjpeg = jpeg
CATALOGNAME_CSWjpegrt = jpeg_rt
CATALOGNAME_CSWjpegdevel = jpeg_devel

SPKG_DESC_CSWjpeg += JPEG library and tools by the Independent JPEG Group
SPKG_DESC_CSWjpegrt += JPEG library and tools by the Independent JPEG Group - runtime package
SPKG_DESC_CSWjpegdevel += JPEG library and tools by the Independent JPEG Group - developer pa ckage

RUNTIME_DEP_PKGS_CSWjpeg += CSWjpegrt 
RUNTIME_DEP_PKGS_CSWjpegrt += 
RUNTIME_DEP_PKGS_CSWjpegdevel += CSWjpegrt

PKGFILES_CSWjpegrt = $(PKGFILES_RT)
PKGFILES_CSWjpegdevel = $(PKGFILES_DEVEL)

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.ijg.org

BUILD64 = 1

STRIP_LIBTOOL = 1

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

include gar/category.mk
