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
