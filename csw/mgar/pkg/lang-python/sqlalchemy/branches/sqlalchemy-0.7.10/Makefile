# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# There are failing unit tests; the issue is submitted upstream:
# http://www.sqlalchemy.org/trac/ticket/1837

NAME = SQLAlchemy
VERSION = 0.7.10
CATEGORIES = python

DISTNAME = $(NAME)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.sqlalchemy.org/
LICENSE = LICENSE

PACKAGES += CSWpy-sqlalchemy
SPKG_DESC_CSWpy-sqlalchemy = Python SQL toolkit and Object Relational Mapper
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpy-sqlalchemy += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpy-sqlalchemy += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-sqlalchemy += CSWlibpython2-7-1-0

include gar/category.mk
