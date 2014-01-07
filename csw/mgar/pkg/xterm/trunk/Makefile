# TODO (release-critical prefixed with !, non release-critical with *)
NAME = xterm
VERSION = 300
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Terminal emulator for the X Window System
define BLURB
  The xterm program is a terminal emulator for the X Window System. It provides
  DEC VT102 and Tektronix 4014 compatible terminals for programs that can't use
  the window system directly. This version implements ISO/ANSI colors using the
  "new" color model (i.e., background color erase). It also implements most of
  the control sequences MASTER_SITES += ftp://invisible-island.net/xterm/
DISTFILES += $(NAME)-$(VERSION).tgz

VENDOR_URL = http://invisible-island.net/xterm/
LICENSE = INSTALL

PACKAGES += CSWxterm
SPKG_DESC_CSWxterm = Terminal emulator for the X Window System
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWxterm += CSWlibxft2
RUNTIME_DEP_PKGS_CSWxterm += CSWlibxpm4
RUNTIME_DEP_PKGS_CSWxterm += CSWlibfontconfig1

PIXMAPDIR = $(sharedstatedir)/pixmaps/xterm
EXTRA_CPPFLAGS += -DPIXMAP_ROOTDIR=\\\"$(PIXMAPDIR)\\\"rget
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
CONFIGURE_ARGS += --program-suffix=86 --wCONFIGURE_ARGS += --with-pixmapdir=$(PIXMAPDIR)with-xterm-symlink

# Specify freetype linker flags, otherwise /opt/csw/X11/bin/xft-config is used
CONFIGURE_ARGS += --with-freetype-cflags="-I$(includedir)/freetype2"
CONFIGURE_ARGS += --with-freetype-libs="-lXft -lfontco
#GARFLAVOR = DBG
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARFLAVOR))
CONFIGURE_ARGS_DBG = --enable-trace --enable-warnings

# luit comes with snv_85 
#   http://bugs.opensolaris.org/bugdatabase/view_bug.o?bug_id=6662431
#CONFIGURE_ARGS += --enable-luit

# xterm doesn't rely on optimized libs, fasten start# xterm Makefile doesn't have a test target
TEST_TARGET =tup
NOISALIST = 1


include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated: CSWDOCS=README.CSW changelog.CSW
post-install-modulated: DOCS=xterm.log.html ctlseqs.txt
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(addprefix $(FILEDIR)/,$(CSWDOCS)) $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS))    $(DOCDEST