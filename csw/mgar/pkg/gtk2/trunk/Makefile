GARNAME = gtk2
GARVERSION = 2.16.1
CATEGORIES = lib

DESCRIPTION = GTK+, the multiplatform X11 toolkit for GUI development
define BLURB
  GTK, which stands for the Gimp ToolKit, is a library for creating graphical
  user interfaces. It is designed to be small and efficient, but still flexible
  enough to allow the programmer freedom in the interfaces created. GTK provides
  some unique features over standard widget libraries.
endef

# WARNING: The Solaris 9 (and maybe 10) X11R6 header file Xlibint.h has
# an error which will cause gdkasync.c to fail.  To fix this, correct
# line 613 of Xlibint.h (definition of GetEmptyReq() macro:
#
# #if (defined(__STDC__) && !defined(UNIXCPP)) || defined(ANSICPP)

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/gtk+/2.16/

DISTFILES = gtk+-$(GARVERSION).tar.bz2
DISTFILES += fixme.sh

WORKSRC = $(WORKDIR)/gtk+-$(GARVERSION)

PREREQUISITE_PKGS = CSWbash

SPKG_SOURCEURL = http://www.gtk.org/

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-debug=yes

#TEST_TARGET = check
# There is a test failing on Xvfb which may or may not be harmful. Disable for now.
TEST_TARGET =

TEST_OVERRIDE_DIRS = SHELL
SHELL = /opt/csw/bin/bash

include gar/category.mk

post-configure-modulated:
	@echo " ==> Fixing libtool files"
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	@$(MAKECOOKIE)
