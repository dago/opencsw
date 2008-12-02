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

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS  = --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include gar/category.mk

