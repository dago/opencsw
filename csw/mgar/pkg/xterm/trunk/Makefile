GARNAME = xterm
GARVERSION = 242
CATEGORIES = x11

DESCRIPTION = Terminal emulator for the X Window System
define BLURB
The xterm program is a terminal emulator for the X Window System. It provides
DEC VT102 and Tektronix 4014 compatible terminals for programs that can't use
the window system directly. This version implements ISO/ANSI colors using the
"new" color model (i.e., background color erase). It also implements most of
the control sequences for VT220.
endef

MASTER_SITES = ftp://invisible-island.net/xterm/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-setuid
CONFIGURE_ARGS += --enable-logging
CONFIGURE_ARGS += --enable-luit
CONFIGURE_ARGS += --enable-sun-fkeys
CONFIGURE_ARGS += --enable-wide-chars
CONFIGURE_ARGS += --with-utempter

include gar/category.mk
