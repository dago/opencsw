# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = web
VERSION = 0.37
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Simple web framework for Python
VENDOR_URL = http://webpy.org/
MASTER_SITES = http://webpy.org/static/
DISTNAME = web.py-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
PACKAGES = CSWpy-webpy
RUNTIME_DEP_PKGS = CSWpy-flup
CHECKPKG_OVERRIDES_CSWpy-webpy += surplus-dependency|CSWpy-flup
ARCHALL = 1
LICENSE = PKG-INFO
TEST_SCRIPTS =

include gar/category.mk
