# TODO
# - Now that we mostly have our own CSW X11 libs, can we place the app-default
#   files in a location where they are actually read by default?
GARNAME = xterm
GARVERSION = 251
CATEGORIES = apps

DESCRIPTION = Terminal emulator for the X Window System
define BLURB
  The xterm program is a terminal emulator for the X Window System. It provides
  DEC VT102 and Tektronix 4014 compatible terminals for programs that can't use
  the window system directly. This version implements ISO/ANSI colors using the
  "new" color model (i.e., background color erase). It also implements most of
  the control sequences for VT220.
endef

SPKG_SOURCEURL = http://invisible-island.net/xterm/
MASTER_SITES   = ftp://invisible-island.net/xterm/
DISTFILES      = $(GARNAME)-$(GARVERSION).tgz
UFILES_REGEX   = $(GARNAME)-(\d+(?:\.\d+)*).tgz

REQUIRED_PKGS = CSWfconfig CSWlibxft2

# xterm Makefile doesn't have a test target
TEST_TARGET =

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

#GARFLAVOR = DBG
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))
CONFIGURE_ARGS_DBG = --enable-trace --enable-warnings

# Notes on CSW X11 libs:
# xterm depends on Xrender and Xft for freetype font support. Starting with 
#
# 	libxrender-0.9.4,REV=2009.06.11
#	libxft2-2.1.13,REV=2009.06.15
#
# these libs moved to the CSW X11 libs prefix (/opt/csw/X11). Accordingly, 
# we need to build against these X11 libs, otherwise ./configure bails out
# when verifying the linkage to freetype. This unfortunatel drags a pile
# of other CSW X11 libs with it ... o_O ... Any caveats? libX11 for
# instance will be run-time linked twice (see ldd output on xterm).
# One from Solaris, another one from us. Time will show how this works out.
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(prefix)/X11/lib

REQUIRED_PKGS += CSWlibice CSWlibx11 CSWlibxaw CSWlibxmu CSWlibxt

# The need for the explicit -lfontconfig linkage also came along when 
# we upgraded from xterm-243 (CSW X11 libs had been introduced in the
# meantime, related? pkgconfig woes?). Without the explicit linkage
# there are implicit symbol dependencies on the final xterm linking run.
EXTRA_LDFLAGS = -L$(libdir) -lfontconfig

# luit comes with snv_85 
#   http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6662431
#CONFIGURE_ARGS += --enable-luit


include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated: CSWDOCS=README.CSW changelog.CSW
post-install-modulated: DOCS=xterm.log.html ctlseqs.txt
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(addprefix $(FILEDIR)/,$(CSWDOCS)) $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS))    $(DOCDEST)
	@$(MAKECOOKIE)
