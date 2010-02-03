# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = gdata-python-client
GARVERSION = 2.0.3
CATEGORIES = python
DESCRIPTION  = Google Data Protocol, a REST-inspired technology
define BLURB
endef
SPKG_SOURCEURL = http://code.google.com/apis/gdata/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = gdata-$(GARVERSION).tar.gz
WORKSRC = $(WORKDIR)/gdata-$(GARVERSION)
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME = py_gdata
PACKAGES = CSWpygdata
ARCHALL_CSWpygdata = 1
RUNTIME_DEP_PKGS =
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWpysetuptools
TEST_SCRIPTS =
include gar/category.mk
