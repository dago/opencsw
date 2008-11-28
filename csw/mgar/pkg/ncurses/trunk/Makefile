GARNAME = ncurses
GARVERSION = 5.7
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 5.4 5.6 5.7

DESCRIPTION = ncurses library and utilities
define BLURB
        The ncurses (new curses) library is a free software emulation of curses in System V Release 4.0 and more. It uses terminfo forma
t, supports pads and color and multiple highlights and forms charcters and function-key mapping, and has all the other SYSV-curses enhan
cements over BSD curses. It should port easily to any ANSI/POSIX-conforming UNIX-like system. On systems supporting libiconv, the librar
y can be built to support wide- and multibyte-character applications, e.g., UTF-8. 
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(foreach V,$(MODULATIONS_GARVERSION),$(GARNAME)-$(V).tar.gz)
DISTFILES += $(call admfiles,CSWncurses)

BUILD64 = 1

CONFIGURE_ARGS = --prefix=/opt/csw 
CONFIGURE_ARGS += --without-libtool
CONFIGURE_ARGS += --with-shared 
CONFIGURE_ARGS += --disable-overwrite
CONFIGURE_ARGS += --without-ada
ifeq ($(MEMORYMODEL),64)
CONFIGURE_ARGS += --with-build-ldflags="-64"
endif

TEST_SCRIPTS =

include gar/category.mk

# 32 Bit
#LDFLAGS := $(filter-out -xarch=386,$(filter-out -m32,$(LDFLAGS)))

# 64 Bit
#LDFLAGS := $(filter-out -xarch=sse2,$(filter-out -m64,$(LDFLAGS)))
#ifeq ($(MEMORYMODEL),64)
#LDFLAGS := $(LDFLAGS) -64
#endif

