# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
# ! Installation needs to be relocated to DESTDIR by using INSTALL_OVERRIDE_VARS
# ! Linkage of libedit.so needs a SONAME, probably libedit.so.1
# ! Package creation is missing

NAME = libedit
VERSION = 0.3
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Non-GPL replacement for readline library
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTNAME = libedit
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Add-definition-for-sig_t.patch

BUILD64_LIBS_ONLY = 1

# The vis.h is completely different what libedit expects
EXTRA_CONFIGURE_ENV += ac_cv_header_vis_h=no

EXTRA_CFLAGS += $(CPPFLAGS)
EXTRA_INC += $(includedir)/ncurses

CONFIGURE_ARGS += $(DIRPATHS)

TEST_TARGET = TEST
TEST_OVERRIDE_VARS = LDADD
TEST_OVERRIDE_VAR_LDADD = $(LDFLAGS)

include gar/category.mk

