# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id: Makefile 8335 2010-02-03 18:36:29Z wahwah $

NAME = gnome-icon-theme
GNOME_VERSION = 2.22
VERSION = $(GNOME_VERSION).0
CATEGORIES = gnome
DESCRIPTION = GNOME icon theme
define BLURB
endef
SPKG_SOURCEURL = http://ftp.gnome.org/pub/GNOME/sources/$(NAME)/
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(NAME)/$(GNOME_VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWgnomeicontheme	
CATALOGNAME_CSWgnomeicontheme = gnome_icon_theme
RUNTIME_DEP_PKGS_CSWgnomeicontheme = CSWicon-naming-utils
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWgnomeicontheme)
CONFIGURE_ARGS = $(DIRPATHS)
ARCHALL_CSWgnomeicontheme = 1
include gar/category.mk
