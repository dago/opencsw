GARNAME = popt
GARVERSION = 1.13
CATEGORIES = lib

DESCRIPTION = Popt is a C library for parsing command line parameters
define BLURB
endef

MASTER_SITES = http://rpm5.org/files/$(GARNAME)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibpopt)

CONFIGURE_ARGS = $(DIRPATHS)

#EXTRA_BUILD_ISAS_i386 = amd64
#EXTRA_BUILD_ISAS_sparc = sparcv9

# Just do 64 bit build
#BUILD64 = 1

# Build all known ISAs (may not work with compiler)
#EXTRA_BUILD_ISAS = $(ISALIST)

# Build all ISAs known to the chosen compiler
EXTRA_BUILD_ISAS = $(ISALIST_$(GARCOMPILER))

TEST_TARGET = check

include ../category.mk

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

env:
	echo "I: $(ISALIST_$(GARCOMPILER))
