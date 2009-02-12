GARNAME = MySQL-python
GARVERSION = 1.2.2
CATEGORIES = lang

DESCRIPTION = MySQL support for Python
define BLURB
  MySQL support for Python
endef

MASTER_SITES = $(SF_MIRROR)/$(call TOLOWER,$(GARNAME))/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWpymysql
REQUIRED_PKGS_CSWpymysql = CSWmysql5rt CSWpython CSWosslrt CSWzlib
CATALOGNAME_CSWpymysql = py_mysql5
SPKG_DESC = MySQL Support for Python

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=22307
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS  = --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include gar/category.mk

mysql_prefix = $(prefix)/mysql5
mysql_bindir = $(mysql_prefix)/bin

LD_OPTIONS := -R/opt/csw/mysql5/lib/mysql/\$$ISALIST $(LD_OPTIONS)
PATH       := $(mysql_bindir):$(PATH)
export LD_OPTIONS PATH

