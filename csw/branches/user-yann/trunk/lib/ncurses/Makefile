GARNAME = ncurses
GARVERSION = 5.4
CATEGORIES = lib

SPKG_PKGNAME = CSWncurses
SPKG_BITNAME = ncurses

DESCRIPTION = A System V Release 4.0 curses emulation library.
define BLURB
  The ncurses (new curses) library is a freeware emulation of System V Release
  4.0 curses. It uses terminfo format, supports pads and color and multiple
  highlights and forms characters and function-key mapping, and has all the
  other SYSV-curses enhancements over BSD curses. The distribution includes the
  library and support utilities, including a terminfo compiler tic, a
  decompiler infocmp, clear, tput, tset, and a termcap conversion tool
  captoinfo. Full manual pages are provided for the library and tools.
endef

MASTER_SITES = ftp://ftp.gnu.org/gnu/$(GARNAME)/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libtool
CONFIGURE_ARGS += --enable-termcap
CONFIGURE_ARGS += --without-debug
CONFIGURE_ARGS += --without-cxx-binding

include ../category.mk
