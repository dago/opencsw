# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = pyantlrrt
GARVERSION = 3.1.1
CATEGORIES = lib

DESCRIPTION = Python ANTLR runtime
define BLURB
  Python ANTLR runtime, needed for Python ANTLR-generated parsers to run.
endef

MASTER_SITES = http://www.antlr.org/download/Python/
DISTFILES  = antlr_python_runtime-$(GARVERSION).tar.gz

WORKSRC = $(WORKDIR)/antlr_python_runtime-$(GARVERSION)

REQUIRED_PKGS = CSWcswclassutils CSWpython CSWpython-rt

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_CLASSES = none cswpycompile
ARCHALL = 1

PROTOTYPE_FILTER = awk ' \
  $$$$3 ~/.*\.py$$$$/ { $$$$2 = "pycompile" } \
  { print }'

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS += --root=$(DESTDIR) --prefix=$(prefix)

TEST_SCRIPTS =

post-install-modulated:
	gfind $(DESTDIR) -type f -name '*.pyc' -exec rm {} \;
	@$(MAKECOOKIE)

include gar/category.mk
