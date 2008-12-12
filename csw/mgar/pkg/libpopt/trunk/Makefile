GARNAME = popt
GARVERSION = 1.14
CATEGORIES = lib

DESCRIPTION = Popt is a C library for parsing command line parameters
define BLURB
endef

MASTER_SITES = http://rpm5.org/files/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibpopt)

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWggettext CSWiconv

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
