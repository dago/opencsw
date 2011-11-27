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

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWgdkpixbuf
CATALOGNAME_CSWgdkpixbuf = gdk_pixbuf
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWtiff
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibjpeg62
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgdkpixbuf += CSWglib2

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

