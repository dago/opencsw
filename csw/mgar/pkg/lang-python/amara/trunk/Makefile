# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = Amara
VERSION = 2.0a4
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Library for XML processing in Python
define BLURB
endef
SPKG_SOURCEURL = http://pypi.python.org/pypi/Amara
MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE = PKG-INFO
PACKAGES = CSWpy-amara
CATALOGNAME_CSWpy-amara = py_amara
TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)
RUNTIME_DEP_PKGS_CSWpy-amara += CSWlibpython2-6-1-0
EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/python/site-packages/amara/test.*
include gar/category.mk
