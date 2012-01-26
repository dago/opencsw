# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Header$

NAME = shout-python
VERSION = 0.2.1
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Python bindings for libshout 2

define BLURB
endef

MASTER_SITES = http://downloads.us.xiph.org/releases/libshout/
DISTFILES  = $(DISTNAME).tar.gz

SPKG_SOURCEURL = http://www.icecast.org/

RUNTIME_DEP_PKGS = CSWlibogg CSWlibshout CSWspeex CSWtheora CSWvorbis

PACKAGES = CSWpyshout
CATALOGNAME_CSWpyshout = py_shout

RUNTIME_DEP_PKGS_CSWpyshout =

BUILD_SCRIPTS = custom

TEST_SCRIPTS =

include gar/category.mk

build-custom:
	(cd $(WORKSRC); $(BUILD_ENV) python setup.py build)
	@$(MAKECOOKIE)

