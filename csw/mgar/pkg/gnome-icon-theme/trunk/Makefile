# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id: Makefile 8335 2010-02-03 18:36:29Z wahwah $

GARNAME = gnome-icon-theme
GNOME_VERSION = 2.22
GARVERSION = $(GNOME_VERSION).0
CATEGORIES = gnome
DESCRIPTION = GNOME icon theme
define BLURB
endef
SPKG_SOURCEURL = http://ftp.gnome.org/pub/GNOME/sources/$(GARNAME)/
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(GARNAME)/$(GNOME_VERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWgnomeicontheme	
CATALOGNAME_CSWgnomeicontheme = gnome_icon_theme
RUNTIME_DEP_PKGS_CSWgnomeicontheme = CSWicon-naming-utils
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWgnomeicontheme)
TEST_TARGET = check
CONFIGURE_ARGS = $(DIRPATHS)
ARCHALL_CSWgnomeicontheme = 1
include gar/category.mk
