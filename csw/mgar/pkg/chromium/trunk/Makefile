# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = chromium
CHROMIUM_REVISION = 32797
GARVERSION = 0.$(CHROMIUM_REVISION)
CATEGORIES = lib
DESCRIPTION = An open-source web browser
define BLURB
endef
SPKG_SOURCEURL =
MASTER_SITES = http://build.chromium.org/buildbot/archives/
# DISTFILES  = chromium.r$(CHROMIUM_REVISION).tgz
DISTFILES   =
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
REQUIRED_PKGS = CSWnspr CSWnss CSWffmpeg
# CSWpyxml must be uninstalled
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWnspr-devel CSWlibxcbdevel CSWffmpeg CSWgperf CSWpython
CONFIGURE_SCRIPTS = chromium
BUILD_SCRIPTS     = chromium
INSTALL_SCRIPTS   = chromium
TEST_SCRIPTS      = chromium

GIT_URI = git://git.chromium.org/chromium.git

GYP_GENERATORS = make
export GYP_GENERATORS

# WORKSRC = $(WORKDIR)/home/chrome-svn/tarball/chromium
WORKSRC = $(WORKDIR)/chromium
CHROMIUM_ROOT = $(WORKSRC)

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

GARCOMPILER = GNU

# # Because of bashisms in Makefiles in Chromium
# SHELL = /opt/csw/bin/bash

# TODO: Make V8 realize it's a known architecture.
# EXTRA_CFLAGS = -DV8_TARGET_ARCH_IA32
# EXTRA_CXXFLAGS = -DV8_TARGET_ARCH_IA32

include gar/category.mk

$(WORKSRC)/.gclient:
	(cd $(WORKSRC) \
	    && \
	PATH=$$PATH:$(abspath $(WORKDIR)/depot_tools) \
	gclient config http://src.chromium.org/svn/trunk/src)

post-extract-modulated:
	mkdir -p $(WORKSRC)
	(cd $(WORKSRC) \
	    && \
	if [ -d src ]; then \
	  (cd src && git fetch ); \
	else \
	  git clone $(GIT_URI) src; \
	fi)
	@$(MAKECOOKIE)

# Skipping gclient sync for now; running only gclient runhooks.  The build
# instructions say that we'll miss on some platform-specific depends, but
# I don't think there's anything platform-specific for Solaris in the source
# code repository.

configure-chromium: prerequisite-tests depot-tools gclient-sync

prerequisite-tests:
	python files/xml_dom_minidom_test.py
	@$(MAKECOOKIE)

gclient-sync: $(WORKSRC)/.gclient
	(cd $(WORKSRC) \
		&& \
	PATH=$(PATH):$(abspath $(WORKDIR)/depot_tools) \
	GYP_DEFINES="use_system_ffmpeg=1" \
	GYP_GENERATORS=make \
	gclient sync --revision src@$(CHROMIUM_REVISION))
	# gclient sync)
	@$(MAKECOOKIE)

gclient-runhooks: $(WORKSRC)/.gclient
	(cd $(WORKSRC) \
		&& \
	PATH=$(PATH):$(abspath $(WORKDIR)/depot_tools) \
	GYP_GENERATORS=make \
	GYP_DEFINES="use_system_ffmpeg=1" \
	gclient runhooks --force)
	@$(MAKECOOKIE)

depot-tools:
	(cd $(WORKDIR) \
	    && \
	 if [ -d depot_tools ]; then \
	   (cd depot_tools; svn up); \
	 else \
	   svn co http://src.chromium.org/svn/trunk/tools/depot_tools; \
	 fi \
	)
	@$(MAKECOOKIE)

build-chromium:
	(cd $(CHROMIUM_ROOT)/src \
		&& \
	PATH=$$PATH:$(abspath $(WORKDIR)/depot_tools):/opt/csw/gcc4/bin \
	gmake $(PARALLELMFLAGS) chrome)
	false
	@$(MAKECOOKIE)
