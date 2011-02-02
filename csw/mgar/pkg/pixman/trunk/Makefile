NAME      = pixman
VERSION   = 0.21.4
CATEGORIES   = lib

DESCRIPTION = The pixel-manipulation library for X and cairo
define BLURB
endef

MASTER_SITES = http://www.cairographics.org/releases/
DISTFILES = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Use-inttypes-if-stdint-is-not-available.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWpixman
CATALOGNAME_CSWpixman = pixman
SPKG_DESC_CSWpixman = Legacy package as contents moved to CSWlibpixman1-0
PKGFILES_CSWpixman = NOFILES
ARCHALL_CSWpixman = 1
RUNTIME_DEP_PKGS_CSWpixman = CSWlibpixman1-0
CHECKPKG_OVERRIDES_CSWpixman += surplus-dependency|CSWlibpixman1-0

PACKAGES += CSWlibpixman1-0
CATALOGNAME_CSWlibpixman1-0 = libpixman1_0
SPKG_DESC_CSWlibpixman1-0 = The pixel-manipulation library for X and cairo, libpixman-1.so.0
PKGFILES_CSWlibpixman1-0 += $(call baseisadirs,$(libdir),libpixman-1\.so\.0(\.\d+)*)

PACKAGES += CSWlibpixman-dev
CATALOGNAME_CSWlibpixman-dev = libpixman_dev
SPKG_DESC_CSWlibpixman-dev = Development files for libpixman
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibpixman-dev += CSWlibpixman1-0

# It should be sufficient to add '-mt', but then I get
# undefined symbol on ___tls_get_addr. Explicit linkage against libthread.so
# solved it, but I am unsure if this is correct.
EXTRA_CFLAGS = -mt
EXTRA_LINKER_FLAGS = -mt -lthread

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-gtk

CONFIGURE_ARGS-i386 = --disable-sse2
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(ISA))

#CONFIGURE_ARGS += --disable-timers
#CONFIGURE_ARGS += --disable-gcc-inline-asm
# CONFIGURE_ARGS += --disable-openmp

include gar/category.mk
