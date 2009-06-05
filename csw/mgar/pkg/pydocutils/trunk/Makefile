GARNAME = docutils
GARVERSION = 0.5
CATEGORIES = lang

DESCRIPTION = Documentation Utiltiies for Python
define BLURB
  Documentation Utilities for Python
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWpydocutils
REQUIRED_PKGS_CSWpydocutils = CSWpython
CATALOGNAME_CSWpydocutils = pydocutils
SPKG_DESC = Documentation Utiltiies for Python

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc 
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS += CSWcswclassutils


# We define upstream file regex so we can be notifed of 
# new upstream software release
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

