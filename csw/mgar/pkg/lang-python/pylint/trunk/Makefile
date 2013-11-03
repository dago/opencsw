# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pylint
VERSION = 1.0.0
CATEGORIES = python
GARTYPE = v2
DESCRIPTION = Python code static checker
VENDOR_URL = http://pypi.python.org/pypi/pylint
DISTFILES  = $(NAME)-$(VERSION).tar.gz
# The software name is 'pylint'.
PACKAGES = CSWpylint
ARCHALL_CSWpylint = 1

DEP_PKGS_CSWpylint = CSWpy-astroid
CHECKPKG_OVERRIDES_CSWpylint += surplus-dependency|CSWpy-astroid

CHECKPKG_OVERRIDES_CSWpylint += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpylint += catalogname-does-not-start-with-py_

include gar/category.mk
