NAME    = meanwhile
VERSION = 1.0.2
GARTYPE = v2

DESCRIPTION = Open implementation of the Lentation of the lotus sametime community client
define BLURB
  The Meanwhile project is an open implementation of the Lotus Sametime client protocol. The project provides a library written in C, a pythPidginodule, and a Gaim plugin utilizing the library.
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$
# Patches for status and glib:
# https://aur.archlinux.org/packages.php?ID=44209&comments=all
PATCHFILES  = 0001-broken-status.patch
PATCHFILES += 0002-fix_glib_includes.patch

# OpenCSW patches
PATCHFILES += 0003-doc_dir.patch
PATCHFILES += 0004-ft_fix.patch
PATCHFILES += 0005-status_timestamp_workaround.patch

OBSOLETED_BY_CSWlibmeanwhile1 += CSWmeanwhile

PACKAGES += CSWlibmeanwhile1
CATALOGNAME_CSWlibmeanwhile1 = libmeanwhile1
PKGFILES_CSWlibmeanwhile1 += $(call baseisadirs,$(libdir),libmeanwhile\.so\.1\.0\.2)
PKGFILES_CSWlibmeanwhile1 += $(call baseisadirs,$(libdir),libmeanwhile\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibmeanwhile1 += $(DESCRIPTION), libmeanwhile.so.1

PACKAGES += CSWmeanwhile-dev
CATALOGNAME_CSWmeanwhile-dev = meanwhile_dev
SPKG_DESC_CSWmeanwhile-dev += $(DESCRIPTION), development files
# PKGFILES is catchall

RUNTIME_DEP_PKGS_CSWlibmeanwhile1 += CSWlibglib2-0-0

RUNTIME_DEP_PKGS_CSWmeanwhile-dev += CSWlibmeanwhile1

# Needed to update the old Doxyfile
BUILD_DEP_PKGS += CSWdoxygen

# All needed for glib2
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWggettext-dev

#No tests
TEST_SCRIPTS =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

EXTRA_CFLAGS += -features=extensions


include gar/category.mk

post-configure:
	@doxygen -u $(WORKSRC)/doc/Doxyfile
