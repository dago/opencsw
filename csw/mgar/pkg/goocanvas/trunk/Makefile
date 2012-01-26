NAME = goocanvas
VERSION = 0.15
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = A cairo-based canvas widget for GTK
define BLURB
	GooCanvas is a canvas widget for GTK that uses the cairo 2D library
	for drawing. 
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWgoocanvas CSWgoocanvasdevel CSWgoocanvasdoc
CATALOGNAME_CSWgoocanvas = goocanvas
CATALOGNAME_CSWgoocanvasdevel = goocanvas_devel
CATALOGNAME_CSWgoocanvasdoc = goocanvas_doc

SPKG_DESC_CSWgoocanvas += A cairo-based canvas widget for GTK
SPKG_DESC_CSWgoocanvasdevel += A cairo-based canvas widget for GTK - developer package
SPKG_DESC_CSWgoocanvasdoc += A cairo-based canvas widget for GTK - documentation

RUNTIME_DEP_PKGS_CSWgoocanvas += CSWfconfig CSWftype2 CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWgoocanvas += CSWgtk2 CSWlibatk CSWlibcairo CSWpango
RUNTIME_DEP_PKGS_CSWgoocanvasdevel += CSWgoocanvas
RUNTIME_DEP_PKGS_CSWgoocanvasdoc += CSWgoocanvas

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/GooCanvas

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

#NOISAEXEC = 1
#NOISALIST = 1
BUILD64 = 1

PKGFILES_CSWgoocanvasdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWgoocanvasdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWgoocanvasdoc = 1

LIBS = -lm
export LIBS

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
