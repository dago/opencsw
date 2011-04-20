NAME = libsigsegv
VERSION = 2.6
CATEGORIES = lib

DESCRIPTION = A library for catching and handling segmentation faults
define BLURB
  This is a library for handling page faults in user mode. A page fault occurs
  when a program tries to access to a region of memory that is currently not available.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

PACKAGES += CSWlibsigsegv0
CATALOGNAME_CSWlibsigsegv0 = libsigsegv0
SPKG_DESC_CSWlibsigsegv0 = A library for catching and handling segmentation faults, libsigsegv.so.0
PKGFILES_CSWlibsigsegv0 += $(call pkgfiles_lib,libsigsegv.so.0)

VENDOR_URL = http://www.gnu.org/software/libsigsegv/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static

include gar/category.mk
