GARNAME = xterm
GARVERSION = 248
CATEGORIES = apps

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

REQUIRED_PKGS = CSWfconfig CSWlibxft2

# enable -mk_width per default to address unicode form character width woes, 
# can be taken out once upstream enhances wcwidth() sanity checking 
#   http://article.gmane.org/gmane.comp.lib.ncurses.bugs/3795
#
# fixed in #244, let's see whether it works
#PATCHFILES = patch-mkwidth.diff

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-setuid
CONFIGURE_ARGS += --disable-setgid
CONFIGURE_ARGS += --enable-broken-osc
CONFIGURE_ARGS += --enable-broken-st
CONFIGURE_ARGS += --enable-dabbrev
CONFIGURE_ARGS += --enable-exec-term
CONFIGURE_ARGS += --enable-load-vt-fonts
CONFIGURE_ARGS += --enable-logfile-exec
CONFIGURE_ARGS += --enable-logging
CONFIGURE_ARGS += --enable-sun-fkeys
CONFIGURE_ARGS += --enable-warnings
CONFIGURE_ARGS += --enable-wide-chars
CONFIGURE_ARGS += --program-suffix=86 --with-xterm-symlink
CONFIGURE_ARGS += --with-freetype-cflags="-I$(includedir)/freetype2"
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib

# luit comes with snv_85 
#   http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6662431
#CONFIGURE_ARGS += --enable-luit

#GARFLAVOR = DBG
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))
CONFIGURE_ARGS_DBG = --enable-trace --enable-warnings

include gar/category.mk

post-install-modulated:
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(FILEDIR)/README.CSW $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)
