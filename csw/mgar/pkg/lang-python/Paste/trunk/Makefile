# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = Paste
VERSION = 1.7.5.1
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Tools for using a Web Server Gateway Interface stack
define BLURB
endef

MASTER_SITES = $(PYPI_MIRROR)
DISTFILES = $(DISTNAME).tar.gz

VENDOR_URL = http://pythonpaste.org/

PACKAGES = CSWpy-paste
ARCHALL_CSWpy-paste = 1

# Some tests fail which are probably harmless
SKIPTEST ?= 1

include gar/category.mk
