NAME = libwnck
VERSION = 2.18.3
# 2.18.3 = .so.18
# 2.19.92 = so.22
# 2.20.3 = .so.22
# 2.24.2 = .so.22
# 2.28.0 = .so.22
CATEGORIES = lib

DESCRIPTION = Library used for writing pagers and tasks lists
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWlibwnck CSWlibwnckdevel

CATALOGNAME_CSWlibwnck = libwnck
CATALOGNAME_CSWlibwnckdevel = libwnck_devel

SPKG_DESC_CSWlibwnck = $(DESCRIPTION)
SPKG_DESC_CSWlibwnckdevel = Developer files for libwnck

VENDOR_URL = http://ftp.gnome.org/pub/GNOME/sources/libwnck/

BUILD_DEP_PKGS = CSWgtk2devel CSWglib2devel

RUNTIME_DEP_PKGS_CSWlibwnck  = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2
RUNTIME_DEP_PKGS_CSWlibwnck += CSWlibatk CSWlibcairo CSWpango CSWstartupnotif
RUNTIME_DEP_PKGS_CSWlibwnckdevel = CSWlibwnck $(BUILD_DEP_PKGS)

# For cos(3m)
EXTRA_LINKER_FLAGS = -lm 

NOISAEXEC = 1
BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

PKGFILES_CSWlibwnckdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibwnckdevel += $(sharedstatedir)/gtk-doc/.*

# This is okay
CHECKPKG_OVERRIDES_CSWlibwnckdevel += surplus-dependency|CSWlibwnck
CHECKPKG_OVERRIDES_CSWlibwnckdevel += surplus-dependency|CSWglib2devel
CHECKPKG_OVERRIDES_CSWlibwnckdevel += surplus-dependency|CSWgtk2devel

include gar/category.mk

# Needed for GNU gettext
PATH := /opt/csw/gnu:$(PATH)
