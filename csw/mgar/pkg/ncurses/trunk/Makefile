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

ifeq ($(GARVERSION),5.7)
LD_OPTIONS = $(LD_FLAGS)
endif

TEST_SCRIPTS =

include gar/category.mk

#LDFLAGS := $(filter-out -xarch=%,$(filter-out -m%,$(LDFLAGS)))
LDFLAGS :=

ifeq ($(MEMORYMODEL),64)
LDFLAGS := $(LDFLAGS) $(if $(findstring $(GARVERSION),5.6),-xarch=v9)
endif

