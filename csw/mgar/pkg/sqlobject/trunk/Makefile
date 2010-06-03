# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = SQLObject
GARVERSION = 0.12.4
CATEGORIES = python
DESCRIPTION = Object Relational Manager for Python
define BLURB
endef
SPKG_SOURCEURL = http://www.sqlobject.org/
MASTER_SITES = http://pypi.python.org/packages/source/S/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE = docs/SQLObject.txt
PACKAGES = CSWpy-sqlobject
RUNTIME_DEP_PKGS_CSWpy-sqlobject = CSWpy-formencode
ARCHALL_CSWpy-sqlobject = 1
CATALOGNAME_CSWpy-sqlobject = py_sqlobject
# To build the dependent package before the dependency is installed on the
# buildfarm.
CHECKPKG_OVERRIDES_CSWpy-sqlobject += unidentified-dependency|CSWpy-formencode
CHECKPKG_OVERRIDES_CSWpy-sqlobject += surplus-dependency|CSWpy-formencode
include gar/category.mk
