GARNAME = gdb
GARVERSION = 6.8
CATEGORIES = devel

DESCRIPTION = The GNU Project Debugger
define BLURB
endef

MASTER_SITES = http://ftp.gnu.org/gnu/gdb/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

SPKG_SOURCEURL = http://www.gnu.org/software/gdb

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

REQUIRED_PKGS = CSWexpat CSWggettextrt CSWiconv CSWncurses

BUILD64 = 1
NO_ISAEXEC = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

# Needed for testing
PATH := $(PATH):/opt/csw/gcc4/bin
