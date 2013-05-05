# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pylint
VERSION = 0.28.0
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Python code static checker
define BLURB
endef
VENDOR_URL = http://pypi.python.org/pypi/pylint
MASTER_SITES = $(PYPI_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PACKAGES = CSWpylint
ARCHALL_CSWpylint = 1
# The software name is 'pylint'.
CHECKPKG_OVERRIDES_CSWpylint += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpylint += catalogname-does-not-start-with-py_
RUNTIME_DEP_PKGS_CSWpylint = CSWpy-logilab-astng
CHECKPKG_OVERRIDES_CSWpylint += surplus-dependency|CSWpy-logilab-astng
include gar/category.mk
