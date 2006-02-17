GARNAME = pysqlite
GARVERSION = 1.0
CATEGORIES = lang

DESCRIPTION = SQLite support for Python
define BLURB
  SQLite support for Python
endef

MASTER_SITES = $(SF_MIRROR)/$(call TOLOWER,$(GARNAME))/
WORKSRC = $(WORKDIR)/$(GARNAME)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWpysqlite.gspec

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS  = --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include ../category.mk

