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
DISTFILES += CSWgdkpixbuf.postinstall

EXPANDVARS = CSWgdkpixbuf.postinstall

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWgdkpixbuf
CATALOGNAME_CSWgdkpixbuf = gdkpixbuf
SPKG_DESC_CSWgdkpixbuf = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgdkpixbuf  = CSWlibgdk_pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgdk_pixbuf_xlib2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibz1


PACKAGES += CSWlibgdk_pixbuf2-0-0
SPKG_DESC_CSWlibgdk_pixbuf2-0-0 = $(DESCRIPTION), libgdk_pixbuf-2.0.so.0
PKGFILES_CSWlibgdk_pixbuf2-0-0 = $(call pkgfiles_lib,libgdk_pixbuf-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf2-0-0  = CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf2-0-0 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf2-0-0 += CSWlibz1

PACKAGES += CSWlibgdk_pixbuf_xlib2-0-0
SPKG_DESC_CSWlibgdk_pixbuf_xlib2-0-0 = $(DESCRIPTION), libgdk_pixbuf_xlib-2.0.so.0
PKGFILES_CSWlibgdk_pixbuf_xlib2-0-0 = $(call pkgfiles_lib,libgdk_pixbuf_xlib-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf_xlib2-0-0  = CSWlibgdk_pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf_xlib2-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf_xlib2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf_xlib2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf_xlib2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf_xlib2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf_xlib2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf_xlib2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf_xlib2-0-0 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgdk_pixbuf_xlib2-0-0 += CSWlibz1

PACKAGES += CSWgdkpixbuf-loaders
CATALOGNAME_CSWgdkpixbuf-loaders = gdkpixbuf_loaders
SPKG_DESC_CSWgdkpixbuf-loaders = $(DESCRIPTION), loader modules
PKGFILES_CSWgdkpixbuf-loaders = .*/loaders/.*\.so
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders  = CSWlibgdk_pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWjbigkit
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWlibz1
RUNTIME_DEP_PKGS_CSWgdkpixbuf-loaders += CSWtiff

PACKAGES += CSWgdkpixbuf-dev
CATALOGNAME_CSWgdkpixbuf-dev = gdkpixbuf_dev
SPKG_DESC_CSWgdkpixbuf-dev = Developtment files $(DESCRIPTION)
PKGFILES_CSWgdkpixbuf-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWgdkpixbuf-dev = CSWgdkpixbuf

BUILD_DEP_PKGS  = CSWggettext-dev
BUILD_DEP_PKGS += CSWjbigkit
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibintl8
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWtiff

# I don't want to do this, but currently I see no other way to get the 32/64
# binaries into the package. The default only includes the 32bit binaries, but
# not the 64bit ones. --raos
ISAEXEC = 1
BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv-prefix
CONFIGURE_ARGS += --with-libintl-prefix

include gar/category.mk

