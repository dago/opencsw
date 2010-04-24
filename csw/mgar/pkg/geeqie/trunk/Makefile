# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = geeqie
GARVERSION = 1.0
CATEGORIES = gnome
DESCRIPTION = A lightweight image viewer, forked from GQview
define BLURB
endef
SPKG_SOURCEURL = http://geeqie.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
TEST_TARGET = check
CONFIGURE_ARGS = $(DIRPATHS)
EXTRA_LDFLAGS = -lsocket

RUNTIME_DEP_PKGS_CSWgeeqie += CSWgtk2
RUNTIME_DEP_PKGS_CSWgeeqie += CSWlcmsrt
RUNTIME_DEP_PKGS_CSWgeeqie += CSWglib2
RUNTIME_DEP_PKGS_CSWgeeqie += CSWpango
RUNTIME_DEP_PKGS_CSWgeeqie += CSWlibatk
RUNTIME_DEP_PKGS_CSWgeeqie += CSWggettextrt
RUNTIME_DEP_PKGS_CSWgeeqie += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgeeqie += CSWfconfig
RUNTIME_DEP_PKGS_CSWgeeqie += CSWftype2

include gar/category.mk
