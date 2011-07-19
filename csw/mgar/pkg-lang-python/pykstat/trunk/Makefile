# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = pykstat
VERSION = 0.5
CATEGORIES = python
DESCRIPTION = a Python interface to the Solaris kstat(3k) and utmpx APIs
define BLURB
endef
SPKG_SOURCEURL = http://www.biostat.wisc.edu/~annis/creations/pykstat.html
MASTER_SITES = http://www.biostat.wisc.edu/~annis/creations/
DISTNAME = PyKstat-$(VERSION)
PATCHFILES = python-2.6-Makefile.patch
DISTFILES  = $(DISTNAME).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWpy-kstat
CATALOGNAME_CSWpy-kstat = py_kstat
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWswig
BUILD_SCRIPTS = py-kstat
INSTALL_SCRIPTS = py-kstat
TEST_SCRIPTS =
include gar/category.mk

build-py-kstat:
	(cd $(WORKSRC); $(BUILD_ENV) gmake all)
	@$(MAKECOOKIE)

install-py-kstat:
	(cd $(WORKSRC); $(INSTALL_ENV) gmake install)
	@$(MAKECOOKIE)

