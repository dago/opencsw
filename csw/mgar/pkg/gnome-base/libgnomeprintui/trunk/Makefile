NAME = libgnomeprintui
VERSION = 2.18.4
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = TODO
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWlibgnomeprintui CSWlibgnomeprintuidevel CSWlibgnomeprintuidoc
CATALOGNAME_CSWlibgnomeprintui = libgnomeprintui
CATALOGNAME_CSWlibgnomeprintuidevel = libgnomeprintui_devel
CATALOGNAME_CSWlibgnomeprintuidoc = libgnomeprintui_doc

SPKG_DESC_CSWlibgnomeprintui += $(DESCRIPTION)
SPKG_DESC_CSWlibgnomeprintuidevel += $(DESCRIPTION) - developer package
SPKG_DESC_CSWlibgnomeprintuidoc += $(DESCRIPTION) - documentation

RUNTIME_DEP_PKGS_CSWlibgnomeprintuidevel += CSWlibgnomeprintui
RUNTIME_DEP_PKGS_CSWlibgnomeprintuidoc += CSWlibgnomeprintui

BUILD_DEP_PKGS += CSWgnomeicontheme
BUILD_DEP_PKGS += CSWlibgnomeprint
BUILD_DEP_PKGS += CSWlibgnomecanvas
BUILD_DEP_PKGS += CSWgtk2devel

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/libgnomeprintui

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_LDFLAGS = -lm
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

#NOISAEXEC = 1
#NOISALIST = 1
#BUILD64 = 1

PKGFILES_CSWlibgnomeprintuidevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibgnomeprintuidoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWlibgnomeprintuidoc = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
