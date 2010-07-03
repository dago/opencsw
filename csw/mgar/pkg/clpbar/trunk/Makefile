# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = bar
GARVERSION = 1.10.9
CATEGORIES = apps
DESCRIPTION = A command line tool to display information about a data transfer stream
define BLURB
endef
SPKG_SOURCEURL = http://clpbar.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = clpbar
PATCHFILES += 0001-Allowing-to-modify-CFLAGS.patch

DISTFILES  = $(GARNAME)_$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
TEST_TARGET = check
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
