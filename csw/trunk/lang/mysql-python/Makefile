GARNAME = MySQL-python
GARVERSION = 1.2.0
CATEGORIES = lang

DESCRIPTION = MySQL support for Python
define BLURB
  MySQL support for Python
endef

MASTER_SITES = $(SF_MIRROR)/$(call TOLOWER,$(GARNAME))/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES   += $(call admfiles,CSWpymysql,depend prototype)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = pymodule
INSTALL_SCRIPTS = pymodule

# No test suite (tsk, tsk)
ENABLE_TEST = 0

include ../category.mk

mysql_prefix = $(prefix)/mysql4
mysql_bindir = $(mysql_prefix)/bin

LD_OPTIONS := -R/opt/csw/mysql4/lib/mysql/\$$ISALIST $(LD_OPTIONS)
PATH       := $(mysql_bindir):$(PATH)
export LD_OPTIONS PATH

build-pymodule:
	@echo " ==> Running custom install for $(GARNAME)"
	@( cd $(WORKSRC) ; $(BUILD_ENV) \
		python setup.py build )

install-pymodule:
	@echo " ==> Running custom install for $(GARNAME)"
	@( cd $(WORKSRC) ; $(INSTALL_ENV) \
		python setup.py install --prefix=$(DESTDIR)$(prefix) )
