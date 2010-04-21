# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id: Makefile 8335 2010-02-03 18:36:29Z wahwah $

GARNAME = xmms
GARVERSION = 1.2.11
CATEGORIES = gnome

DESCRIPTION = The X MultiMedia System.
define BLURB
    XMMS is a multimedia player based on the look of WinAmp. XMMS plays MPEG layer
    1/2/3, Ogg Vorbis, WAV, all formats supported by libmikmod, and CD audio. XMMS
    has a plugin system for Input / Output / Effects / Visualization, and through
    plugins it can play a lot more sound and video formats.
endef

MASTER_SITES = http://www.xmms.org/files/1.2.x/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-glib-prefix=$(prefix)
CONFIGURE_ARGS += --with-gtk-prefix=$(prefix)
CONFIGURE_ARGS += --with-ogg=$(prefix)
CONFIGURE_ARGS += --with-vorbis=$(prefix)

# No test suite
TEST_SCRIPTS =

DEP_PKGS_CSWxmms += CSWesound
DEP_PKGS_CSWxmms += CSWmesa
DEP_PKGS_CSWxmms += CSWlibx11
DEP_PKGS_CSWxmms += CSWlibice
DEP_PKGS_CSWxmms += CSWlibsm
DEP_PKGS_CSWxmms += CSWlibogg
DEP_PKGS_CSWxmms += CSWvorbis
DEP_PKGS_CSWxmms += CSWiconv
DEP_PKGS_CSWxmms += CSWlibxext
DEP_PKGS_CSWxmms += CSWggettextrt
DEP_PKGS_CSWxmms += CSWglib
DEP_PKGS_CSWxmms += CSWzlib
DEP_PKGS_CSWxmms += CSWgtk
DEP_PKGS_CSWxmms += CSWmikmod

include gar/category.mk
