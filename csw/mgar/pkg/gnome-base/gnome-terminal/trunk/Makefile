# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = gnome-terminal
GT_MAJOR_VERSION = 2
GT_MINOR_VERSION = 22
GT_PATCHLEVEL = 1
VERSION = $(GT_MAJOR_VERSION).$(GT_MINOR_VERSION).$(GT_PATCHLEVEL)
CATEGORIES = gnome
GARTYPE = v2
DESCRIPTION = A terminal emulator, part of GNOME
define BLURB
endef
SPKG_SOURCEURL = http://www.gnome.org/
MASTER_SITES = http://ftp.heanet.ie/pub/ftp.gnome.org/sources/gnome-terminal/$(GT_MAJOR_VERSION).$(GT_MINOR_VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWlibxft2devel
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
MSGFMT= /opt/csw/bin/gmsgfmt
MSGMERGE= /opt/csw/bin/gmsgmerge
XGETTEXT = /opt/csw/bin/gxgettext
GETTEXT = /opt/csw/bin/ggettext
export MSGMERGE
export MSGFMT
export XGETTEXT
export GETTEXT

include gar/category.mk

# TODO: Update CSWvte
