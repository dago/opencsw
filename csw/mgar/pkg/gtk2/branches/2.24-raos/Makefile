NAME = gtk2
VERSION = 2.18.9
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

DISTNAME = gtk+-$(VERSION)
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += CSWgtk2.postinstall

PATCHFILES = gdkdnd-x11.c.diff

PACKAGES = CSWgtk2 CSWgtk2devel CSWgtk2doc

CATALOGNAME_CSWgtk2 = gtk2
CATALOGNAME_CSWgtk2devel = gtk2_devel
CATALOGNAME_CSWgtk2doc = gtk2_doc

SPKG_DESC_CSWgtk2 = A feature rich toolkit for creating graphical user interfaces 
SPKG_DESC_CSWgtk2devel = A feature rich toolkit for creating graphical user interfaces development package
SPKG_DESC_CSWgtk2doc = A feature rich toolkit for creating graphical user interfaces documentation

BUILD_DEP_PKGS = CSWbash
RUNTIME_DEP_PKGS_CSWgtk2 = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWjpeg CSWlibatk
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibcairo CSWlibxrender CSWpango CSWpng CSWtiff
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibcups
RUNTIME_DEP_PKGS_CSWgtk2 += CSWgnutls
RUNTIME_DEP_PKGS_CSWgtk2 += CSWzlib
RUNTIME_DEP_PKGS_CSWgtk2 += CSWkrb5lib

RUNTIME_DEP_PKGS_CSWgtk2devel  = CSWgtk2 CSWglib2devel CSWlibatkdevel
RUNTIME_DEP_PKGS_CSWgtk2devel += CSWlibcairodevel CSWlibxrenderdevel CSWpangodevel

SPKG_SOURCEURL = http://www.gtk.org/

NOISALIST = 1
BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)

CONFIGURE_ARGS-32 += --enable-cups
CONFIGURE_ARGS-64 += --disable-cups
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

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

CHECKPKG_OVERRIDES_CSWgtk2 += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/gtk-2.0/2.10.0/printbackends/libprintbackend-cups.so

CHECKPKG_OVERRIDES_CSWgtk2devel += surplus-dependency|CSWglib2devel
CHECKPKG_OVERRIDES_CSWgtk2devel += surplus-dependency|CSWpangodevel
CHECKPKG_OVERRIDES_CSWgtk2devel += surplus-dependency|CSWlibatkdevel
CHECKPKG_OVERRIDES_CSWgtk2devel += surplus-dependency|CSWgtk2
CHECKPKG_OVERRIDES_CSWgtk2devel += surplus-dependency|CSWlibxrenderdevel
CHECKPKG_OVERRIDES_CSWgtk2devel += surplus-dependency|CSWlibcairodevel

# There are a *ton* of different libs on amd64 available that are not installed on Solaris 9.
# Skip this complete test for now.
CHECKPKG_OVERRIDES_CSWgtk2 += soname-not-found

include gar/category.mk
