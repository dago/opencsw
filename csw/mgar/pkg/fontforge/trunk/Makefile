# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = fontforge
VERSION_DATESTAMP = 20090923
VERSION = 0.$(VERSION_DATESTAMP)
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = An outline font editor
define BLURB
endef
SPKG_SOURCEURL = http://fontforge.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = fontforge
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWiconv
RUNTIME_DEP_PKGS += CSWpython

DISTNAME = fontforge-$(VERSION_DATESTAMP)
PATCHFILES  = grayscale.patch
PATCHFILES += grayscale-cvdgloss.c.patch
DISTFILES  = fontforge_full-$(VERSION_DATESTAMP).tar.bz2
UFILES_REGEX = fontforge_full-(\d+(?:\.\d+)*).tar.bz2
CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_LINKER_FLAGS = -liconv -lintl -lrt
TEST_SCRIPTS =
include gar/category.mk
