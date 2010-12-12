# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id: Makefile 8335 2010-02-03 18:36:29Z wahwah $

NAME = xmms
VERSION = 1.2.11
CATEGORIES = gnome

DESCRIPTION = The X MultiMedia System.
define BLURB
    XMMS is a multimedia player based on the look of WinAmp. XMMS plays MPEG layer
    1/2/3, Ogg Vorbis, WAV, all formats supported by libmikmod, and CD audio. XMMS
    has a plugin system for Input / Output / Effects / Visualization, and through
    plugins it can play a lot more sound and video formats.
endef

MASTER_SITES = http://www.xmms.org/files/1.2.x/
DISTFILES = $(NAME)-$(VERSION).tar.bz2
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-glib-prefix=$(prefix)
CONFIGURE_ARGS += --with-gtk-prefix=$(prefix)
CONFIGURE_ARGS += --with-ogg=$(prefix)
CONFIGURE_ARGS += --with-vorbis=$(prefix)

# Needed for opengl plugin
EXTRA_CPPFLAGS = -DSUN_OGL_NO_VERTEX_MACROS

# No test suite
TEST_SCRIPTS =

RUNTIME_DEP_PKGS_CSWxmms += CSWglib
RUNTIME_DEP_PKGS_CSWxmms += CSWmesa
RUNTIME_DEP_PKGS_CSWxmms += CSWesound
RUNTIME_DEP_PKGS_CSWxmms += CSWvorbis
RUNTIME_DEP_PKGS_CSWxmms += CSWlibogg
RUNTIME_DEP_PKGS_CSWxmms += CSWmikmod
RUNTIME_DEP_PKGS_CSWxmms += CSWiconv
RUNTIME_DEP_PKGS_CSWxmms += CSWgtk
RUNTIME_DEP_PKGS_CSWxmms += CSWzlib
RUNTIME_DEP_PKGS_CSWxmms += CSWggettextrt

include gar/category.mk
