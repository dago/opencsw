# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = startup-notification
GARVERSION = 0.10
CATEGORIES = gnome
DESCRIPTION = Reference implementation of the startup notification protocol
define BLURB
endef
SPKG_SOURCEURL = http://www.freedesktop.org/wiki/Software/startup-notification
MASTER_SITES = http://www.freedesktop.org/software/startup-notification/releases/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME = startup_notif
PACKAGES = CSWstartupnotif
CONFIGURE_ARGS = $(DIRPATHS)
RUNTIME_DEP_PKGS_CSWstartupnotif += CSWlibice
RUNTIME_DEP_PKGS_CSWstartupnotif += CSWlibsm
RUNTIME_DEP_PKGS_CSWstartupnotif += CSWlibx11
RUNTIME_DEP_PKGS_CSWstartupnotif += CSWlibxcb
RUNTIME_DEP_PKGS_CSWstartupnotif += CSWxcbutil
include gar/category.mk
