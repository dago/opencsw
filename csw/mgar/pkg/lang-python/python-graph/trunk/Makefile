# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = python-graph
VERSION = 1.7.0
CATEGORIES = python
DESCRIPTION = A library for working with graphs in Python
define BLURB
endef
SPKG_SOURCEURL = http://pypi.python.org/pypi/python-graph
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2
PACKAGES = CSWpy-graph
CATALOGNAME_CSWpy-graph = py_graph
BUILD_SCRIPTS =
# INSTALL_SCRIPTS = python-graph
TEST_SCRIPTS =
BUILD_SCRIPTS ?= $(WORKSRC)/core/setup.py
INSTALL_SCRIPTS ?= $(WORKSRC)/core/setup.py

ARCHALL_CSWpy-graph = 1

include gar/category.mk
