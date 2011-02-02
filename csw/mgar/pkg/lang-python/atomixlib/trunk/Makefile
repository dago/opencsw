# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = atomixlib
VERSION = 0.6.1a
CATEGORIES = python
DESCRIPTION = A module to generate Atom 1.0 documents through a simple API
define BLURB
endef
SPKG_SOURCEURL = http://pypi.python.org/pypi/atomixlib
MASTER_SITES = http://www.defuze.org/oss/atomixlib/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE = PKG-INFO
PACKAGES = CSWpy-atomixlib
CATALOGNAME_CSWpy-atomixlib = py_atomixlib
DEP_PKGS = CSWpy-amara
CONFIGURE_ARGS = $(DIRPATHS)
ARCHALL_CSWpy-atomixlib = 1
CHECKPKG_OVERRIDES_CSWpy-atomixlib += surplus-dependency|CSWpy-amara
include gar/category.mk
