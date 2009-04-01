GARNAME = vttest
GARVERSION = 20071216
CATEGORIES = utils

DESCRIPTION = Tool for testing VT100 compatibility of terminals
define BLURB
This is a program to test the compatibility (or to demonstrate the
non-compatibility) of so-called "VT100-compatible" terminals. Additional tests
(past version 1.7) are provided for analysis of vt220, vt420 terminals, as well
as variants of xterm. 
endef

MASTER_SITES = ftp://invisible-island.net/vttest/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

UFILES_REGEX = $(GARNAME)-(\d+).tgz

TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

# No RUNPATH needed, vttest only links against system libs
LINKER_FLAGS =

include gar/category.mk
