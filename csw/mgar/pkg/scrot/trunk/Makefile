# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = scrot
VERSION = 0.8

DESCRIPTION = Screen capture utility

MASTER_SITES = http://linuxbrit.co.uk/downloads/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Do-not-add-Wall.patch

VENDOR_URL = http://freecode.com/projects/scrot

BUILD_DEP_PKGS += CSWlibgiblib-dev
BUILD_DEP_PKGS += CSWimlib2

PACKAGES += CSWscrot
SPKG_DESC_CSWscrot = Screen capture utility
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWscrot += CSWlibgiblib1
RUNTIME_DEP_PKGS_CSWscrot += CSWimlib2

include gar/category.mk

