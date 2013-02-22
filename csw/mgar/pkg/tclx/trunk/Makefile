NAME = tclx
MAJOR = 8.4
MINOR = 1
VERSION = $(MAJOR).$(MINOR)
GARTYPE = v2

DESCRIPTION = TCL X

MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(NAME)$(MAJOR)
DISTFILES += $(NAME)$(VERSION).tar.bz2

VENDOR_URL = http://www.neosoft.com/TclX/

PACKAGES += CSWtclx
SPKG_DESC_CSWtclx = Extended Tcl
# PKGFILES is catchall

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

# The test for 32 bit pulls in 64 bit tclsh
SKIPTEST ?= 1

TEST_TARGET = test


include gar/category.mk

