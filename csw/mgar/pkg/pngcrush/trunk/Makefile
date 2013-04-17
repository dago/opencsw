# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pngcrush
VERSION = 1.7.58
GARTYPE = v2

DESCRIPTION = An optimizer for PNG (Portable Network Graphics) files

SF_PROJECT = pmt
MASTER_SITES = $(SF_MIRROR)
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += COPYING

VENDOR_URL = http://pmt.sourceforge.net/pngcrush/index.html

BUILD64 = 1
ISAEXEC = 1

# There is no configure
CONFIGURE_SCRIPTS =

BUILD_OVERRIDE_VARS += CC
BUILD_OVERRIDE_VAR_CC = $(CC)
BUILD_OVERRIDE_VARS += LD
BUILD_OVERRIDE_VAR_LD = $(CC)
BUILD_OVERRIDE_VARS += CFLAGS
BUILD_OVERRIDE_VAR_CFLAGS = $(CFLAGS)
BUILD_OVERRIDE_VARS += LDFLAGS
BUILD_OVERRIDE_VAR_LDFLAGS = $(LDFLAGS)

BUILD_OVERRIDE_VARS += PNGINC
BUILD_OVERRIDE_VAR_PNGINC = $(includedir)
BUILD_OVERRIDE_VARS += PNGLIB
BUILD_OVERRIDE_VAR_PNGLIB = $(libdir)
BUILD_OVERRIDE_VARS += ZINC
BUILD_OVERRIDE_VAR_ZINC = $(includedir)
BUILD_OVERRIDE_VARS += ZLIB
BUILD_OVERRIDE_VAR_ZLIB = $(libdir)

BUILD_ARGS += -f Makefile-nolib

# There is no testsuite
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)	
	ginstall -m 0755 $(WORKSRC)/pngcrush $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(sharedstatedir)$(NAME)
	ginstall -m 0644 $(WORKSRC)/ChangeLog.html $(DESTDIR)$(sharedstatedir)$(NAME)
	@$(MAKECOOKIE)

