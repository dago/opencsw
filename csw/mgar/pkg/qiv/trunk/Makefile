# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = qiv
VERSION = 2.3.1
GARTYPE = v2

DESCRIPTION = Quick image viewer
define BLURB
  Quick Image Viewer (qiv) is a fast and simple image viewer based
  on GDK and imlib. Features include zooming, fullscreen, statusbar,
  screensaver mode, brightness/contrast control, transparency,
  slideshow, exif autorotation and a browse mode.
endef

MASTER_SITES = http://spiegl.de/qiv/download/
DISTFILES  = $(DISTNAME).tgz
LICENSE = README.COPYING

RUNTIME_DEP_PKGS += CSWlibmagic1 CSWlibgdk-x11-2-0-0 CSWlibgdk-pixbuf2-0-0 \
  CSWlibgobject2-0-0 CSWlibimlib2-1 CSWlibglib2-0-0 CSWlibpango1-0-0 \
  CSWlibtiff5 CSWliblcms2-2 CSWlibexif12 CSWlibjpeg7

PATCHFILES += 0001-adapt-Makefile-for-opencsw.patch
CONFIGURE_SCRIPTS =
EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig
BUILD_ARGS = -f Makefile.Solaris
TEST_SCRIPTS =
INSTALL_ARGS = -f Makefile.Solaris

include gar/category.mk

