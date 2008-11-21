GARNAME = MySQL-python
GARVERSION = 1.2.2
CATEGORIES = lang

DESCRIPTION = MySQL support for Python
define BLURB
  MySQL support for Python
endef

MASTER_SITES = $(SF_MIRROR)/$(call TOLOWER,$(GARNAME))/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWpymysql,depend prototype)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS  = --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include ../category.mk

mysql_prefix = $(prefix)/mysql5
mysql_bindir = $(mysql_prefix)/bin

LD_OPTIONS := -R/opt/csw/mysql5/lib/mysql/\$$ISALIST $(LD_OPTIONS)
PATH       := $(mysql_bindir):$(PATH)
export LD_OPTIONS PATH

