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

PATCHFILES += 0001-Solaris-package-mge-does-not-handle-spaces.patch

ARCHALL_CSWpy-setuptools = 1
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += LICENSE
OBSOLETED_BY_CSWpy-setuptools = CSWpysetuptools
SPKG_DESC_CSWpy-setuptools = Distribution Utiltiies for Python
TEST_SCRIPTS =
LICENSE = LICENSE

CHECKPKG_OVERRIDES_CSWpy-setuptools += file-with-bad-content

include gar/category.mk

post-install-modulated:
	mv "$(DESTDIR)$(SITE_PACKAGES)/setuptools/script template.py" \
		 "$(DESTDIR)$(SITE_PACKAGES)/setuptools/script_template.py"
	mv "$(DESTDIR)$(SITE_PACKAGES)/setuptools/script template (dev).py" \
		 "$(DESTDIR)$(SITE_PACKAGES)/setuptools/script_template_(dev).py"
	@$(MAKECOOKIE)

post-merge:
	@(cd $(PKGROOT)/$(SITE_PACKAGES)/setuptools/; \
		rm -rf tests )
	@$(MAKECOOKIE)
