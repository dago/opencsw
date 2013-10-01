# $Id$

NAME = setuptools
VERSION = 1.1.6
CATEGORIES = python
GARTYPE = v2

VENDOR_URL = https://pypi.python.org/pypi/setuptools
PYSETUPTOOLS_VERSION := $(shell echo $(VERSION) | sed -e 's/[a-z].*//')
PYSETUPTOOLS_RELEASE := $(shell echo $(VERSION) | sed -e 's/^[0-9].[0-9]*//')

DESCRIPTION = Distribution Utilities for Python
define BLURB
  Distribution Utilities for Python
endef

ARCHALL_CSWpy-setuptools = 1
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += LICENSE
OBSOLETED_BY_CSWpy-setuptools = CSWpysetuptools
SPKG_DESC_CSWpy-setuptools = Distribution Utiltiies for Python
TEST_SCRIPTS =
LICENSE = LICENSE

include gar/category.mk

post-merge:
	@(cd $(PKGROOT)/$(SITE_PACKAGES)/setuptools/; \
		rm -rf tests )
	@$(MAKECOOKIE)
