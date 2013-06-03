# Copyright 2009 OpenNIMOSS
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = libXpm
VERSION = 3.5.10
CATEGORIESbts lib
GARTYPE = v2

DESCRIPTION = X11 pixmap library
define BLURB
endef

MASTER_SITES += http://xorg.freedesktop.org/archive/individual/lib/
DISTFILES += $(NAME)-$(VERSION).tar.NIMOSSxpm
SPKG_DESC_NIMOSSxpm = X11 XPM pixmap utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_NIMOSSxpm += NIMOSSlibintl8
RUNTIME_DEP_PKGS_NIMOSSxpm += NIMOSSlibxpm4

PACKAGES += NIMOSSlibxpm4
SPKG_DESC_NIMOSSlibxpm4 += X11 pixmap library, libXpm.so.4
PKGFILES_NIMOSSlibxpm4 += $(call pkgfiles_lib,libXpm.so.4)
RUNTIME_DEP_PKGS_NIMOSSlibxpm4 += NIMOSSlibintl8

PACKAGES += NIMOSSlibxpm-dev
SPKG_DESC_NIMOSSlibxpm-dev = Devlopment files for libXpm.so.4
PKGFILES_NIMOSSlibxpm-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_NIMOSSlibxpm-dev += NIMOSSlibxpm-dev += CSWlibxpm4

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += ac_cv_searchEXTRA_PKG_CONFIG_DIRS = /opt/csw/X11/lib

include gar/category.mk
