GARNAME = fltk
GARVERSION = 1.1.9
CATEGORIES = lib

DESCRIPTION = Fast light Tool Kit
define BLURB
  FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit for UNIX®/Linux® (X11), Microsoft® Windows®, and MacOS® X. FLTK provides modern GUI functionality without the bloat and supports 3D graphics via OpenGL® and its built-in GLUT emulation.
endef

MASTER_SITES = http://www.fltk.org/$(GARVERSION)/

DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tar.gz
DISTFILES += $(call admfiles,CSWfltk, prototype)

UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES = makeinclude.in.diff

CONFIGURE_ARGS = $(DIRPATHS) LDFLAGS='-L/opt/csw/lib -L../lib'
CONFIGURE_ARGS += --mandir=/opt/csw/share/man
CONFIGURE_ARGS += --disable-localpng
CONFIGURE_ARGS += --disable-localjpeg
CONFIGURE_ARGS += --disable-localzlib
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-largefile
CONFIGURE_ARGS += --enable-shared 

include gar/category.mk
