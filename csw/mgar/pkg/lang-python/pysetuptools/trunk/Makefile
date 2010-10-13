# $Id$

GARNAME = setuptools
GARVERSION = 0.6c11
CATEGORIES = python

SPKG_SOURCEURL = http://peak.telecommunity.com/DevCenter/setuptools
PYSETUPTOOLS_VERSION := $(shell echo $(GARVERSION) | sed -e 's/[a-z].*//')
PYSETUPTOOLS_RELEASE := $(shell echo $(GARVERSION) | sed -e 's/^[0-9].[0-9]*//')

DESCRIPTION = Distribution Utilities for Python
define BLURB
  Distribution Utilities for Python
endef

ARCHALL_CSWpysetuptools = 1
MASTER_SITES = http://cheeseshop.python.org/packages/source/s/setuptools/
UFILES_REGEX = $(GARNAME)(\d+(?:\.\d+)*)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += LICENSE
PACKAGES = CSWpysetuptools
CATALOGNAME_CSWpysetuptools = pysetuptools
SPKG_DESC_CSWpysetuptools = Distribution Utiltiies for Python
TEST_SCRIPTS = 
LICENSE = LICENSE
include gar/category.mk
