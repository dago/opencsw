# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = vbindiff
VERSION = 3.0_beta4
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Visual Binary Diff
define BLURB
endef

MASTER_SITES = http://www.cjmweb.net/vbindiff/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWvbindiff
SPKG_DESC_CSWvbindiff = Visual binary diff
RUNTIME_DEP_PKGS_CSWvbindiff += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWvbindiff += CSWlibpanel5

REINPLACEMENTS = wall
REINPLACE_MATCH_wall = -Wall
REINPLACE_WITH_wall =
REINPLACE_FILES_wall += Makefile.in

EXTRA_INC += $(includedir)/ncurses

EXTRA_CXXFLAGS = -norunpath

#CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

