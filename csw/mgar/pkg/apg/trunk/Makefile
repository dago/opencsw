NAME = apg
VERSION = 2.2.3
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Automated Password Generator
define BLURB
endef

MASTER_SITES = http://www.adel.nursat.kz/apg/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Fix-Makefile-for-Solaris-use.patch

# There is no configure
CONFIGURE_SCRIPTS =

# There is no testsuite
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS += INSTALL_PREFIX
INSTALL_OVERRIDE_VAR_INSTALL_PREFIX = $(DESTDIR)$(prefix)

include gar/category.mk
