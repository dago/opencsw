GARNAME = namebench
GARVERSION = 1.2
CATEGORIES = python

DESCRIPTION = DNS benchmark utility
define BLURB
  DNS benchmark utility
endef

MASTER_SITES = http://namebench.googlecode.com/files/
DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tgz

RUNTIME_DEP_PKGS = CSWpython-tk

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

ARCHALL = 1

TEST_SCRIPTS =

include gar/category.mk
