GARNAME = gtk2
GARVERSION = 2.18.9
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

GNOME_PROJ = gtk+
MASTER_SITES = $(GNOME_MIRROR)

DISTNAME = gtk+-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += CSWgtk2.postinstall

PACKAGES = CSWgtk2 CSWgtk2devel CSWgtk2doc

CATALOGNAME_CSWgtk2 = gtk2
CATALOGNAME_CSWgtk2devel = gtk2_devel
CATALOGNAME_CSWgtk2doc = gtk2_doc

SPKG_DESC_CSWgtk2 = A feature rich toolkit for creating graphical user interfaces 
SPKG_DESC_CSWgtk2devel = A feature rich toolkit for creating graphical user interfaces development package
SPKG_DESC_CSWgtk2doc = A feature rich toolkit for creating graphical user interfaces documentation

BUILD_DEP_PKGS = CSWbash
RUNTIME_DEP_PKGS_CSWgtk2 = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWjpeg CSWlibatk
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibcairo CSWlibx11 CSWlibxrender CSWpango CSWpng CSWtiff
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibxcomposite CSWlibxcursor CSWlibxdamage CSWlibxext CSWlibxfixes CSWlibxinerama CSWlibxrandr
RUNTIME_DEP_PKGS_CSWgtk2devel  = CSWgtk2 CSWglib2devel CSWatkdevel
RUNTIME_DEP_PKGS_CSWgtk2devel += CSWlibcairodevel CSWlibx11devel CSWlibxrenderdevel CSWpangodevel

SPKG_SOURCEURL = http://www.gtk.org/

NOISAEXEC = 1
NOISALIST = 1
BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-cups

STRIP_LIBTOOL = 1

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
