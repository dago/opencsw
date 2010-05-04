# TODO (release-critical prefixed with !, non release-critical with *)
# * app-defaults are currently in $(prefix)/X11/etc/X11/app-defaults
#   because of our libXt. Once the whole X11 mess is sorted, they
#   might go to $(prefix)/etc/X11/app-defaults instead.
GARNAME = xterm
GARVERSION = 258
CATEGORIES = apps

DESCRIPTION = Terminal emulator for the X Window System
define BLURB
  The xterm program is a terminal emulator for the X Window System. It provides
  DEC VT102 and Tektronix 4014 compatible terminals for programs that can't use
  the window system directly. This version implements ISO/ANSI colors using the
  "new" color model (i.e., background color erase). It also implements most of
  the control sequences for VT220.
endef

VENDOR_URL    = http://invisible-island.net/xterm/
MASTER_SITES  = ftp://invisible-island.net/xterm/
DISTFILES     = $(GARNAME)-$(GARVERSION).tgz
UFILES_REGEX  = $(GARNAME)-(\d+(?:\.\d+)*).tgz
DISTFILES    += COPYING

RUNTIME_DEP_PKGS  = CSWfconfig
RUNTIME_DEP_PKGS += CSWlibxft2
RUNTIME_DEP_PKGS += CSWlibice
RUNTIME_DEP_PKGS += CSWlibx11
RUNTIME_DEP_PKGS += CSWlibxaw
RUNTIME_DEP_PKGS += CSWlibxmu
RUNTIME_DEP_PKGS += CSWlibxt

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
# Through CSW freetype, xterm depends on Xrender and Xft. Starting with 
#
# 	libxrender-0.9.4,REV=2009.06.11
#	libxft2-2.1.13,REV=2009.06.15
#
# these libs moved to the CSW X11 libs prefix (/opt/csw/X11). Accordingly, 
# we need to build against these X11 libs, otherwise ./configure bails out
# when verifying the linkage to freetype. This unfortunatel drags a pile
# of other CSW X11 libs with it ... o_O ...
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

# Xt app-default files need to go where Xt looks for them (one of
# $(prefix)/X11/{etc,share,lib}/X11/app-defaults)
CONFIGURE_ARGS += --with-app-defaults=$(prefix)/X11/etc/X11/app-defaults

# Make sure to runtime link the same way that we link edited
# * xterm link edit order is (-L/-R):  X11/lib/, lib/
# * LD_OPTIONS would prepend (-R):  lib/
# -> libs like libXft might be runtime linked from lib/ instead of X11/lib/
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(filter-out %ISALIST, $(RUNPATH_LINKER_FLAGS))

# luit comes with snv_85 
#   http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=6662431
#CONFIGURE_ARGS += --enable-luit


include gar/category.mk

# ./configure needs to find xft-config
PATH := /opt/csw/X11/bin:$(PATH)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated: CSWDOCS=README.CSW changelog.CSW
post-install-modulated: DOCS=xterm.log.html ctlseqs.txt
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(addprefix $(FILEDIR)/,$(CSWDOCS)) $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS))    $(DOCDEST)
	@$(MAKECOOKIE)
