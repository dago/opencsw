# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = virtualenv
VERSION = 1.8.2
PACKAGES = CSWpy-virtualenv
CATALOGNAME_CSWpy-virtualenv = py_virtualenv
CATEGORIES = python
GARTYPE = v2
SPKG_DESC_CSWpy-virtualenv = Virtual Python Environment builder
ARCHALL_CSWpy-virtualenv = 1
define BLURB
endef
SPKG_SOURCEURL = http://pypi.python.org/pypi/virtualenv
MASTER_SITES = http://pypi.python.org/packages/source/v/virtualenv/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = PKG-INFO
# /usr/share references are fine, these are docstrings.
CHECKPKG_OVERRIDES_CSWpy-virtualenv += file-with-bad-content
include gar/category.mk
