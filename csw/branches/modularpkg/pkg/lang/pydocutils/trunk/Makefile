GARNAME = docutils
GARVERSION = 0.4
CATEGORIES = lang

DESCRIPTION = Documentation Utiltiies for Python
define BLURB
  Documentation Utilities for Python
endef

MASTER_SITES = $(SF_MIRROR)/$(GARNAME)/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpydocutils,depend prototype)

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

