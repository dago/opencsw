NAME = babl
VERSION = 0.1.10
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = A dynamic, any to any, pixel format translation library
define BLURB
  babl is a library for dynamically handling pixel formats and managing
  conversions between them.  It is being used by GEGL.
endef

MASTER_SITES = http://ftp.gtk.org/pub/babl/$(shell echo $(VERSION) | awk -F. '{print $$1"."$$2}')/
DISTFILES += $(NAME)-$(VERSION).tar.bz2

GARCOMPILER = SOS12U3

# Use patch until this is fixed:
#   https://bugzilla.gnome.org/show_bug.cgi?id=664800
PATCHFILES += 0001-Use-inttypes.h-if-stdint.h-is-not-available.patch
PATCHFILES += 0002-include-iso-limits-babl-palette.c.patch

VENDOR_URL = http://gegl.org/babl/

PACKAGES += CSWlibbabl0-1-0
SPKG_DESC_CSWlibbabl0-1-0 = A dynamic, any to any, pixel format translation library, libbabl-0.1.so.0
PKGFILES_CSWlibbabl0-1-0 += $(call pkgfiles_lib,libbabl-0.1.so.0)
PKGFILES_CSWlibbabl0-1-0 += $(call baseisadirs,$(libdir),babl-0.1/.*)
OBSOLETED_BY_CSWlibbabl0-1-0 += CSWlibbabl

PACKAGES += CSWlibbabl-dev
SPKG_DESC_CSWlibbabl-dev = Development files for libbabl-0.1.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibbabl-dev += CSWlibbabl0-1-0

BUILD64_LIBS_ONLY = 1

# Replace manually until this is fixed:
#   https://bugzilla.gnome.org/show_bug.cgi?id=664800
REINPLACEMENTS += pthread
REINPLACE_MATCH_pthread = -pthread
REINPLACE_WITH_pthread = -lpthread
REINPLACE_FILES_pthread = tests/Makefile.in

# There is currently one test failing, upstream has been notified, disable for now until this is fixed:
#   https://bugzilla.gnome.org/show_bug.cgi?id=664800
SKIPTEST ?= 1

# wrong option for SolarisStudio Compiler
CONFIGURE_ARGS += --enable-mmx=no
# CONFIGURE_ARGS += --disable-sse 

include gar/category.mk
