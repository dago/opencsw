NAME = fltk
VERSION = 1.1.10
CATEGORIES = lib

DESCRIPTION = Fast light Tool Kit
define BLURB
  FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit for UNIX®/Linux® (X11), Microsoft® Windows®, and MacOS® X. FLTK provides modern GUI functionality without the bloat and supports 3D graphics via OpenGL® and its built-in GLUT emulation.
endef

MASTER_SITES = http://ftp.easysw.com/pub/fltk/$(VERSION)/

DISTFILES  = $(NAME)-$(VERSION)-source.tar.gz
PATCHFILES = makeinclude.in.diff Makefile.diff

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.fltk.org/

DEP_PKGS = CSWzlib CSWjpeg CSWpng

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --mandir=/opt/csw/share/man
CONFIGURE_ARGS += --disable-localpng
CONFIGURE_ARGS += --disable-localjpeg
CONFIGURE_ARGS += --disable-localzlib
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-largefile
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-shared 

EXTRA_BUILD_EXPORTS = libdir

CHECKPKG_OVERRIDES_CSWfltk += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libfltk.so.1.1
CHECKPKG_OVERRIDES_CSWfltk += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libfltk_forms.so.1.1
CHECKPKG_OVERRIDES_CSWfltk += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libfltk_images.so.1.1

include gar/category.mk
