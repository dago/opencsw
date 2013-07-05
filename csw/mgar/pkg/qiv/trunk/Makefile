# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = qiv
VERSION = 2.2.4
GARTYPE = v2

DESCRIPTION = Quick image viewer
define BLURB
  Quick Image Viewer (qiv) is a fast and simple image viewer based
  on GDK and imlib. Features include zooming, fullscreen, statusbar,
  screensaver mode, brighness/contrast control, transparency,
  slideshow, exif autorotation and a browse mode.
endef

MASTER_SITES = http://spiegl.de/qiv/download/
DISTFILES  = $(DISTNAME).tgz
LICENSE = README.COPYING

RUNTIME_DEP_PKGS += CSWlibmagic1 CSWlibgdk-x11-2-0-0 CSWlibgdk-pixbuf2-0-0 \
  CSWlibgobject2-0-0 CSWlibimlib2-1 CSWlibglib2-0-0 CSWpango

PATCHFILES += 0001-adapt-Makefile-for-opencsw.patch
CONFIGURE_SCRIPTS =
BUILD_ARGS = -f Makefile.Solaris
TEST_SCRIPTS =
INSTALL_ARGS = -f Makefile.Solaris

include gar/category.mk

