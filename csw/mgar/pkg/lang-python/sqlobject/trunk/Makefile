# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = SQLObject
VERSION = 0.15.0
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Object Relational Manager for Python
define BLURB
endef
SPKG_SOURCEURL = http://www.sqlobject.org/
MASTER_SITES = http://pypi.python.org/packages/source/S/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
LICENSE = docs/SQLObject.txt
PACKAGES = CSWpy-sqlobject
RUNTIME_DEP_PKGS_CSWpy-sqlobject = CSWpy-formencode
ARCHALL_CSWpy-sqlobject = 1
CATALOGNAME_CSWpy-sqlobject = py_sqlobject
CHECKPKG_OVERRIDES_CSWpy-sqlobject += surplus-dependency|CSWpy-formencode
include gar/category.mk
