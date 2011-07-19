# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pylint
VERSION = 0.21.3
CATEGORIES = python
DESCRIPTION = Python code static checker
define BLURB
endef
SPKG_SOURCEURL = http://pypi.python.org/pypi/pylint
MASTER_SITES = http://pypi.python.org/packages/source/p/pylint/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
ARCHALL_CSWpylint = 1
EXTRA_MERGE_EXCLUDE_FILES = .*\.pyc
# The software name is 'pylint'.
CHECKPKG_OVERRIDES_CSWpylint += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWpylint += catalogname-does-not-start-with-py_
RUNTIME_DEP_PKGS_CSWpylint = CSWpy-logilab-astng
CHECKPKG_OVERRIDES_CSWpylint += surplus-dependency|CSWpy-logilab-astng
include gar/category.mk
