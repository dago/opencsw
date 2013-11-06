# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#

# ! Doesn't build due to missing dependency to XInput2 which is not in OpenCSW as of 2013-11-06.

NAME = gtk3
VERSION = 3.6.4
DISTNAME = gtk+-$(VERSION)
GARTYPE = v2

GARCOMPILER = GNU
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = Brief description
define BLURB
  Long description
endef

GNOME_PROJ = gtk+
MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz

BUILD_DEP_PKGS  = CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibpango-dev
BUILD_DEP_PKGS += CSWlibcairo-dev
BUILD_DEP_PKGS += CSWlibatk-dev

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-explicit-deps=yes
CONFIGURE_ARGS += --disable-papi

include gar/category.mk

