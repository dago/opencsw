GARNAME = pysqlite
GARVERSION = 2.0.5
CATEGORIES = lang

DESCRIPTION = SQLite support for Python
define BLURB
  SQLite support for Python
endef

MASTER_SITES = http://initd.org/pub/software/pysqlite/releases/2.0/2.0.5/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpysqlite2,depend prototype)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

INSTALL_ARGS += --root=$(DESTDIR)

include ../category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@( cd $(WORKSRC); $(INSTALL_ENV) python ./setup.py install $(INSTALL_ARGS) )

