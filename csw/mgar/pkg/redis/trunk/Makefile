# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = redis
VERSION = 2.6.9

DESCRIPTION = An advanced key-value storee
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-backtrace-is-only-available-on-Solalaris10-i386

PACKAGES += CSWredis
SPKG_DESC_CSWredis = An advan
BUILD64 = 1
ISAEXEC = 1

GARCOMPILER = GNU

GARCOMPILER = GCC4

# These are set in the Makefile and are not inherited when we force our CFLAGS in
EXTRA_CFLAGS += -std=c99 -pedantic -Wall -W -D__EXTENSIONS__ -D_XPG6

# There is no configure
CONFIGURE_SCRIPTS =

BUILD_ARGS += V=1

INSTALL_OVERRIDE_VARS += PREFIX
INSTALL_OVERRIDE_VAR_PREFIX = $(DESTDIR)$(prefix)

# This is for tail taking -n namely gtail for us
TEST_ENV_PATH = $(prefix)/gnu:$(PATH)

include gar/category.mk

