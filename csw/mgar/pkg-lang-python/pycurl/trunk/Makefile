# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pycurl
VERSION = 7.19.0
CATEGORIES = python
DESCRIPTION = PycURL is a Python interface to libcurl
PACKAGES = CSWpy-curl
CATALOGNAME_CSWpy-curl = py_curl
define BLURB
endef
SPKG_SOURCEURL = http://pycurl.sourceforge.net/
MASTER_SITES = http://pycurl.sourceforge.net/download/
PATCHFILES = remove-static-libs.patch
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
RUNTIME_DEP_PKGS += CSWcurlrt
RUNTIME_DEP_PKGS += CSWlibidn
RUNTIME_DEP_PKGS += CSWoldaprt
RUNTIME_DEP_PKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWzlib
TEST_SCRIPTS =
include gar/category.mk
