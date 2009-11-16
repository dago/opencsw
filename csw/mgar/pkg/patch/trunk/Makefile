GARNAME = patch
GARVERSION = 2.6
CATEGORIES = utils

DESCRIPTION = GNU patch utility
define BLURB
  The GNU patch utility.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

PACKAGES = CSWgpatch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

INSTALL_OVERRIDE_DIRS = prefix exec_prefix bindir mandir

TEST_TARGET = check

include gar/category.mk
