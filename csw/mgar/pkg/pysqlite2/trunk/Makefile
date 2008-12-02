GARNAME = pysqlite
GARVERSION = 2.3.5
CATEGORIES = lang

DESCRIPTION = SQLite3 support for Python
define BLURB
  SQLite support for Python
endef

MASTER_SITES = http://initd.org/pub/software/pysqlite/releases/2.3/2.3.5/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpysqlite2,depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

include gar/category.mk

post-install:
	install -d $(DESTDIR)$(docdir)
	mv $(DESTDIR)$(prefix)/pysqlite2-doc $(DESTDIR)$(docdir)/pysqlite2
	$(DONADA)

