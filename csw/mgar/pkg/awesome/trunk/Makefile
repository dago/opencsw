# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARFLAVOR = DBG

NAME = awesome
VERSION = 3.4.4
GARTYPE = v2
DESCRIPTION = A tiling window manager for X
define BLURB
endef
SPKG_SOURCEURL = http://awesome.naquadah.org/
MASTER_SITES = http://awesome.naquadah.org/download/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = awesome
INSTALL_SCRIPTS = awesome
CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER = GNU
# EXTRA_LD_OPTIONS = -L/opt/csw/lib -liconv
# EXTRA_CFLAGS = -xc99 -DCE
# EXTRA_CXXFLAGS = -xc99 -DCEPLUSPLUS
TEST_SCRIPTS =

EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib
EXTRA_PKG_CONFIG_DIRS = /opt/csw/X11/lib
PATCHFILES += gperf.sh-solarify.patch
PATCHFILES += backtrace.c.patch
PATCHFILES += iconv-try-1.patch
# PATCHFILES += libiconv.patch
PATCHFILES += test-dash-e-unavailable.patch
PATCHFILES += remove-export-dynamic.patch
PATCHFILES += turn-off-rpath-breakage.patch

CMAKE_ARGS  = -DSYSCONFDIR=/etc/opt/csw
CMAKE_ARGS += -DPREFIX=/opt/csw
export CMAKE_ARGS

RUNTIME_DEP_PKGS_CSWawesome += CSWggettextrt
RUNTIME_DEP_PKGS_CSWawesome += CSWglib2
RUNTIME_DEP_PKGS_CSWawesome += CSWiconv
RUNTIME_DEP_PKGS_CSWawesome += CSWimlib2
RUNTIME_DEP_PKGS_CSWawesome += CSWlibcairo
RUNTIME_DEP_PKGS_CSWawesome += CSWlibdbus
RUNTIME_DEP_PKGS_CSWawesome += CSWlibev
RUNTIME_DEP_PKGS_CSWawesome += CSWlibx11
RUNTIME_DEP_PKGS_CSWawesome += CSWlibxcb
RUNTIME_DEP_PKGS_CSWawesome += CSWlibxdgbasedir
RUNTIME_DEP_PKGS_CSWawesome += CSWlua
RUNTIME_DEP_PKGS_CSWawesome += CSWpango
RUNTIME_DEP_PKGS_CSWawesome += CSWstartupnotif
RUNTIME_DEP_PKGS_CSWawesome += CSWxcbutil

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWawesome)
BUILD_DEP_PKGS += CSWcmake
BUILD_DEP_PKGS += CSWgperf
BUILD_DEP_PKGS += CSWlibdbusdev
BUILD_DEP_PKGS += CSWimagemagick
BUILD_DEP_PKGS += CSWlibcairodevel
# Enable when fixed to used gtail
# BUILD_DEP_PKGS += CSWasciidoc
# BUILD_DEP_PKGS += CSWxmlto
BUILD_DEP_PKGS += CSWxcbproto
BUILD_DEP_PKGS += CSWpyxcbproto
BUILD_DEP_PKGS += CSWlibxdmcpdevel
BUILD_DEP_PKGS += CSWlibxaudevel
BUILD_DEP_PKGS += CSWlibxrenderdevel
BUILD_DEP_PKGS += CSWlibx11devel

LICENSE = LICENSE

include gar/category.mk

build-awesome:
	(cd $(WORKSRC); gmake $(BUILD_ENV) VERBOSE=1 $(PARALLELMFLAGS))
	@$(MAKECOOKIE)

install-awesome:
	(cd $(WORKSRC); gmake  $(INSTALL_ENV) install)
	@$(MAKECOOKIE)

PATH := /opt/csw/gnu:$(PATH)
# PATCHFILES += turn-off-rpath-breakage.patch
