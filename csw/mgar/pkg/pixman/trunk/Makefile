NAME      = pixman
VERSION   = 0.22.2
CATEGORIES   = lib
GARTYPE = v2

DESCRIPTION = The pixel-manipulation library for X and cairo
define BLURB
endef

MASTER_SITES = http://www.cairographics.org/releases/
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Use patch until this is fixed:
#   https://bugs.freedesktop.org/show_bug.cgi?id=41257
PATCHFILES += 0001-Use-inttypes-if-stdint-is-not-available.patch

PACKAGES += CSWlibpixman1-0
CATALOGNAME_CSWlibpixman1-0 = libpixman1_0
SPKG_DESC_CSWlibpixman1-0 = The pixel-manipulation library for X and cairo, libpixman-1.so.0
PKGFILES_CSWlibpixman1-0 += $(call pkgfiles_lib,libpixman-1.so.0)
OBSOLETED_BY_CSWlibpixman1-0 += CSWpixman

PACKAGES += CSWlibpixman-dev
CATALOGNAME_CSWlibpixman-dev = libpixman_dev
SPKG_DESC_CSWlibpixman-dev = Development files for libpixman-1.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibpixman-dev += CSWlibpixman1-0

EXTRA_CFLAGS = -mt
EXTRA_LINKER_FLAGS = -mt

BUILD64_LIBS_ONLY = 1
NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-gtk

CONFIGURE_ARGS-i386 = --disable-sse2
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(ISA))

BUILD_ARGS += V=1

include gar/category.mk
