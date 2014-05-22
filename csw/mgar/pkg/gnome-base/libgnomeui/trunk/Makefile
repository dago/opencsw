NAME = libgnomeui
VERSION = 2.24.5
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
PACKAGES += CSWlibgnomeui-dev
PACKAGES += CSWlibgnomeui-doc

CATALOGNAME_CSWlibgnomeui2-0 = libgnomeui2_0
CATALOGNAME_CSWlibgnomeui-dev = libgnomeui_dev
CATALOGNAME_CSWlibgnomeui-doc = libgnomeui_doc

OBSOLETED_BY_CSWlibgnomeui2-0  = CSWlibgnomeui
OBSOLETED_BY_CSWlibgnomeui-dev = CSWlibgnomeui-devel

SPKG_DESC_CSWlibgnomeui2-0 = $(DESCRIPTION) providing libgnomeui-2.so.0
SPKG_DESC_CSWlibgnomeui-dev += $(DESCRIPTION) - developer package
SPKG_DESC_CSWlibgnomeui-doc += $(DESCRIPTION) - documentation

BUILD_DEP_PKGS += CSWlibgnome-dev
BUILD_DEP_PKGS += CSWlibgnomecanvas-dev
BUILD_DEP_PKGS += CSWlibgtk2-dev

RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibart
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibglade2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgconf2-4
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgnome2-0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgnome-keyring0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibbonoboui2-0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgnomecanvas2-0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgnomeui2-0 += CSWlibglib2-0-0

RUNTIME_DEP_PKGS_CSWlibgnomeui-dev = CSWlibgnomeui2-0

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_LDFLAGS = -lm

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no
CONFIGURE_ARGS += --enable-gtk-doc=no
CONFIGURE_ARGS += --enable-gtk-doc-html=no


ARCHALL_CSWlibgnomeui-doc = 1

PKGFILES_CSWlibgnomeui-dev = $(PKGFILES_DEVEL)
PKGFILES_CSWlibgnomeui-doc = $(sharedstatedir)/gtk-doc/.*

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
