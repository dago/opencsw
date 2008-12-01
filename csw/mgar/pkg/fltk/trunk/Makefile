GARNAME = fltk
GARVERSION = 1.1.7
CATEGORIES = lib

DESCRIPTION = Fast light Tool Kit
define BLURB
  FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit for UNIX®/Linux® (X11), Microsoft® Windows®, and MacOS® X. FLTK provides modern GUI functionality without the bloat and supports 3D graphics via OpenGL® and its built-in GLUT emulation.
endef

MASTER_SITES = http://ftp.easysw.com/pub/fltk/1.1.7/
UPSTREAM_MASTER_SITES = http://ftp.easysw.com/pub/fltk/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWfltk,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES = makeincludes.diff

CONFIGURE_ARGS = $(DIRPATHS) --mandir=/opt/csw/share/man --disable-localpng --disable-localjpeg --disable-localzlib --enable-shared

include gar/category.mk
