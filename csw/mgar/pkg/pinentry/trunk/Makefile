# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = pinentry
GARVERSION = 0.7.6
CATEGORIES = utils
DESCRIPTION = Allows entering passwords into gpg-agent.
define BLURB
endef
SPKG_SOURCEURL = http://www.gnupg.org/
PKG_CONFIG_PATH = /opt/csw/lib/pkgconfig
MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/pinentry/
PATCHFILES  = 0001-remove-__extension__-from-util.c.patch
PATCHFILES += 0002-ncurses-include.patch
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
REQUIRED_PKGS = CSWglib CSWgtk CSWiconv CSWncurses
PREREQUISITE_PKGS = $(REQUIRED_PKGS)
PREREQUISITE_PKGS += CSWgtk2devel
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
include gar/category.mk
