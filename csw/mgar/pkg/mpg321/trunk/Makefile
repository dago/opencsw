# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = mpg321
GARVERSION = 0.2.11
DISTFILE_SUFFIX = -2
CATEGORIES = apps

DESCRIPTION = A Free replacement for mpg123
SPKG_SOURCEURL = http://mpg321.sourceforge.net/
define BLURB
endef
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION)$(DISTFILE_SUFFIX).tar.gz
RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibao
RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibid3tag
RUNTIME_DEP_PKGS_CSWmpg321 += CSWlibmad
RUNTIME_DEP_PKGS_CSWmpg321 += CSWzlib
BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS_CSWmpg321)
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
TEST_TARGET = check
CONFIGURE_ARGS = $(DIRPATHS)
# A fix for an inline function and 'symbol not found'.
EXTRA_CFLAGS = -features=no%extinl
include gar/category.mk
