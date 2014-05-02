# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = rxvt-unicode
VERSION = 9.07
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
PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc
GARCOMPILER = GNU

PATCHFILES += rxvt-unicode-9.06-solaris8.patch
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-perl
CONFIGURE_ARGS += --with-terminfo=/opt/csw/share/terminfo

PACKAGES = CSWrxvt-unicode
SPKG_DESC_CSWrxvt-unicode = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWrxvt-unicode += CSWterminfo
CHECKPKG_OVERRIDES_CSWrxvt-unicode += surplus-dependency|CSWterminfo
OBSOLETED_BY_CSWrxvt-unicode = CSWurxvt= /opt/csw/X11/lib

include gar/category.mk

post-install-modulated:
	ginstall -m 755 -d $(DESTDIR)$(libexecdir)
	for b in urxvt urxvtd urxvtc; do \
	  mv $(DESTDIR)$(bindir)/$${b} $(DESTDIR)$(libexecdir); \
	  ln -s ../libexec/urxvt-wrapper $(DESTDIR)$(bindir)/$${b}; \
	done
	ginstall -m 755 $(FILEDIR)/urxvt-wrapper $(DESTDIR)$(libexecdir