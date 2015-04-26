# $Id$
NAME = getopt
VERSION = 1.1.5
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Help shell scripts parse command-line parameters
define BLURB
endef

# TBD:
# - The existing package uses ggetopt instead of getopt everywhere
# - The existing package is linked against CSWggettext and CSWlibiconv

MASTER_SITES = http://software.frodo.looijaard.name/getopt/files/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Include-locale.h-when-usi#PATCHFILES += 0002-Do-not-make-standalone-version.patch
#ne-version.patch
PATCHFILES += 0003-Makefile-settings.patch

# Patch from http://lists.gnu.org/archive/html/bug-bison/2010-04/msg00046.html
PATCHFILES += 0004-Sanitize-getopt.h.patch

PACKAGES = CSWggetopt
CATALOGNAME = ggetopt

VENDOR_URL = http://software.frodo.looijaa#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
aard.name/getopt/

EXTRA_CFLAGS += -Xc

# No scipt there...
CONFIGURE_SCRIPTS =

BUILD_OVERRIDE_VARS = prefix CC CFLAGS LIBCGETOPT PACKAGE
BUILD_OVERRIDE_VAR_prefix = $(prefix)
BUILD_OVERRIDE_VAR_CC = $(CC)
BUILD_OVERRIDE_VAR_CFLAGS = $(CFLAGS)
BUILD_OVERRIDE_VAR_LIBCGETOPT = 0
BUILD_OVERRIDE_VAR_PACKAGE = ggetopt

TEST_TARGET =

INSTALL_OVERRIDE_VARS = prefix mandir WITH_GETTEXT
INSTALL_OVERRIDE_VAR_prefix = $(prefix)
INSTALL_OVERRIDE_VAR_mandir = $(mandir)
INSTALL_OVERRIDE_VAR_WITH_GETTEXT = 1

INSTALL_ARGS = inst# Use correct version of 'install'
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

include gar/category.mk

post-extract:
	@# Why are these files in the tarball?
	rm -f $(WORKSRC)/gnu/*.o
	@$(MAKECOOKIE)

post-installinstall-modulated:
	perl -pi -e 's,/usr/local/lib,$(libdir),' \
		$(DESTDIR)$(mandir