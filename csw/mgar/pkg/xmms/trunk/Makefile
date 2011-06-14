# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id: Makefile 8335 2010-02-03 18:36:29Z wahwah $

NAME = xmms
VERSION = 1.2.11
CATEGORIES = gnome

DESCRIPTION = The X MultiMedia System
define BLURB
    XMMS is a multimedia player based on the look of WinAmp. XMMS plays MPEG layer
    1/2/3, Ogg Vorbis, WAV, all formats supported by libmikmod, and CD audio. XMMS
    has a plugin system for Input / Output / Effects / Visualization, and through
    plugins it can play a lot more sound and video formats.
endef

MASTER_SITES = http://www.xmms.org/files/1.2.x/
DISTFILES = $(NAME)-$(VERSION).tar.bz2

PACKAGES += CSWlibxmms1
SPKG_DESC_CSWlibxmms1 += The X MultiMedia System library, libxmms.so.1
PKGFILES_CSWlibxmms1 += $(call pkgfiles_lib,libxmms.so.1)
RUNTIME_DEP_PKGS_CSWlibxmms1 += CSWglib
RUNTIME_DEP_PKGS_CSWlibxmms1 += CSWgtk

PACKAGES += CSWlibxmms-dev
SPKG_DESC_CSWlibxmms-dev = Development files for libxmms.so.1
PKGFILES_CSWlibxmms-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibxmms-dev += CSWlibxmms1

PACKAGES += CSWxmms
SPKG_DESC_CSWxmms = The X MultiMedia System
RUNTIME_DEP_PKGS_CSWxmms += CSWlibxmms1
RUNTIME_DEP_PKGS_CSWxmms += CSWiconv
RUNTIME_DEP_PKGS_CSWxmms += CSWzlib
RUNTIME_DEP_PKGS_CSWxmms += CSWmesa
RUNTIME_DEP_PKGS_CSWxmms += CSWglib
RUNTIME_DEP_PKGS_CSWxmms += CSWmikmod
RUNTIME_DEP_PKGS_CSWxmms += CSWgtk
RUNTIME_DEP_PKGS_CSWxmms += CSWlibintl8
RUNTIME_DEP_PKGS_CSWxmms += CSWlibogg0
RUNTIME_DEP_PKGS_CSWxmms += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWxmms += CSWlibvorbisfile3
RUNTIME_DEP_PKGS_CSWxmms += CSWlibesd0

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-glib-prefix=$(prefix)
CONFIGURE_ARGS += --with-gtk-prefix=$(prefix)
CONFIGURE_ARGS += --with-ogg=$(prefix)
CONFIGURE_ARGS += --with-vorbis=$(prefix)

# Needed for opengl plugin
EXTRA_CPPFLAGS = -DSUN_OGL_NO_VERTEX_MACROS

# No test suite
TEST_SCRIPTS =

include gar/category.mk
