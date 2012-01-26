# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# There are failing unit tests; the issue is submitted upstream:
# http://www.sqlalchemy.org/trac/ticket/1837

NAME = sqlalchemy
VERSION = 0.6.1
CATEGORIES = python
GARTYPE = v2
PACKAGES = CSWpy-sqlalchemy
CATALOGNAME_CSWpy-sqlalchemy = py_sqlalchemy
DESCRIPTION = Python SQL toolkit and Object Relational Mapper
define BLURB
endef
SPKG_SOURCEURL = http://www.sqlalchemy.org/
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = SQLAlchemy-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
ARCHALL_CSWpy-sqlalchemy = 1
LICENSE = LICENSE
include gar/category.mk
