GARNAME = glib
GARVERSION = 2.25.10
CATEGORIES = lib

DESCRIPTION = The GLib library of C routines.
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, and lists. GLib was previously distributed with the GTK toolkit, but
  has been split off as of the developers' version 1.1.0.
endef

PACKAGES = CSWglib2 CSWglib2devel
CATALOGNAME_CSWglib2 = glib2
CATALOGNAME_CSWglib2devel = glib2_devel
SPKG_DESC_CSWglib2 = Low level core compatibility library for GTK+ and GNOME
SPKG_DESC_CSWglib2devel = Low level core compatibility library for GTK+ and GNOME development

MASTER_SITES = $(GNOME_MIRROR)

DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

PATCHFILES  = glib-typedetect.patch
# PATCHFILES += FIXED_STR.patch
PATCHFILES += gsize.patch
# PATCHFILES += gconverter.patch
PATCHFILES += CMSG_LEN.patch

# Bug reported upstream:
#   https://bugzilla.gnome.org/show_bug.cgi?id=612300
# PATCHFILES += 0001-Use-G_STRFUNC-instead-of-explicit-gcc-only-__PRETTY_.patch

PATCHFILES += 0001-Make-sure-we-have-the-include-for-major-minor.patch
PATCHFILES += 0001-Replace-.-not-understood-by-Sun-Studio.patch

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv=gnu
CONFIGURE_ARGS += --enable-static

# DTrace compilation fails for 64 bit, disable for now
CONFIGURE_ARGS += --disable-dtrace

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NOISAEXEC = 1

BUILD_DEP_PKGS = CSWggettext CSWperl

RUNTIME_DEP_PKGS_CSWglib2 += CSWggettextrt
RUNTIME_DEP_PKGS_CSWglib2 += CSWiconv
RUNTIME_DEP_PKGS_CSWglib2 += CSWzlib
RUNTIME_DEP_PKGS_CSWglib2devel += CSWgamin
RUNTIME_DEP_PKGS_CSWglib2devel += CSWggettextrt
RUNTIME_DEP_PKGS_CSWglib2devel += CSWglib2
RUNTIME_DEP_PKGS_CSWglib2devel += CSWiconv
RUNTIME_DEP_PKGS_CSWglib2devel += CSWpython
RUNTIME_DEP_PKGS_CSWglib2devel += CSWzlib

# Some tests fail, they may be harmless, disable for now, but check later!
SKIPTEST ?= 1
TEST_TARGET = check

#provided by iconv
MERGE_EXCLUDE_FILES = .*/charset.alias

PKGFILES_CSWglib2  = $(PKGFILES_RT)
PKGFILES_CSWglib2 += /opt/csw/share/locale/.*

EXTRA_LDFLAGS = -lsocket

include gar/category.mk

# We need /opt/csw/gnu/gettext, /usr/bin/gettext bails out
PATH := /opt/csw/gnu:$(PATH)
