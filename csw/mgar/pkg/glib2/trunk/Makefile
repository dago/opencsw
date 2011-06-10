NAME = glib
VERSION = 2.29.6
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

PATCHFILES += 0001-Make-sure-we-have-the-include-for-major-minor.patch
PATCHFILES += 0001-Replace-.-not-understood-by-Sun-Studio.patch

# Use patch unless this is fixed:
#  https://bugzilla.gnome.org/show_bug.cgi?id=652272
PATCHFILES += 0003-Do-not-unconditionally-use-gcc-specific-Wstrict-alia.patch

PACKAGES += CSWglib2
SPKG_DESC_CSWglib2 = Low level core compatibility library for GTK+ and GNOME
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWglib2 += CSWlibffi5
RUNTIME_DEP_PKGS_CSWglib2 += CSWiconv
RUNTIME_DEP_PKGS_CSWglib2 += CSWzlib
# No package split yet
CHECKPKG_OVERRIDES_CSWglib2 += non-uniform-lib-versions-in-package

PACKAGES += CSWglib2-dev
SPKG_DESC_CSWglib2-dev = Low level core compatibility library for GTK+ and GNOME development
RUNTIME_DEP_PKGS_CSWglib2-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWglib2-dev += CSWlibffi5
RUNTIME_DEP_PKGS_CSWglib2-dev += CSWgamin
RUNTIME_DEP_PKGS_CSWglib2-dev += CSWglib2
RUNTIME_DEP_PKGS_CSWglib2-dev += CSWiconv
RUNTIME_DEP_PKGS_CSWglib2-dev += CSWpython
RUNTIME_DEP_PKGS_CSWglib2-dev += CSWzlib
OBSOLETED_BY_CSWglib2-dev = CSWglib2devel
CATALOGNAME_CSWglib2devel = glib2_devel_stub

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

EXTRA_CFLAGS = -features=extensions

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv=gnu
CONFIGURE_ARGS += --enable-static

# DTrace compilation fails for 64 bit, disable for now
#CONFIGURE_ARGS += --disable-dtrace

BUILD64 = 1

BUILD_DEP_PKGS = CSWggettext

# Some tests fail, they may be harmless, disable for now, but check later!
# SKIPTEST ?= 1

#provided by iconv
MERGE_EXCLUDE_FILES = .*/charset.alias

PKGFILES_CSWglib2  = $(PKGFILES_RT)
PKGFILES_CSWglib2 += /opt/csw/share/locale/.*

EXTRA_LDFLAGS = -lsocket

include gar/category.mk

# We need /opt/csw/gnu/gettext, /usr/bin/gettext bails out
PATH := /opt/csw/gnu:$(PATH)
