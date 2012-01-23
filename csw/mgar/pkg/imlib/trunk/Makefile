NAME = imlib
VERSION = 1.9.15
CATEGORIES = lib

DESCRIPTION = An advanced replacement library for libraries like libXpm
define BLURB
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

STRIP_LIBTOOL = 1

# Make glib and gtk 64 bit first
# BUILD64 = 1
sysconfdir = /etc/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)

PRESERVECONF += $(sysconfdir)/im_palette-small.pal
PRESERVECONF += $(sysconfdir)/im_palette-tiny.pal
PRESERVECONF += $(sysconfdir)/im_palette.pal
PRESERVECONF += $(sysconfdir)/imrc

RUNTIME_DEP_PKGS_CSWimlib += CSWjpeg
RUNTIME_DEP_PKGS_CSWimlib += CSWpng
RUNTIME_DEP_PKGS_CSWimlib += CSWtiff
RUNTIME_DEP_PKGS_CSWimlib += CSWzlib
RUNTIME_DEP_PKGS_CSWimlib += CSWglib
RUNTIME_DEP_PKGS_CSWimlib += CSWgiflibrt
RUNTIME_DEP_PKGS_CSWimlib += CSWgtk

# Building the test cases misses -lX11, disable for now
SKIPTEST ?= 1

TEST_TARGET = check

# No package refactoring for now
CHECKPKG_OVERRIDES_CSWimlib += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWimlib += non-uniform-lib-versions-in-package

include gar/category.mk
