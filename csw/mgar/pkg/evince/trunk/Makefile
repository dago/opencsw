# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = evince
GNOME_VERSION = 2.24
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
EXTRA_LD_OPTIONS = /opt/csw/X11/lib/libX11.so -lm
# There are no shared-object dependencies on CSWdbus, but it's required for
# evince to work.
RUNTIME_DEP_PKGS_CSWevince += CSWdbus
RUNTIME_DEP_PKGS_CSWevince += CSWdbusglib
RUNTIME_DEP_PKGS_CSWevince += CSWdjvulibre
RUNTIME_DEP_PKGS_CSWevince += CSWfconfig
RUNTIME_DEP_PKGS_CSWevince += CSWftype2
RUNTIME_DEP_PKGS_CSWevince += CSWgconf2
RUNTIME_DEP_PKGS_CSWevince += CSWggettextrt
RUNTIME_DEP_PKGS_CSWevince += CSWglib2
RUNTIME_DEP_PKGS_CSWevince += CSWgnomekeyring
RUNTIME_DEP_PKGS_CSWevince += CSWgtk2
RUNTIME_DEP_PKGS_CSWevince += CSWiconv
RUNTIME_DEP_PKGS_CSWevince += CSWjpeg
RUNTIME_DEP_PKGS_CSWevince += CSWlibatk
RUNTIME_DEP_PKGS_CSWevince += CSWlibcairo
RUNTIME_DEP_PKGS_CSWevince += CSWlibdbus
RUNTIME_DEP_PKGS_CSWevince += CSWlibglade2
RUNTIME_DEP_PKGS_CSWevince += CSWlibice
RUNTIME_DEP_PKGS_CSWevince += CSWlibsm
RUNTIME_DEP_PKGS_CSWevince += CSWlibx11
RUNTIME_DEP_PKGS_CSWevince += CSWlibxml2
RUNTIME_DEP_PKGS_CSWevince += CSWpango
RUNTIME_DEP_PKGS_CSWevince += CSWpoppler
RUNTIME_DEP_PKGS_CSWevince += CSWtiff
RUNTIME_DEP_PKGS_CSWevince += CSWzlib
include gar/category.mk
