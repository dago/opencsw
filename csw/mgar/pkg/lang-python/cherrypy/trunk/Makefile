# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = cherrypy
VERSION = 3.2.2
CATEGORIES = python

DESCRIPTION = A pythonic, object-oriented web framework
define BLURB
endef

MASTER_SITES = http://download.cherrypy.org/cherrypy/$(VERSION)/
DISTNAME = CherryPy-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

VENDOR_URL = http://cherrypy.org/

PACKAGES = CSWcherrypy
SPKG_DESC_CSWcherrypy = A pythonic, object-oriented web framework
ARCHALL_CSWcherrypy = 1
# The package name is ok as this is also a daemon and well known under that name
CHECKPKG_OVERRIDES_CSWcherrypy += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWcherrypy += catalogname-does-not-start-with-py_

include gar/category.mk
