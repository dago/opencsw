# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = wxWidgets
VERSION = 2.8.10
CATEGORIES = lib
GARTYPE = v2
define BLURB
  wxWidgets lets developers create applications for Win32, Mac OS X, GTK+, X11,
  Motif, WinCE, and more using one codebase. It can be used from languages such
  as C++, Python, Perl, and C#/.NET. Unlike other cross-platform toolkits,
  wxWidgets applications look and feel native. This is because wxWidgets uses
  the platform's own native controls rather than emulating them.
endef

# The unicode version can't be currently built on Solaris 8.  Doing separate
# builds on Solaris 8 and Solaris 9.  Unicode support will start in Solaris 9.
# More details below, look for 'unicode'.
# PACKAGING_PLATFORMS = solaris8-sparc solaris8-i386

EXTRA_MODULATORS = VERSION

# Once upon a time, this build also supported the version 2.8.5 for backward
# compatibility. Unfortunately, it was segfaulting.  As a workaround, binary
# files copied from the old package have been provided.
MODULATIONS_VERSION = 2.8.10

MERGE_SCRIPTS_isa-i386-version-2.8.5 = copy-only
MERGE_DIRS_isa-i386-version-2.8.5 = $(libdir)
MERGE_SCRIPTS_isa-sparcv8-version-2.8.5 = copy-only
MERGE_DIRS_isa-sparcv8-version-2.8.5 = $(libdir)
MERGE_SCRIPTS_isa-i386-version-2.8.10 = copy-all
MERGE_SCRIPTS_isa-sparcv8-version-2.8.10 = copy-all

SOURCEFILES = $(foreach VERSION,$(MODULATIONS_VERSION),$(NAME)-$(VERSION).tar.gz)
NOEXTRACT = $(filter-out $(NAME)-$(VERSION).tar.gz,$(SOURCEFILES))
DISTFILES  = $(SOURCEFILES)
DISTFILES += libwx_gtk2u-2.8.so.0.2.0-i386
DISTFILES += libwx_gtk2u-2.8.so.0.2.0-sparc
DISTFILES += libwx_gtk2u_gl-2.8.so.0.2.0-i386
DISTFILES += libwx_gtk2u_gl-2.8.so.0.2.0-sparc
SPKG_SOURCEURL = http://www.wxwidgets.org/
MASTER_SITES  = $(SFECT_MIRRORS)
SF_PROJ = wxwindows


PATCHFILES_isa-i386-version-2.8.5  = 0500-wxT-macro-first-iteration.patch
PATCHFILES_isa-i386-version-2.8.5 += 0501-a-possible-fix-to-wxchar.h.patch
PATCHFILES_isa-i386-version-2.8.5 += 0002-Fixing-retarded-checks-for-libGL.patch
PATCHFILES_isa-i386-version-2.8.5 += 0003-vsscanf-support-via-ncursesw.patch
PATCHFILES_isa-i386-version-2.8.5 += 0004-add-monodll_appbase.so-to-wxrc.patch
PATCHFILES_isa-i386-version-2.8.5 += 0005-stupid-vwscanf-workaround.patch
PATCHFILES_isa-sparcv8-version-2.8.5  = 0500-wxT-macro-first-iteration.patch
PATCHFILES_isa-sparcv8-version-2.8.5 += 0501-a-possible-fix-to-wxchar.h.patch
PATCHFILES_isa-sparcv8-version-2.8.5 += 0002-Fixing-retarded-checks-for-libGL.patch
PATCHFILES_isa-sparcv8-version-2.8.5 += 0003-vsscanf-support-via-ncursesw.patch
PATCHFILES_isa-sparcv8-version-2.8.5 += 0004-add-monodll_appbase.so-to-wxrc.patch
PATCHFILES_isa-sparcv8-version-2.8.5 += 0005-stupid-vwscanf-workaround.patch
PATCHFILES_isa-i386-version-2.8.10  = 0001-Patches-from-http-trac.wxwidgets.org-ticket-10660.patch
PATCHFILES_isa-i386-version-2.8.10 += 0002-Fixing-retarded-checks-for-libGL.patch
PATCHFILES_isa-i386-version-2.8.10 += 0003-vsscanf-support-via-ncursesw.patch
PATCHFILES_isa-i386-version-2.8.10 += 0005-stupid-vwscanf-workaround.patch
PATCHFILES_isa-sparcv8-version-2.8.10  = 0001-Patches-from-http-trac.wxwidgets.org-ticket-10660.patch
PATCHFILES_isa-sparcv8-version-2.8.10 += 0002-Fixing-retarded-checks-for-libGL.patch
PATCHFILES_isa-sparcv8-version-2.8.10 += 0003-vsscanf-support-via-ncursesw.patch
PATCHFILES_isa-sparcv8-version-2.8.10 += 0005-stupid-vwscanf-workaround.patch
PACKAGES  = CSWwxwidgetscommon
PACKAGES += CSWwxwidgetsdevel
PACKAGES += CSWwxwidgetsgtk2
SPKG_DESC_CSWwxwidgetscommon = A cross-platform toolkit, common files
SPKG_DESC_CSWwxwidgetsdevel  = A cross-platform toolkit, header files
SPKG_DESC_CSWwxwidgetsgtk2   = A cross-platform toolkit, gtk2 support

RUNTIME_DEP_PKGS_CSWwxwidgetscommon += CSWexpat
RUNTIME_DEP_PKGS_CSWwxwidgetscommon += CSWiconv
RUNTIME_DEP_PKGS_CSWwxwidgetscommon += CSWlibxext
RUNTIME_DEP_PKGS_CSWwxwidgetscommon += CSWncurses
RUNTIME_DEP_PKGS_CSWwxwidgetscommon += CSWsunmath
RUNTIME_DEP_PKGS_CSWwxwidgetscommon += CSWzlib
RUNTIME_DEP_PKGS_CSWwxwidgetsdevel += CSWexpat
RUNTIME_DEP_PKGS_CSWwxwidgetsdevel += CSWiconv
RUNTIME_DEP_PKGS_CSWwxwidgetsdevel += CSWlibxext
RUNTIME_DEP_PKGS_CSWwxwidgetsdevel += CSWncurses
RUNTIME_DEP_PKGS_CSWwxwidgetsdevel += CSWsunmath
RUNTIME_DEP_PKGS_CSWwxwidgetsdevel += CSWzlib
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWexpat
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWftype2
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWggettextrt
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWglib2
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWgtk2
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWiconv
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWjpeg
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibatk
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibsm
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibxext
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWmesa
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWncurses
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWpango
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWpng
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWsunmath
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWtiff
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWzlib


# Dependencies between wxwidgets subpackages
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2  += CSWwxwidgetscommon
RUNTIME_DEP_PKGS_CSWwxwidgetsdevel += CSWwxwidgetscommon CSWwxwidgetsgtk2

BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWgtk2devel
BUILD_DEP_PKGS += CSWlibpthreadstubs
BUILD_DEP_PKGS += CSWxproto
BUILD_DEP_PKGS += CSWkbproto
BUILD_DEP_PKGS += CSWlibxcb
BUILD_DEP_PKGS += CSWlibxcbdevel
BUILD_DEP_PKGS += CSWlibxau
# BUILD_DEP_PKGS += CSWlibxaudevel
BUILD_DEP_PKGS += CSWlibxrenderdevel
# BUILD_DEP_PKGS += CSWrenderproto
BUILD_DEP_PKGS += SUNWxwinc

PKGFILES_CSWwxwidgetsdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWwxwidgetsdevel += /opt/csw/bin/wx-config
PKGFILES_CSWwxwidgetsdevel += /opt/csw/share/bakefile/presets.*
PKGFILES_CSWwxwidgetsdevel += /opt/csw/share/aclocal.*
PKGFILES_CSWwxwidgetsdevel += /opt/csw/bin/wx-config
PKGFILES_CSWwxwidgetsdevel += /opt/csw/bin/wxrc=wxrc-2.8
PKGFILES_CSWwxwidgetsdevel += /opt/csw/bin/wxrc-2.8
PKGFILES_CSWwxwidgetsdevel += /opt/csw/lib/wx/config.*
PKGFILES_CSWwxwidgetsdevel += /opt/csw/lib/wx/include.*
PKGFILES_CSWwxwidgetsgtk2  = /opt/csw/lib/wx/(include|config)/gtk2-.*
PKGFILES_CSWwxwidgetsgtk2 += /opt/csw/lib/libwx_gtk2.*
PKGFILES_CSWwxwidgetsgtk2 += /opt/csw/bin/wx(-config|rc(|-2.8))

CATALOGNAME_CSWwxwidgetscommon = wxwidgets_common
CATALOGNAME_CSWwxwidgetsdevel  = wxwidgets_devel
CATALOGNAME_CSWwxwidgetsgtk2   = wxwidgets_gtk2
TEST_SCRIPTS =

# To fix a problem with unresolved symbols
EXTRA_LINKER_FLAGS  = /usr/openwin/lib/libXext.so
# For vsscanf support
# EXTRA_LINKER_FLAGS += /opt/csw/lib/libncursesw.so
EXTRA_LINKER_FLAGS += -lncursesw
# To fix the __sincos problem on x86
EXTRA_LINKER_FLAGS += -lsunmath

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-gtk=2
CONFIGURE_ARGS += --with-gtk-prefix=/opt/csw
CONFIGURE_ARGS += --with-regex
CONFIGURE_ARGS += --with-opengl
CONFIGURE_ARGS += --enable-unicode
EXTRA_CFLAGS = -fast -xstrconst -xnolibmopt -D__EXTENSIONS__
EXTRA_CXXFLAGS = -fast -xstrconst -xnolibmopt -D__EXTENSIONS__
EXTRA_INC = /opt/csw/X11/include /usr/X11/include /usr/openwin/share/include
EXTRA_LIB = /opt/csw/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# The 2.8.5 version has been compiled as a monolithic library.  Building it the
# same way for backwards compatibility.
CONFIGURE_ARGS_version-2.8.5 = --enable-monolithic
CONFIGURE_ARGS += $(CONFIGURE_ARGS_version-$(VERSION))

INSTALL_SCRIPTS = wxwidgets

LICENSE = docs/licence.txt

include gar/category.mk

install-wxwidgets:
	(cd $(WORKSRC); $(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) install)
	(cd $(WORKSRC)/contrib; $(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) install)
	@$(MAKECOOKIE)

post-merge:
	ginstall -m 755 \
	  $(FILEDIR)/libwx_gtk2u-2.8.so.0.2.0-$(GARCH) \
	  $(PKGROOT)$(libdir)/libwx_gtk2u-2.8.so.0.2.0
	ginstall -m 755 \
	  $(FILEDIR)/libwx_gtk2u_gl-2.8.so.0.2.0-$(GARCH) \
	  $(PKGROOT)$(libdir)/libwx_gtk2u_gl-2.8.so.0.2.0