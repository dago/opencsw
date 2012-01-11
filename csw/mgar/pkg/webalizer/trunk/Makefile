# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = webalizer
VERSION = 2.23
SUBREV = 05
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = A flexible web server log file analysis program
define BLURB
endef

MASTER_SITES = ftp://ftp.mrunix.net/pub/webalizer/
DISTNAME = $(NAME)-$(VERSION)-$(SUBREV)
DISTFILES += $(DISTNAME)-src.tgz

PATCHFILES += 0001-Force-void-context.patch

PACKAGES += CSWwebalizer
SPKG_DESC_CSWwebalizer = A flexible web server log file analysis program
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWwebalizer += CSWlibgd2
RUNTIME_DEP_PKGS_CSWwebalizer += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWwebalizer += CSWlibz1

#EXTRA_INC = $(prefix)/bdb48/include
#EXTRA_LIB = $(prefix)/bdb48/lib

CONFIGURE_ARGS = $(DIRPATHS)

# There is no testsuite
TEST_SCRIPTS =

MIGRATE_FILES += webalizer.conf
PRESERVECONF += $(sysconfdir)/webalizer.conf

EXTRA_PAX_ARGS += -s ',/webalizer\.conf\.sample$$,/webalizer.conf.CSW,'

include gar/category.mk

