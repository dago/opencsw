NAME = pth
VERSION = 2.0.7
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNU Pth - The GNU Portable Threads
define BLURB
  Pth is a very portable POSIX/ANSI-C based library for Unix platforms which
  provides non-preemptive priority-based scheduling for multiple threads of
  execution (aka 'multithreading') inside event-driven applications.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# Patch PTH.H to increase FD_SETSIZE for 64bit b+= 0001_patch_pth_fdsetsize64.diff

# The max FD_SETSIZE test must depend on the architecture being built
PATCHFILES += 0002_FD_SETSIZE_depends_on_arch.patch_fdsetsize64.diff

VENDOR_URL = http://www.gnu.org/software/pth/

PACKAGES += CSWlibpth20
SPKG_DESC_CSWlibpth20 = GNU Pth portable threads
PKGFILES_CSWlibpth20 = $(call pkgfiles_lib,libpth.so.20)
OBSOLETED_BY_CSWlibpth20 = CSWpth

PACKAGES += CSWlibpth-dev
SPKG_DESC_CSWlibpth-dev = Development files for libpth.so.20
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibpth-dev = CSWlibpth20

BUILD6CONFIGURE_ARGS = $(DIRPATHS)D6include gar/category.mk
