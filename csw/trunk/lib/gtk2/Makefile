GARNAME = gtk2
GARVERSION = 2.4.3
CATEGORIES = lib

DESCRIPTION = A library for creating graphical user interfaces.
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

MASTER_SITES = ftp://ftp.gtk.org/pub/gtk/v2.4/

DISTFILES = gtk+-$(GARVERSION).tar.bz2
WORKSRC = $(WORKDIR)/gtk+-$(GARVERSION)

LIBDEPS += lib/atk
LIBDEPS += lib/pango
LIBDEPS += lib/xcursor
LIBDEPS += xtra/hicolor-icon-theme

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-debug=yes

TEST_TARGET = check

include ../category.mk

CFLAGS := -g $(CFLAGS)
CXXFLAGS := -g $(CXXFLAGS)
export CFLAGS CXXFLAGS
