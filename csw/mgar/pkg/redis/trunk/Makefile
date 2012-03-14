# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = redis
VERSION = 2.4.8
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = An advanced key-value store
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-backtrace-is-only-available-on-Solaris-11.patch

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWredis
SPKG_DESC_CSWredis = An advanced key-value store
# PKGFILES is catchall

GARCOMPILER = GCC4

# These are set in the Makefile and are not inherited when we force our CFLAGS in
EXTRA_CFLAGS += -std=c99 -pedantic -Wall -W -D__EXTENSIONS__ -D_XPG6

# There is no configure
CONFIGURE_SCRIPTS =

BUILD_ARGS += V=1

TEST_TARGET = test

# We need TCL 8.5 for this which we don't have yet
SKIPTEST ?= 1

INSTALL_OVERRIDE_VARS += PREFIX
INSTALL_OVERRIDE_VAR_PREFIX = $(DESTDIR)$(prefix)

include gar/category.mk

