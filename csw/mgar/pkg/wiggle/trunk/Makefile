NAME = wiggle
VERSION = 0.8
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Apply conflicting patches
define BLURB
  Wiggle is a program for applying patches that 'patch' cannot apply due
  to conflicting changes in the original.

  Wiggle will always apply all changes in the patch to the original. If
  it cannot find a way to cleanly apply a patch, it inserts it in the
  original in a manner similar to 'merge', and reports an unresolvable
  conflict.
endef

BUILD_DEP_PKGS += CSWlibncurses-dev
RUNTIME_DEP_PKGS += CSWlibncursesw5

MASTER_SITES = http://neil.brown.name/wiggle/
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_SCRIPTS =
PATCHFILES += 0001-remove-gcc-options.patch \
    0002-fix-for-building-with-solstudio.patch \
    0003-fix-installation-target.patch \
    0004-skip-time-in-test-script.patch
BUILD_ARGS = wiggle wiggle.man
TEST_TARGET = test

include gar/category.mk

CPPFLAGS := -I$(includedir)/ncursesw $(CPPFLAGS)
