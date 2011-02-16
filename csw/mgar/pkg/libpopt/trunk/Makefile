NAME = popt
VERSION = 1.16
CATEGORIES = lib

DESCRIPTION = Popt is a C library for parsing command line parameters
define BLURB
Popt is a C library for parsing command line parameters. Popt was
heavily influenced by the getopt() and getopt_long() functions,
but it improves on them by allowing more powerful argument expansion.
Popt can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments. Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules. 
endef

MASTER_SITES = http://rpm5.org/files/$(NAME)/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# This patch has been sent upstream:
#   http://www.mail-archive.com/popt-devel@rpm5.org/
PATCHFILES += 0001-Use-inttypes.h-if-stdint.h-is-not-available.patch

# This fixes a minor failing check. See for details
#   http://www.mail-archive.com/popt-devel@rpm5.org/msg00155.html
PATCHFILES += 0002-Fix-failing-tests.patch

PACKAGES += CSWlibpopt
CATALOGNAME_CSWlibpopt = libpopt
SPKG_DESC_CSWlibpopt = Transitional package as contents moved to CSWlibpopt0
PKGFILES_CSWlibpopt = NOFILES
ARCHALL_CSWlibpopt = 1
RUNTIME_DEP_PKGS_CSWlibpopt = CSWlibpopt0
CHECKPKG_OVERRIDES_CSWlibpopt += surplus-dependency|CSWlibpopt0

PACKAGES += CSWlibpopt0
CATALOGNAME_CSWlibpopt0 = libpopt0
SPKG_DESC_CSWlibpopt0 = Library for parsing command line parameters providing libpopt.so.0
# PKGFILES_CSWlibpopt0 = $(call baseisadirs,$(libdir),libpopt\.so\.0(\.\d+)*)

PACKAGES += CSWlibpopt-dev
CATALOGNAME_CSWlibpopt-dev = libpopt_dev
SPKG_DESC_CSWlibpopt-dev = Development files for libpopt.so
RUNTIME_DEP_PKGS_CSWlibpopt-dev = CSWlibpopt0
PKGFILES_CSWlibpopt-dev = $(PKGFILES_DEVEL)

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWggettextrt CSWiconv

BUILD64 = 1
NORUNPATH = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

# We need GNU gettext under the name xgettext (not gxgettext) and
# prepending /opt/csw/gnu needs _A LOT_ of GNU stuff installed
# or several commands usually taken from /usr/bin are searched
# there and are not found.
pre-configure:
	@ln -s /opt/csw/bin/gxgettext $(WORKSRC)/xgettext
	@$(MAKECOOKIE)

# Make sure xgettext we carefully linked just before is found before
# other versions.
PATH := .:$(PATH)
