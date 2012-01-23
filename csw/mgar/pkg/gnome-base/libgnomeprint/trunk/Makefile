NAME = libgnomeprint
VERSION = 2.18.6
CATEGORIES = gnome

DESCRIPTION = TODO
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWlibgnomeprint CSWlibgnomeprintdevel CSWlibgnomeprintdoc
CATALOGNAME_CSWlibgnomeprint = libgnomeprint
CATALOGNAME_CSWlibgnomeprintdevel = libgnomeprint_devel
CATALOGNAME_CSWlibgnomeprintdoc = libgnomeprint_doc

SPKG_DESC_CSWlibgnomeprint += $(DESCRIPTION)
SPKG_DESC_CSWlibgnomeprintdevel += $(DESCRIPTION) - developer package
SPKG_DESC_CSWlibgnomeprintdoc += $(DESCRIPTION) - documentation

RUNTIME_DEP_PKGS_CSWlibgnomeprintdevel += CSWlibgnomeprint
RUNTIME_DEP_PKGS_CSWlibgnomeprintdoc += CSWlibgnomeprint

#BUILD_DEP_PKGS += CSWgnomeicontheme
#BUILD_DEP_PKGS += CSWlibgnomeprint
#BUILD_DEP_PKGS += CSWlibgnomecanvas
BUILD_DEP_PKGS += CSWgtk2devel

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://live.gnome.org/libgnomeprint

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_LDFLAGS = -lm
EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

#NOISAEXEC = 1
#NOISALIST = 1
#BUILD64 = 1

PKGFILES_CSWlibgnomeprintdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibgnomeprintdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWlibgnomeprintdoc = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
