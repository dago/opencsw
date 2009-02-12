GARNAME = docutils
GARVERSION = 0.5
CATEGORIES = lang

DESCRIPTION = Documentation Utiltiies for Python
define BLURB
  Documentation Utilities for Python
endef

MASTER_SITES = $(SF_MIRROR)/$(GARNAME)/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWpydocutils
REQUIRED_PKGS_CSWpydocutils = CSWpython
CATALOGNAME_CSWpydocutils = py_docutils
SPKG_DESC = Documentation Utiltiies for Python

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)

include gar/category.mk

post-install:
	install -d $(DESTDIR)$(docdir)
	cp -R $(WORKSRC)/docs $(DESTDIR)$(docdir)/pydocutils
	cp -R $(WORKSRC)/extras $(DESTDIR)$(docdir)/pydocutils
	$(DONADA)

