NAME = libsigsegv
VERSION = 2.10
CATEGORIES = lib

DESCRIPTION = A library for catching and handling segmentation faults
define BLURB
  This is a library for handling page faults in user mode. A page fault occurs
  when a program tries to access to a region of memory that is currently not available.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

PACKAGES += CSWlibsigsegv2
CATALOGNAME_CSWlibsigsegv2 = libsigsegv2
SPKG_DESC_CSWlibsigsegv2 = A library for catching and handling segmentation faults, libsigsegv.so.2
PKGFILES_CSWlibsigsegv2 += $(call pkgfiles_lib,libsigsegv.so.2)
OBSOLETED_BY_CSWlibsigsegv2 = CSWlibsigsegv

FOREIGN_PACKAGES += CSWlibsigsegv0
OBSOLETED_BY_CSWlibsigsegv0 = CSWlibsigsegv

PACKAGES += CSWlibsigsegv-dev
CATALOGNAME_CSWlibsigsegv-dev = libsigsegv_dev
SPKG_DESC_CSWlibsigsegv-dev = Development files for libsigsegv.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibsigsegv-dev += CSWlibsigsegv2
OBSOLETED_BY_CSWlibsigsegv-dev = CSWlibsigsegv-devel

VENDOR_URL = http://www.gnu.org/software/libsigsegv/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static


include gar/category.mk
