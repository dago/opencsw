GARNAME = patch
GARVERSION = 2.5.4
CATEGORIES = utils

DESCRIPTION = GNU patch utility
define BLURB
	The GNU patch utility.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_OVERRIDE_DIRS = prefix exec_prefix bindir mandir

TEST_TARGET = check

include ../category.mk
