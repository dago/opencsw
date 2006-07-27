GARNAME = ncurses
GARVERSION = 5.5
CATEGORIES = lib

DESCRIPTION = ncurses library and utilities
define BLURB
	The ncurses (new curses) library is a free software emulation of curses in System V Release 4.0 and more. It uses terminfo format, supports pads and color and multiple highlights and forms charcters and function-key mapping, and has all the other SYSV-curses enhancements over BSD curses. It should port easily to any ANSI/POSIX-conforming UNIX-like system. On systems supporting libiconv, the library can be built to support wide- and multibyte-character applications, e.g., UTF-8. 
endef

MASTER_SITES = ftp://ftp.gnu.org/pub/gnu/ncurses/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWncurses,prototype)

CONFIGURE_ARGS = $(DIRPATHS) 
CONFIGURE_ARGS += --without-libtool
CONFIGURE_ARGS += --with-shared 
CONFIGURE_ARGS += --disable-overwrite
CONFIGURE_ARGS += --without-ada

ENABLE_TEST = 0

include ../category.mk

LDFLAGS = -L/export/home/aalmroth/csw-build.5.8-i386/opt/csw/lib  -L/opt/csw/lib
