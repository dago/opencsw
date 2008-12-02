GARNAME = setuptools
GARVERSION = 0.6c7
CATEGORIES = lang

SPKG_SOURCEURL = http://peak.telecommunity.com/DevCenter/setuptools

DESCRIPTION = Distribution Utiltiies for Python
define BLURB
  Distribution Utilities for Python
endef

MASTER_SITES = http://cheeseshop.python.org/packages/source/s/setuptools/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpysetuptools,depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Use versionless python lib
PATCHFILES += pyversion.diff

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include gar/category.mk

PYTHONPATH = $(DESTDIR)$(libdir)/python/site-packages/
export PYTHONPATH

pre-install:
	install -d $(PYTHONPATH)
	$(DONADA)

