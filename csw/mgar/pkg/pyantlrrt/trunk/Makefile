# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = py_antlr
GARVERSION = 3.1.1
CATEGORIES = python

DESCRIPTION = Python ANTLR runtime
define BLURB
  Python ANTLR runtime, needed for Python ANTLR-generated parsers to run.
endef

MASTER_SITES = http://www.antlr.org/download/Python/
DISTFILES  = antlr_python_runtime-$(GARVERSION).tar.gz

WORKSRC = $(WORKDIR)/antlr_python_runtime-$(GARVERSION)

PACKAGES = CSWpy-antlr
CATALOGNAME = py_antlr
PREREQUISITE_PKGS = CSWpysetuptools

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL = 1

# BUILD_SCRIPTS = $(WORKSRC)/setup.py

# INSTALL_SCRIPTS = $(WORKSRC)/setup.py
# INSTALL_ARGS += --root=$(DESTDIR) --prefix=$(prefix)

TEST_SCRIPTS =

include gar/category.mk

post-install:
	gfind $(DESTDIR) -type f -name '*.pyc' -exec rm {} \;
	@$(MAKECOOKIE)
