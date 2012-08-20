# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gpsbabel
VERSION = 1.4.3
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = GPS data translator
define BLURB
  GPSBabel lets you move data between popular GPS systems such as those from Garmin, Magellan or a large number of map programs. 
endef

MASTER_SITES = http://www.gpsbabel.org/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = SOS12U3

BUILD_DEP_PKGS += CSWlibexpat-dev
RUNTIME_DEP_PKGS_CSWgpsbabel += CSWlibexpat1

SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

