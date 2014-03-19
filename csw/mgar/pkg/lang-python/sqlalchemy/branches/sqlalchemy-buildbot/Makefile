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

# Buildbot is 2.7 only
MODULATIONS_PYTHON_VERSION = 2_7

PACKAGES += CSWbuildbot-sqlalchemy
SPKG_DESC_CSWbuildbot-sqlalchemy = Python SQL toolkit and Object Relational Mapper, private Buildbot version
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWbuildbot-sqlalchemy += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWbuildbot-sqlalchemy += CSWlibpython2-7-1-0

# Yes, this is intended
CHECKPKG_OVERRIDES_CSWbuildbot-sqlalchemy += discouraged-path-in-pkgmap

prefix = $(BUILD_PREFIX)/share/buildbot

include gar/category.mk
