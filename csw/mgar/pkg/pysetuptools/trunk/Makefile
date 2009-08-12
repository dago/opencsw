GARNAME = setuptools
GARVERSION = 0.6c9
CATEGORIES = lang

SPKG_SOURCEURL = http://peak.telecommunity.com/DevCenter/setuptools
PYSETUPTOOLS_VERSION := $(shell echo $(GARVERSION) | sed -e 's/[a-z].*//')
PYSETUPTOOLS_RELEASE := $(shell echo $(GARVERSION) | sed -e 's/^[0-9].[0-9]*//')

DESCRIPTION = Distribution Utiltiies for Python
define BLURB
  Distribution Utilities for Python
endef

ARCHALL_CSWpysetuptools = 1
MASTER_SITES = http://cheeseshop.python.org/packages/source/s/setuptools/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

REQUIRED_PKGS_CSWpysetuptools = CSWpython CSWpydistutils
PACKAGES = CSWpysetuptools
CATALOGNAME_CSWpysetuptools = pysetuptools
SPKG_DESC_CSWpysetuptools = Distribution Utiltiies for Python

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc .*\.exe
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile 
REQUIRED_PKGS += CSWcswclassutils

ENABLE_CHECK = 0

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)(\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = skip
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

test-skip:
	$(DONADA)

INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include gar/category.mk

SPKG_VERSION := $(PYSETUPTOOLS_VERSION)
SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(PYSETUPTOOLS_RELEASE)

