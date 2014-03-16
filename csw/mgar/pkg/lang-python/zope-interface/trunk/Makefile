# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = zope.interface
VERSION = 4.1.0
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Implementation of object interfaces in Python
define BLURB
endef

MASTER_SITES += $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://pypi.python.org/pypi/zope.interface
LICENSE = LICENSE.txt

PACKAGES = CSWpy-zope-interface
SPKG_DESC_CSWpy-zope-interface = Implementation of object interfaces in Python
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpy-zope-interface += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-zope-interface += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-zope-interface += CSWlibgcc-s1

# For the Python 2.7 modulation the wrong Python is chosen
SKIPTEST ?= 1

include gar/category.mk
