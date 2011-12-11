# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gdk-pixbuf
VERSION = 2.24.0
GARTYPE = v2
CATEGORIES = gnome

DESCRIPTION = GNOME tools for pixmap manupulation
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz
DISTFILES += CSWgdkpixbuf-loaders.postinstall

EXPANDVARS = CSWgdkpixbuf-loaders.postinstall

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWgdkpixbuf
SPKG_DESC_CSWgdkpixbuf = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgdkpixbuf  = CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgdk-pixbuf-xlib2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWgdkpixbuf-loaders
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibpng12-0
# I assume if one installs CSWgdkpixbuf, one wants all the stuff
# except -dev
CHECKPKG_OVERRIDES_CSWgdkpixbuf += surplus-dependency|CSWlibgdk-pixbuf-xlib2-0-0
CHECKPKG_OVERRIDES_CSWgdkpixbuf += surplus-dependency|CSWgdkpixbuf-loaders

PACKAGES += CSWgdkpixbuf-doc
SPKG_DESC_CSWgdkpixbuf-doc = $(DESCRIPTION), Documentation
ARCHALL_CSWgdkpixbuf-doc = 1
PKGFILES_CSWgdkpixbuf-doc = .*/gtk-doc/.*

PACKAGES += CSWlibgdk-pixbuf2-0-0
SPKG_DESC_CSWlibgdk-pixbuf2-0-0 = $(DESCRIPTION), libgdk_pixbuf-2.0.so.0
PKGFILES_CSWlibgdk-pixbuf2-0-0 = $(call pkgfiles_lib,libgdk_pixbuf-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0  = CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf2-0-0 += CSWlibintl8

PACKAGES += CSWlibgdk-pixbuf-xlib2-0-0
SPKG_DESC_CSWlibgdk-pixbuf-xlib2-0-0 = $(DESCRIPTION), libgdk_pixbuf_xlib-2.0.so.0
PKGFILES_CSWlibgdk-pixbuf-xlib2-0-0 = $(call pkgfiles_lib,libgdk_pixbuf_xlib-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0  = CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-xlib2-0-0 += CSWlibpng12-0

PACKAGES += CSWgdkpixbuf-loaders
SPKG_DESC_CSWgdkpixbuf-loaders = $(DESCRIPTION), loader modules
PKGFILES_CSWgdkpixbuf-loaders  = .*/loaders/.*\.so
PKGFILES_CSWgdkpixbuf-loaders += .*/gdk-pixbuf-query-loaders
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders  = CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWtiff

PACKAGES += CSWlibgdk-pixbuf-dev
SPKG_DESC_CSWlibgdk-pixbuf-dev = Developtment files $(DESCRIPTION)
PKGFILES_CSWlibgdk-pixbuf-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-dev = CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-dev += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-pixbuf-dev += CSWlibgdk-pixbuf-xlib2-0-0

BUILD_DEP_PKGS  = CSWggettext-dev
BUILD_DEP_PKGS += CSWjbigkit
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibintl8
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWtiff

ISAEXEC = 0
BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv-prefix
CONFIGURE_ARGS += --with-libintl-prefix

include gar/category.mk

