# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = rxvt-unicode
VERSION = 9.20
CATEGORIES = apps
GARTYPE = 

DESCRIPTION = A VT102 emulator for the X window system (pron. ouR XVT, unicode)
define BLURB
  rxvt-unicode, is a colour vt102 terminal emulator intended as an xterm(1)
  replacement for users who do not require features such as Tektronix 4014
  emulation and toolkit-style configurability. As a result, rxvt-unicode uses
  much less swap space -- a significant advantage on a machine serving many
  X sessions.

  Documentation is available at:
  http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod
end= http://dist.schmorp.de/rxvt-unicode/
DISTFILES = $(NAME)-$(VERSION).tar.bz2
DISTFILES += urxvt-wrapper
VENDOR_URL = http://software.schmorp.de/pkg/rxvt-unicode.html
GARCOMPILER = GNU

PACKAGES = CSWrxvt-unicode CSWterminfo-rxvt-unicode
SPKG_DESC_CSWrxvt-unicode = $(DESCRIPTION)
SPKG_DESC_CSWterminfo-rxvt-unicode = Entries for rxvt-unicode in terminal information database
ARCHALL_CSWterminfo-rxvt-unicode = 1
PKGFILES_CSWterminfo-rxvt-unicode = $(datadir)/terminfo.*

EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib
EXTRA_PKG_CONFIG_DIRS = /opt/csw/X11/lib
PATCHFILES += 0001-remove-old-solaris-fix.patch
PATCHFILES += 0002-hardcode-missing-constant.patch
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-perl
CONFIGURE_ARGS += --with-terminfo=/opt/csw/share/terminfo
EXTRA_LDFLAGS  = -Wl,-zignore -Wl,-zcombreloc -Wl,-Bdirect
EXTRA_LINKER_FLAGS = -lrt

BUILD_DEP_PKGS += CSWncurses
RUNTIME_DEP_PKGS_CSWrxvt-unicode += CSWlibintl8
RUNTIME_DEP_PKGS_CSWrxvt-unicode += CSWlibxft2
RUNTIME_DEP_PKGS_CSWrxvt-unicode += CSWlibxrender
RUNTIME_DEP_PKGS_CSWrxvt-unicode += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWrxvt-unicode += CSWstartupnotif
RUNTIME_DEP_PKGS_CSWrxvt-unicode += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWrxvt-unicode += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWrxvt-unicode += CSWterminfo
RUNTIME_DEP_PKGS_CSWrxvt-unicode += CSWterminfo-rxvt-unicode
CHECKPKG_OVERRIDES_CSWrxvt-unicode += surplus-dependency|CSWterminfo
CHECKPKG_OVERRIDES_CSWrxvt-unicode += surplus-dependency|CSWterminfo-rxvt-unicode
OBSOLETED_BY_CSWrxvt-unicode = CSWurxvt= /opt/csw/X11/lib

include gar/category.mk

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)$(libexecdir)
	for b in urxvt urxvtd urxvtc; do \
	  mv $(DESTDIR)$(bindir)/$${b} $(DESTDIR)$(libexecdir); \
	  ln -s ../libexec/urxvt-wrapper $(DESTDIR)$(bindir)/$${b}; \
	done
	ginstall -m 755 $(FILEDIR)/urxvt-wrapper $(DESTD/opt/csw/bin/tic -x -s -o $(DESTDIR)$(datadir)/terminfo $(WORKSRC)/doc/etc/rxvt-unicode.terminfo
	@$(MAKECOOKIE)
