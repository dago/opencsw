# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = libXpm
VERSION = 3.5.10
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = X11 pixmap library
define BLURB
endef

MASTER_SITES += http://xorg.freedesktop.org/archive/individual/lib/
DISTFILES += $(NAME)-$(VERSION).tar.bz2

PACKAGES += CSWxpm
SPKG_DESC_CSWxpm = X11 XPM pixmap utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWxpm += CSWlibintl8
RUNTIME_DEP_PKGS_CSWxpm += CSWlibxpm4

PACKAGES += CSWlibxpm4
SPKG_DESC_CSWlibxpm4 += X11 pixmap library, libXpm.so.4
PKGFILES_CSWlibxpm4 += $(call pkgfiles_lib,libXpm.so.4)
RUNTIME_DEP_PKGS_CSWlibxpm4 += CSWlibintl8

PACKAGES += CSWlibxpm-dev
SPKG_DESC_CSWlibxpm-dev = Devlopment files for libXpm.so.4
PKGFILES_CSWlibxpm-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibxpm-dev += CSWlibxpm4

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += ac_cv_search_gettext=-lintl

include gar/category.mk
