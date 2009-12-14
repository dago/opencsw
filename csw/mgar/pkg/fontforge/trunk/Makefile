# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = fontforge
VERSION_DATESTAMP = 20090923
GARVERSION = 0.$(VERSION_DATESTAMP)
CATEGORIES = lib
DESCRIPTION = An outline font editor
define BLURB
endef
SPKG_SOURCEURL = http://fontforge.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = fontforge
REQUIRED_PKGS += CSWggettextrt
REQUIRED_PKGS += CSWiconv
REQUIRED_PKGS += CSWlibice
REQUIRED_PKGS += CSWlibsm
REQUIRED_PKGS += CSWpython
REQUIRED_PKGS += CSWpython-rt

DISTNAME = fontforge-$(VERSION_DATESTAMP)
PATCHFILES  = grayscale.patch
PATCHFILES += grayscale-cvdgloss.c.patch
DISTFILES  = fontforge_full-$(VERSION_DATESTAMP).tar.bz2
UFILES_REGEX = fontforge_full-(\d+(?:\.\d+)*).tar.bz2
CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_LINKER_FLAGS = -liconv -lintl -lrt
TEST_SCRIPTS =
include gar/category.mk
