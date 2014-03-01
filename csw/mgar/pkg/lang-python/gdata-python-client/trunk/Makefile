# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = gdata-python-client
VERSION = 2.0.18
CATEGORIES = python
GARTYPE = v2
DESCRIPTION  = Google Data Protocol, a REST-inspired technology
SPKG_SOURCEURL = http://code.google.com/apis/gdata/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = gdata-$(VERSION).tar.gz
DISTNAME = gdata-$(VERSION)
RUNTIME_DEP_PKGS =
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWpysetuptools
TEST_SCRIPTS =
LICENSE = PKG-INFO
PATCHFILES += 0001-Remove-a-usr-local-reference.patch

PACKAGES += CSWpy-gdata
SPKG_DESC_CSWpy-gdata = $(DESCRIPTION)
INCOMPATIBLE_PKGS_CSWpy-gdata = CSWpygdata
ARCHALL_CSWpy-gdata = 1

include gar/category.mk
