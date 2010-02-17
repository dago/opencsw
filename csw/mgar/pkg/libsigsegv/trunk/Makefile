GARNAME = libsigsegv
GARVERSION = 2.8
CATEGORIES = lib

DESCRIPTION = A library for catching and handling segmentation faults
define BLURB
  This is a library for handling page faults in user mode. A page fault occurs
  when a program tries to access to a region of memory that is currently not available.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.gnu.org/software/libsigsegv/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static

TEST_TARGET = check

include gar/category.mk
