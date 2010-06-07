GARNAME = namebench
GARVERSION = 1.3
CATEGORIES = python

DESCRIPTION = DNS benchmark utility
define BLURB
  DNS benchmark utility
endef

MASTER_SITES = http://namebench.googlecode.com/files/
DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tgz

SPKG_SOURCEURL = http://code.google.com/p/namebench

RUNTIME_DEP_PKGS = CSWpython-tk

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

ARCHALL = 1

TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWnamebench += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWnamebench += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWnamebench += surplus-dependency|CSWpython-tk

include gar/category.mk
