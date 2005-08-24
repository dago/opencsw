GARNAME = pysqlite
GARVERSION = 1.0
CATEGORIES = lang

DESCRIPTION = SQLite support for Python
define BLURB
  SQLite support for Python
endef

MASTER_SITES = $(SF_MIRROR)/$(call TOLOWER,$(GARNAME))/
WORKSRC = $(WORKDIR)/$(GARNAME)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWpysqlite.gspec

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = pymodule
INSTALL_SCRIPTS = pymodule

# No test target
ENABLE_TEST = 0

include ../category.mk

build-pymodule:
	@echo " ==> Running custom install for $(GARNAME)"
	@( cd $(WORKSRC) ; $(BUILD_ENV) python setup.py build )

install-pymodule:
	@echo " ==> Running custom install for $(GARNAME)"
	@( cd $(WORKSRC) ; \
		python setup.py install --prefix=$(DESTDIR)$(prefix) )
