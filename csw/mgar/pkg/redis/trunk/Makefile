# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = redis
VERSION = 2.8.3

DESCRIPTION = An advanced key-value store

MASTER_SITES = http://download.redis.io/releases/
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWredis
SPKG_DESC_CSWredis = An advanced key-value store

BUILD64 = 1
ISAEXEC = 1

GARCOMPILER = GNU

PATCHFILES += 0001-Fix-tclsh-finding.patch

PATCHFILES += 0001-Solaris-needs-lrt-for-nanosleep.patch

GARCOMPILER = GCC4

# These are set in the Makefile and are not inherited when we force our CFLAGS in
EXTRA_CFLAGS += -std=c99 -pedantic -Wall -W -D__EXTENSIONS__ -D_XPG6

# There is no configure
CONFIGURE_SCRIPTS =

BUILD_ARGS += V=1

# Some tests fail
SKIPTEST ?= 1

INSTALL_OVERRIDE_VARS += PREFIX
INSTALL_OVERRIDE_VAR_PREFIX = $(DESTDIR)$(prefix)
INSTALL_OVERRIDE_VARS += INSTALL_BIN
INSTALL_OVERRIDE_VAR_INSTALL_BIN = $(DESTDIR)$(bindir)

# This is for tail taking -n namely gtail for us
TEST_ENV_PATH = $(prefix)/gnu:$(PATH)

include gar/category.mk

