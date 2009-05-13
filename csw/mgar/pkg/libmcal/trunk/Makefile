GARNAME = libmcal
GARVERSION = 0.7
CATEGORIES = lib

DESCRIPTION = Modular Calendar Access Library
define BLURB
	mcal stands for Modular Calendar Access Library. 
	libmcal is a C library for accessing calendars. 
	It's written to be very modular, with pluggable drivers. 
	One of the main drivers it handles is ICAP.
endef

SF_PROJ = $(call TOLOWER,$(GARNAME))
MASTER_SITES = $(SF_MIRRORS)

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PACKAGES = CSWlibmcal
CATALOGNAME_CSWlibmcal = libmcal
SPKG_DESC_CSWlibmcal = $(DESCRIPTION)


REQUIRED_PKGS_CSWlibmcal  = CSWexpat CSWfconfig CSWftype2 CSWiconv 

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)

## There are no tests for this
TEST_SCRIPTS = skip

test-skip:
	$(DONADA)

include gar/category.mk
