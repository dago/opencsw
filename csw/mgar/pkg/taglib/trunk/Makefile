GARNAME = taglib
GARVERSION = 1.6.1
CATEGORIES = lib

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://developer.kde.org/~wheeler/files/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = COPYING.MPL

RUNTIME_DEP_PKGS_CSWtaglib += CSWzlib

# UPSTREAM_MASTER_SITES = 

EXTRA_LD_FLAGS += -lCstd -lCrun -lc -lm

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
