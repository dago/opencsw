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

PACKAGES += CSWlibpopt0
SPKG_DESC_CSWlibpopt0 = Library for parsing command line parameters, libpopt.so.0
# PKGFILES is catchall (library and according LC_MESSAGES)
OBSOLETED_BY_CSWlibpopt0 += CSWlibpopt
RUNTIME_DEP_PKGS_CSWlibpopt0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibpopt0 += CSWlibiconv2

PACKAGES += CSWlibpopt-dev
SPKG_DESC_CSWlibpopt-dev = Development files for libpopt.so
RUNTIME_DEP_PKGS_CSWlibpopt-dev = CSWlibpopt0
PKGFILES_CSWlibpopt-dev += $(PKGFILES_DEVEL)
OBSOLETES_CSWlibpopt-dev += CSWlibpopt

BUILD64_LIBS_ONLY = 1
NORUNPATH = 1

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
