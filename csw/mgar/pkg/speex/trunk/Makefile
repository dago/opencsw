# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = speex
GARVERSION = 1.2rc1
CATEGORIES = lib

DESCRIPTION = Speex audio codec support library
define BLURB
endef

MASTER_SITES = http://downloads.xiph.org/releases/speex/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWspeex
CATALOGNAME = libspeex
REQUIRED_PKGS = CSWlibogg
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

SPKG_SOURCEURL = http://www.speex.org/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# 64-bit doesn't build on x86.
# BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
