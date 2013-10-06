# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = virtualenv
VERSION = 1.10.1
CATEGORIES = python
GARTYPE = v2
SPKG_DESC_CSWpy-virtualenv = Virtual Python Environment builder
ARCHALL_CSWpy-virtualenv = 1

define BLURB
A tool to create isolated Python environments.
endef

PACKAGES = CSWpy-virtualenv
VENDOR_URL = http://pypi.python.org/pypi/virtualenv
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = PKG-INFO
BUILD_DEP_PKGS += CSWpy-mock
DEP_PKGS = CSWpython-dev
# /usr/share references are fine, these are docstrings.
CHECKPKG_OVERRIDES_CSWpy-virtualenv += file-with-bad-content
CHECKPKG_OVERRIDES_CSWpy-virtualenv += surplus-dependency|CSWpython-dev
include gar/category.mk
