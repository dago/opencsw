NAME = libgnomeui
VERSION = 2.24.3
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = The main GNOME 2 UI library
define BLURB
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

SPKG_SOURCEURL = http://live.gnome.org/libgnomeui

LICENSE = COPYING.LIB

PACKAGES += CSWlibgnomeui
PACKAGES += CSWlibgnomeui2-0
PACKAGES += CSWlibgnomeui-devel
PACKAGES += CSWlibgnomeui-doc

CATALOGNAME_CSWlibgnomeui = libgnomeui
CATALOGNAME_CSWlibgnomeui2-0 = libgnomeui2_0
CATALOGNAME_CSWlibgnomeui-devel = libgnomeui_devel
CATALOGNAME_CSWlibgnomeui-doc = libgnomeui_doc

SPKG_DESC_CSWlibgnomeui = Transitional package as contents moved to CSWlibgnomeui2-0
SPKG_DESC_CSWlibgnomeui2-0 = $(DESCRIPTION) providing libgnomeui-2.so.0
SPKG_DESC_CSWlibgnomeui-devel += $(DESCRIPTION) - developer package
SPKG_DESC_CSWlibgnomeui-doc += $(DESCRIPTION) - documentation

BUILD_DEP_PKGS += CSWgnomeicontheme
BUILD_DEP_PKGS += CSWlibgnome
BUILD_DEP_PKGS += CSWlibgnomecanvas
BUILD_DEP_PKGS += CSWgtk2devel

RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibpopt
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgnome
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgnomecanvas
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibatk
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWorbit2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWgconf2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWbonobo2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibbonoboui
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWgnomekeyring
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWpango
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWglib2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibart
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibglade2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibcairo

RUNTIME_DEP_PKGS_CSWlibgnomeui-devel = CSWlibgnomeui2-0

# Legacy package dependencies, remove after deprecation
RUNTIME_DEP_PKGS_CSWlibgnomeui = CSWlibgnomeui2-0 CSWlibgnomeui-devel CSWlibgnomeui-doc
CHECKPKG_OVERRIDES_CSWlibgnomeui += surplus-dependency|CSWlibgnomeui-devel
CHECKPKG_OVERRIDES_CSWlibgnomeui += surplus-dependency|CSWlibgnomeui-doc
CHECKPKG_OVERRIDES_CSWlibgnomeui += surplus-dependency|CSWlibgnomeui2-0

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_LDFLAGS = -lm

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc

ARCHALL_CSWlibgnomeui = 1
ARCHALL_CSWlibgnomeui-doc = 1

PKGFILES_CSWlibgnomeui = NOFILES
PKGFILES_CSWlibgnomeui-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibgnomeui-doc = $(sharedstatedir)/gtk-doc/.*

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
