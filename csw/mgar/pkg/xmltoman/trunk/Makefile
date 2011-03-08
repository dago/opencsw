# $Id$
NAME = xmltoman
VERSION = 0.4
CATEGORIES = utils

DESCRIPTION = A man page creation tool
define BLURB

endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz
PATCHFILES += 0001-Override-default-hard-coded-prefix-with-opt-csw.patch
PATCHFILES += 0002-Use-CSW-perl-instead-of-system-perl.patch
PATCHFILES += 0003-Use-ginstall-not-system-install.patch

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

include gar/category.mk
