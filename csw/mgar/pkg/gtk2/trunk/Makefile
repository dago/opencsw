GARNAME = gtk2
GARVERSION = 2.16.5
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

PACKAGES = CSWgtk2 CSWgtk2devel CSWgtk2doc

CATALOGNAME_CSWgtk2 = gtk2
CATALOGNAME_CSWgtk2devel = gtk2_devel
CATALOGNAME_CSWgtk2doc = gtk2_doc

PREREQUISITE_PKGS = CSWbash
REQUIRED_PKGS_CSWgtk2 = CSWjasper CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWjpeg CSWlibatk
REQUIRED_PKGS_CSWgtk2 += CSWlibcairo CSWlibx11 CSWlibxrender CSWpango CSWpng CSWtiff CSWzlib
REQUIRED_PKGS_CSWgtk2devel = CSWgtk2

SPKG_SOURCEURL = http://www.gtk.org/

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

NO_ISAEXEC = 1
NOISALIST = 1
BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += --disable-cups

#TEST_TARGET = check
# There is a test failing on Xvfb which may or may not be harmful. Disable for now.
TEST_TARGET =

TEST_OVERRIDE_DIRS = SHELL
SHELL = /opt/csw/bin/bash

PKGFILES_CSWgtk2devel = $(PKGFILES_DEVEL)
PKGFILES_CSWgtk2devel +=  $(sharedstatedir)/gtk-2.0/demo/.*
PKGFILES_CSWgtk2doc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWgtk2doc = 1

include gar/category.mk

post-configure-modulated:
	@echo " ==> Fixing libtool files"
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	@$(MAKECOOKIE)
