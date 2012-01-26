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

ARCHALL_CSWpysetuptools = 1
MASTER_SITES = http://cheeseshop.python.org/packages/source/s/setuptools/
UFILES_REGEX = $(NAME)(\d+(?:\.\d+)*)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += LICENSE
PACKAGES = CSWpysetuptools
CATALOGNAME_CSWpysetuptools = pysetuptools
SPKG_DESC_CSWpysetuptools = Distribution Utiltiies for Python
TEST_SCRIPTS = 
LICENSE = LICENSE
include gar/category.mk
