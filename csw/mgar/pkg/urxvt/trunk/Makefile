# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Header: $

GARNAME = rxvt-unicode
GARVERSION = 9.06
CATEGORIES = apps

DESCRIPTION = (ouR XVT, unicode) - a VT102 emulator for the X window system
define BLURB
  rxvt-unicode, is a colour vt102 terminal emulator intended as an xterm(1)
  replacement for users who do not require features such as Tektronix 4014
  emulation and toolkit-style configurability. As a result, rxvt-unicode uses
  much less swap space -- a significant advantage on a machine serving many
  X sessions.

  Documentation is available at:
  http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod
endef

MASTER_SITES = http://dist.schmorp.de/rxvt-unicode/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# PATCHFILES = $(GARNAME)-$(GARVERSION)-solaris8.patch

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2
SPKG_SOURCEURL = http://software.schmorp.de/pkg/rxvt-unicode.html

PACKAGES = CSWurxvt
CATALOGNAME_CSWurxvt = urxvt

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-perl

GARCOMPILER = GNU

REQUIRED_PKGS_CSWurxvt = CSWfconfig CSWftype2 CSWlibxft2 CSWlibxrender CSWzlib
TEST_SCRIPTS =

include gar/category.mk
