NAME = pysqlite
VERSION = 2.5.6
CATEGORIES = lang
GARTYPE = v2

RELVER = $(shell echo $(VERSION) |gsed 's/\(^[0-9].*\)\.[0-9]*/\1/')

DESCRIPTION = SQLite3 support for Python
define BLURB
  SQLite support for Python
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWpysqlite2
RUNTIME_DEP_PKGS_CSWpysqlite2 = CSWpython CSWsqlite3rt
CATALOGNAME_CSWpysqlite2 = pysqlite2
SPKG_DESC_CSWpysqlite2 = SQLite3 support for Python

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc 
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)
INSTALL_ARGS += --prefix=$(prefix)

LICENSE = LICENSE

include gar/category.mk

post-install-modulated:
	install -d $(DESTDIR)$(docdir)
	mv $(DESTDIR)$(prefix)/pysqlite2-doc $(DESTDIR)$(docdir)/pysqlite2
	$(DONADA)

