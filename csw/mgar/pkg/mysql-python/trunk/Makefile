GARNAME = MySQL-python
GARVERSION = 1.2.2
CATEGORIES = lang

DESCRIPTION = MySQL support for Python
define BLURB
  MySQL support for Python
endef

SF_PROJ = $(call TOLOWER,$(GARNAME))
MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWpymysql
REQUIRED_PKGS_CSWpymysql = CSWmysql5rt CSWpython CSWosslrt CSWzlib
CATALOGNAME_CSWpymysql = pymysql
SPKG_DESC = MySQL Support for Python

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc 
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS += CSWcswclassutils

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS  = --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include gar/category.mk

mysql_prefix = $(prefix)/mysql5
mysql_bindir = $(mysql_prefix)/bin

EXTRA_LD_OPTIONS = -R/opt/csw/mysql5/lib/mysql/\$$ISALIST
PATH       := $(mysql_bindir):$(PATH)
export PATH 

