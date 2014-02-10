# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xsane
VERSION = 0.999
GARTYPE = v2
# CATEGORIES = category

DESCRIPTION = XSane graphical scanning frontend
define BLURB
  Long description
endef

MASTER_SITES = http://www.xsane.org/download/
DISTFILES  = $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibpango-dev

# on libpng15 API changed
PATCHFILES = 0001-libpng15.patch

RUNTIME_DEP_PKGS_CSWxsane += CSWlibtiff5
RUNTIME_DEP_PKGS_CSWxsane += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWxsane += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWxsane += CSWlibintl8
RUNTIME_DEP_PKGS_CSWxsane += CSWlibz1
RUNTIME_DEP_PKGS_CSWxsane += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWxsane += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWxsane += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWxsane += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWxsane += CSWlibsane1
CHECKPKG_OVERRIDES_CSWxsane += file-with-bad-content|/usr/share|root/opt/csw/bin/xsane

GARCOMPILER = GCC4

EXTRA_LINKER_FLAGS  = -lsocket -lnsl
SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

