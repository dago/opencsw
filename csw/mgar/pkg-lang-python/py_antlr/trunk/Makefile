# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = py_antlr
VERSION = 3.1.1
CATEGORIES = python

DESCRIPTION = Python ANTLR runtime
define BLURB
  Python ANTLR runtime, needed for Python ANTLR-generated parsers to run.
endef

MASTER_SITES = http://www.antlr.org/download/Python/
DISTFILES  = antlr_python_runtime-$(VERSION).tar.gz

WORKSRC = $(WORKDIR)/antlr_python_runtime-$(VERSION)

PACKAGES = CSWpy-antlr
CATALOGNAME = py_antlr
BUILD_DEP_PKGS = CSWpysetuptools

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1

# BUILD_SCRIPTS = $(WORKSRC)/setup.py

# INSTALL_SCRIPTS = $(WORKSRC)/setup.py
# INSTALL_ARGS += --root=$(DESTDIR) --prefix=$(prefix)

TEST_SCRIPTS =

include gar/category.mk

post-install:
	gfind $(DESTDIR) -type f -name '*.pyc' -exec rm {} \;
	@$(MAKECOOKIE)
