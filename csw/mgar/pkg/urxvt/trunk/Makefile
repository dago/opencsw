# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = rxvt-unicode
VERSION = 9.07
CATEGORIES = apps

DESCRIPTION = A VT102 emulator for the X window system (pron. ouR XVT, unicode)
define BLURB
  rxvt-unicode, is a colour vt102 terminal emulator intended as an xterm(1)
  replacement for users who do not require features such as Tektronix 4014
  emulation and toolkit-style configurability. As a result, rxvt-unicode uses
  much less swap space -- a significant advantage on a machine serving many
  X sessions.

  Documentation is available at:
  http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod
endef

MASTER_SITES         = http://dist.schmorp.de/rxvt-unicode/
DISTFILES            = $(NAME)-$(VERSION).tar.bz2
DISTFILES           += urxvt-wrapper
UFILES_REGEX         = $(NAME)-(\d+(?:\.\d+)*).tar.bz2
SPKG_SOURCEURL       = http://software.schmorp.de/pkg/rxvt-unicode.html
PACKAGES             = CSWurxvt
CATALOGNAME_CSWurxvt = urxvt
CONFIGURE_ARGS       = $(DIRPATHS)
CONFIGURE_ARGS      += --disable-perl
CONFIGURE_ARGS      += --with-terminfo=/opt/csw/share/terminfo
# Because of terminfo
RUNTIME_DEP_PKGS_CSWurxvt += CSWncurses
# Shared library dependencies
RUNTIME_DEP_PKGS_CSWurxvt += CSWfconfig
RUNTIME_DEP_PKGS_CSWurxvt += CSWftype2
RUNTIME_DEP_PKGS_CSWurxvt += CSWlibx11
RUNTIME_DEP_PKGS_CSWurxvt += CSWlibxft2
RUNTIME_DEP_PKGS_CSWurxvt += CSWlibxrender
GARCOMPILER = GNU
EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib
EXTRA_PKG_CONFIG_DIRS = /opt/csw/X11/lib

include gar/category.mk

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)$(libexecdir)
	for b in urxvt urxvtd urxvtc; do \
	  mv $(DESTDIR)$(bindir)/$${b} $(DESTDIR)$(libexecdir); \
	  ln -s ../libexec/urxvt-wrapper $(DESTDIR)$(bindir)/$${b}; \
	done
	ginstall -m 755 $(FILEDIR)/urxvt-wrapper $(DESTDIR)$(libexecdir)
	@$(MAKECOOKIE)
