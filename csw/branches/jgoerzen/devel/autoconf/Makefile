GARNAME = autoconf
GARVERSION = 2.58
CATEGORIES = devel

DESCRIPTION = M4 macros to produce scripts to configure sourcecode.
define BLURB
  Autoconf is an extensible package of m4 macros that produce shell scripts to
  automatically configure software source code packages. These scripts can adapt
  the package to many kinds of UNIX-like systems without manual user
  intervention.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

DEPENDS = utils/sed utils/sh-utils

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Tests take a loooooonnng time.
ENABLE_TEST = 0

include ../category.mk
