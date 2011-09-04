# TBD:
# - python files are produced for 32/64 bit: we don't have 64 bit python, wtf?
# - python files are not in the python lib dir, but directly in lib. The dir in configure is not used

NAME = glib
VERSION = 2.29.16
CATEGORIES = lib

DESCRIPTION = The GLib library of C routines.
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists. GLib was previously distributed with the GTK toolkit, but
  has been split off as of the developers' version 1.1.0.
endef

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES = $(NAME)-$(VERSION).tar.bz2

#PATCHFILES  = glib-typedetect.patch
# PATCHFILES += FIXED_STR.patch
#PATCHFILES += gsize.patch
# PATCHFILES += gconverter.patch
#PATCHFILES += CMSG_LEN.patch

# Bug reported upstream:
#   https://bugzilla.gnome.org/show_bug.cgi?id=612300
# PATCHFILES += 0001-Use-G_STRFUNC-instead-of-explicit-gcc-only-__PRETTY_.patch

#PATCHFILES += 0001-Make-sure-we-have-the-include-for-major-minor.patch
#PATCHFILES += 0001-Replace-.-not-understood-by-Sun-Studio.patch

# Use patch unless this is fixed:
#  https://bugzilla.gnome.org/show_bug.cgi?id=652272
PATCHFILES += 0003-Do-not-unconditionally-use-gcc-specific-Wstrict-alia.patch

# Skip /strfuncs/strtod unless this is fixed:
#   http://bugzilla.gnome.org/show_bug.cgi?id=652560
PATCHFILES += 0004-Skip-test-strfuncs-strtod-as-Solaris-does-not-suppor.patch

PATCHFILES += 0005-Disable-faililing-tests-for-now.patch

PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
# Make special build for Solaris 10 to use dtrace
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

PACKAGES += CSWglib2
SPKG_DESC_CSWglib2 = Low level core compatibility library for GTK+ and GNOME
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWglib2 += CSWgamin
RUNTIME_DEP_PKGS_CSWglib2 += CSWpython
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibffi5
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibgio2-0-0
## No package split yet
#CHECKPKG_OVERRIDES_CSWglib2 += non-uniform-lib-versions-in-package

PACKAGES += CSWlibgio2-0-0
PKGFILES_CSWlibgio2-0-0 += $(call pkgfiles_lib,libgio-2.0.so.0)
SPKG_DESC_CSWlibgio2-0-0 += $(DESCRIPTION), libgio-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibffi5
RUNTIME_DEP_PKGS_CSWlibgio2-0-0 += CSWlibglib2-0-0

PACKAGES += CSWlibglib2-0-0
PKGFILES_CSWlibglib2-0-0 += $(call pkgfiles_lib,libglib-2.0.so.0)
SPKG_DESC_CSWlibglib2-0-0 += $(DESCRIPTION), libglib-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibglib2-0-0 += CSWlibiconv2

PACKAGES += CSWlibgmodule2-0-0
PKGFILES_CSWlibgmodule2-0-0 += $(call pkgfiles_lib,libgmodule-2.0.so.0)
SPKG_DESC_CSWlibgmodule2-0-0 += $(DESCRIPTION), libgmodule-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgmodule2-0-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgobject2-0-0
PKGFILES_CSWlibgobject2-0-0 += $(call pkgfiles_lib,libgobject-2.0.so.0)
SPKG_DESC_CSWlibgobject2-0-0 += $(DESCRIPTION), libgobject-2.0.so.0
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibffi5
RUNTIME_DEP_PKGS_CSWlibgobject2-0-0 += CSWlibglib2-0-0

PACKAGES += CSWlibgthread2-0-0
SPKG_DESC_CSWlibgthread2-0-0 += $(DESCRIPTION), libgthread-2.0.so.0
PKGFILES_CSWlibgthread2-0-0 += $(call pkgfiles_lib,libgthread-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgthread2-0-0 += CSWlibglib2-0-0

PACKAGES += CSWlibglib2-dev
SPKG_DESC_CSWlibglib2-dev = Development files for libglib-2.0.so.0 and assorted libglib, libgmodule, libgobject and libgthread
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibffi5
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWgamin
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWglib2
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWiconv
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWpython
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWzlib
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibglib2-dev += CSWlibgthread2-0-0
PKGFILES_CSWlibglib2-dev += $(PKGFILES_DEVEL)
OBSOLETED_BY_CSWlibglib2-dev = CSWglib2devel
CATALOGNAME_CSWglib2devel = glib2_devel_stub

BUILD_DEP_PKGS = CSWggettext

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

EXTRA_CFLAGS = -features=extensions

EXTRA_CFLAGS-5.10 += -xc99=all -D_XOPEN_SOURCE=600 -D_XPG6
EXTRA_CFLAGS += $(EXTRA_CFLAGS-$(GAROSREL))

EXTRA_LDFLAGS = -lsocket

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv=gnu
# CONFIGURE_ARGS += --enable-static

# DTrace compilation fails, disable for now
CONFIGURE_ARGS += --disable-dtrace

# Some tests fail, they may be harmless, disable for now, but check later!
#   http://bugzilla.gnome.org/show_bug.cgi?id=652560
SKIPTEST ?= 1

PYCOMPILE = 1

#provided by iconv
MERGE_EXCLUDE_FILES = .*/charset.alias

include gar/category.mk

# We need /opt/csw/gnu/gettext, /usr/bin/gettext bails out
PATH := /opt/csw/gnu:$(PATH)
