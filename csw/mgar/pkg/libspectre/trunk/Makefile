NAME = libspectre
VERSION = 0.2.6
CATEGORIES = lib

DESCRIPTION = A small library for rendering Postscript documents
define BLURB
endef

MASTER_SITES = http://libspectre.freedesktop.org/releases/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Use int_types.h instead of stdint.h until this is fixed:
#   https://bugs.freedesktop.org/show_bug.cgi?id=27734
PATCHFILES = patch-stdint.diff

SPKG_SOURCEURL = http://libspectre.freedesktop.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS = CSWgs

# The flags -pedantic gets selected during configure as it seems to cause
# no harm, but it effectively triggers performance tuning and fails as some
# files miss _mcount as the performance lib is not linked in.
# Do this until this bug is resolved:
#   https://bugs.freedesktop.org/show_bug.cgi?id=27735
BUILD_OVERRIDE_VARS = SPECTRE_CFLAGS
BUILD_OVERRIDE_VAR_SPECTRE_CFLAGS =

# Disable for now as libgs is missing 64 bit
#BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
