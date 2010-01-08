# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = rhythmbox
GARVERSION = 0.12.6
CATEGORIES = apps
DESCRIPTION = an integrated music management application
define BLURB
endef
SPKG_SOURCEURL = http://projects.gnome.org/rhythmbox/
MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/rhythmbox/0.12/
PATCHFILES  = 0001-ggettext-for-intltool.patch
PATCHFILES += 0002-Adding-ACLOCAL_AMFLAGS-I-macros-to-Makefile.am.patch
PATCHFILES += 0003-autoreconf-results.patch
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2
CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_PKG_CONFIG_DIRS = /opt/csw/X11/lib

include gar/category.mk
