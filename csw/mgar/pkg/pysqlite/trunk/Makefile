GARNAME = pysqlite
GARVERSION = 1.1.8a
CATEGORIES = lang

PYSQLITE_VERSION := $(shell echo $(GARVERSION) | sed -e 's/[a-z]//g')
PYSQLITE_RELEASE := $(shell echo $(GARVERSION) | sed -e 's/[^a-z]//g')

DESCRIPTION = SQLite 1.x support for Python
define BLURB
  SQLite support for Python
endef

MASTER_SITES = $(SF_MIRROR)/$(call TOLOWER,$(GARNAME))/
WORKSRC = $(WORKDIR)/$(GARNAME)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWpysqlite
CATALOGNAME_CSWpysqlite = pysqlite
SPKG_DESC_CSWpysqlite = SQLite 1.x support for Python
REQUIRED_PKGS_CSWpysqlite = CSWpython CSWsqlite3

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=54058
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

NOISALIST = 1
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS  = --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include gar/category.mk

SPKG_VERSION := $(PYSQLITE_VERSION)
SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(PYSQLITE_RELEASE)

