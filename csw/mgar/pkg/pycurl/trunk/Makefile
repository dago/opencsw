# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = pycurl
GARVERSION = 7.19.0
CATEGORIES = python
DESCRIPTION = PycURL is a Python interface to libcurl
PACKAGES = CSWpy-curl
CATALOGNAME_CSWpy-curl = py_curl
define BLURB
endef
SPKG_SOURCEURL = http://pycurl.sourceforge.net/
MASTER_SITES = http://pycurl.sourceforge.net/download/
PATCHFILES = remove-static-libs.patch
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
REQUIRED_PKGS += CSWcurlrt
REQUIRED_PKGS += CSWlibidn
REQUIRED_PKGS += CSWoldaprt
REQUIRED_PKGS += CSWosslrt
REQUIRED_PKGS += CSWzlib
TEST_SCRIPTS =
include gar/category.mk
