# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = evince
GNOME_VERSION = 2.22
GARVERSION = $(GNOME_VERSION).2
CATEGORIES = gnome
DESCRIPTION = Document viewer for multiple document formats
define BLURB
endef
SPKG_SOURCEURL = http://projects.gnome.org/evince/
MASTER_SITES = http://ftp.gnome.org/pub/GNOME/sources/$(GARNAME)/$(GNOME_VERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)
STRIP_LIBTOOL = 1
include gar/category.mk
