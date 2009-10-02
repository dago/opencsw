GARNAME = popt
GARVERSION = 1.15
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

MASTER_SITES = http://rpm5.org/files/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWlibpopt

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWggettextrt CSWiconv

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
