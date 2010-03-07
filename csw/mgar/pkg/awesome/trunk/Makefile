# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = awesome
GARVERSION = 3.4.4
CATEGORIES = apps
DESCRIPTION = A tiling window manager for X
define BLURB
endef
SPKG_SOURCEURL = http://awesome.naquadah.org/
MASTER_SITES = http://awesome.naquadah.org/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = awesome
INSTALL_SCRIPTS = awesome
CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER = GNU
EXTRA_LD_OPTIONS = -L/opt/csw/lib -liconv

BUILD_DEP_PKGS += CSWlua CSWgperf
EXTRA_PKG_CONFIG_PATH += /opt/csw/X11/lib/pkgconfig
PATCHFILES += gperf.sh-solarify.patch
PATCHFILES += backtrace.c.patch

include gar/category.mk

build-awesome:
	(cd $(WORKSRC); gmake $(BUILD_ENV) VERBOSE=1)
	@$(MAKECOOKIE)

install-awesome:
	(cd $(WORKSRC); gmake  $(INSTALL_ENV) install)
	@$(MAKECOOKIE)

PATH := /opt/csw/gnu:$(PATH)
