# $Id$

NAME = setuptools
VERSION = 0.6c11
CATEGORIES = python
GARTYPE = v2

SPKG_SOURCEURL = http://peak.telecommunity.com/DevCenter/setuptools
PYSETUPTOOLS_VERSION := $(shell echo $(VERSION) | sed -e 's/[a-z].*//')
PYSETUPTOOLS_RELEASE := $(shell echo $(VERSION) | sed -e 's/^[0-9].[0-9]*//')

DESCRIPTION = Distribution Utilities for Python
define BLURB
  Distribution Utilities for Python
endef

ARCHALL_CSWpy-setuptools = 1
MASTER_SITES = http://cheeseshop.python.org/packages/source/s/setuptools/
UFILES_REGEX = $(NAME)(\d+(?:\.\d+)*)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += LICENSE
PACKAGES = CSWpy-setuptools
CATALOG_NAME_CSWpy-setuptools = py_setuptools
OBSOLETED_BY_CSWpy-setuptools = CSWpysetuptools
SPKG_DESC_CSWpy-setuptools = Distribution Utiltiies for Python
TEST_SCRIPTS = 
LICENSE = LICENSE

CHECKPKG_OVERRIDES_CSWpysetuptools += surplus-dependency|CSWpython

include gar/category.mk

post-merge:
	@(cd $(PKGROOT)/$(SITE_PACKAGES/setuptools/; \
		rm -rf tests )
	@$(MAKECOOKIE)
