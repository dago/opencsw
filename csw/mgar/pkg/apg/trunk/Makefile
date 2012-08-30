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
PATCHFILES += 0002-Do-not-change-owner-and-group.patch

# This is the path to apg
REINPLACE_USRLOCAL += doc/man/apg.1

# There is no configure
CONFIGURE_SCRIPTS =

# We want to build both standalone and client/server
BUILD_ARGS = all

# There is no testsuite
TEST_SCRIPTS =

INSTALL_OVERRIDE_VARS += INSTALL_PREFIX
INSTALL_OVERRIDE_VAR_INSTALL_PREFIX = $(DESTDIR)$(prefix)

INSTALL_OVERRIDE_VARS += APG_MAN_DIR
INSTALL_OVERRIDE_VAR_APG_MAN_DIR = /share/man/man1

INSTALL_OVERRIDE_VARS += APGD_MAN_DIR
INSTALL_OVERRIDE_VAR_APGD_MAN_DIR = /share/man/man8

include gar/category.mk
