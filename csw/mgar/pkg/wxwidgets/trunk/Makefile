# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = wxWidgets
GARVERSION = 2.8.10
CATEGORIES = lib
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
PACKAGING_PLATFORMS = solaris8-sparc solaris8-i386 solaris9-sparc solaris9-i386

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 2.8.5 2.8.10
MERGE_SCRIPTS_isa-i386-garversion-2.8.5 = copy-only
MERGE_DIRS_isa-i386-garversion-2.8.5 = $(libdir)
MERGE_SCRIPTS_isa-sparcv8-garversion-2.8.5 = copy-only
MERGE_DIRS_isa-sparcv8-garversion-2.8.5 = $(libdir)
MERGE_SCRIPTS_isa-i386-garversion-2.8.10 = copy-all
MERGE_SCRIPTS_isa-sparcv8-garversion-2.8.10 = copy-all

SOURCEFILES = $(foreach VERSION,$(MODULATIONS_GARVERSION),$(GARNAME)-$(VERSION).tar.gz)
NOEXTRACT = $(filter-out $(GARNAME)-$(GARVERSION).tar.gz,$(SOURCEFILES))
SPKG_SOURCEURL = http://www.wxwidgets.org/
MASTER_SITES  = $(SF_MIRRORS)
SF_PROJ = wxwindows

PATCHFILES_isa-i386-garversion-2.8.5  = 0500-wxT-macro-first-iteration.patch
PATCHFILES_isa-i386-garversion-2.8.5 += 0501-a-possible-fix-to-wxchar.h.patch
PATCHFILES_isa-i386-garversion-2.8.5 += 0002-Fixing-retarded-checks-for-libGL.patch
PATCHFILES_isa-i386-garversion-2.8.5 += 0003-vsscanf-support-via-ncursesw.patch
PATCHFILES_isa-sparcv8-garversion-2.8.5  = 0500-wxT-macro-first-iteration.patch
PATCHFILES_isa-sparcv8-garversion-2.8.5 += 0501-a-possible-fix-to-wxchar.h.patch
PATCHFILES_isa-sparcv8-garversion-2.8.5 += 0002-Fixing-retarded-checks-for-libGL.patch
PATCHFILES_isa-sparcv8-garversion-2.8.5 += 0003-vsscanf-support-via-ncursesw.patch
PATCHFILES_isa-i386-garversion-2.8.10  = 0001-Patches-from-http-trac.wxwidgets.org-ticket-10660.patch
PATCHFILES_isa-i386-garversion-2.8.10 += 0002-Fixing-retarded-checks-for-libGL.patch
PATCHFILES_isa-i386-garversion-2.8.10 += 0003-vsscanf-support-via-ncursesw.patch
PATCHFILES_isa-sparcv8-garversion-2.8.10  = 0001-Patches-from-http-trac.wxwidgets.org-ticket-10660.patch
PATCHFILES_isa-sparcv8-garversion-2.8.10 += 0002-Fixing-retarded-checks-for-libGL.patch
PATCHFILES_isa-sparcv8-garversion-2.8.10 += 0003-vsscanf-support-via-ncursesw.patch
DISTFILES  = $(SOURCEFILES)
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES  = CSWwxwidgetscommon
PACKAGES += CSWwxwidgetsdevel
PACKAGES += CSWwxwidgetsgtk2
ARCHALL_CSWwxwidgetsdevel  = 1
SPKG_DESC_CSWwxwidgetscommon = A cross-platform toolkit, common files
SPKG_DESC_CSWwxwidgetsdevel = A cross-platform toolkit, header files
SPKG_DESC_CSWwxwidgetsgtk2 = A cross-platform toolkit, gtk2 support

REQUIRED_PKGS  = CSWexpat
REQUIRED_PKGS += CSWfconfig
REQUIRED_PKGS += CSWftype2
REQUIRED_PKGS += CSWggettextrt
REQUIRED_PKGS += CSWglib2
REQUIRED_PKGS += CSWgtk2
REQUIRED_PKGS += CSWiconv
REQUIRED_PKGS += CSWjpeg
REQUIRED_PKGS += CSWlibatk
REQUIRED_PKGS += CSWlibsm
REQUIRED_PKGS += CSWlibxext
REQUIRED_PKGS += CSWmesa
REQUIRED_PKGS += CSWpango
REQUIRED_PKGS += CSWpng
REQUIRED_PKGS += CSWtiff
REQUIRED_PKGS += CSWzlib

REQUIRED_PKGS_CSWwxwidgetsgtk2 = CSWwxwidgetscommon
REQUIRED_PKGS_CSWwxwidgetsdevel = CSWwxwidgetscommon

PREREQUISITE_PKGS  = $(REQUIRED_PKGS)
PREREQUISITE_PKGS += CSWgtk2devel
PREREQUISITE_PKGS += CSWlibpthreadstubs
PREREQUISITE_PKGS += CSWxproto
PREREQUISITE_PKGS += CSWkbproto
PREREQUISITE_PKGS += CSWlibxcb
PREREQUISITE_PKGS += CSWlibxcbdevel
PREREQUISITE_PKGS += CSWlibxau
PREREQUISITE_PKGS += CSWlibxaudevel
PREREQUISITE_PKGS += CSWlibxrenderdevel
PREREQUISITE_PKGS += CSWrenderproto
PREREQUISITE_PKGS += SUNWxwinc

PKGFILES_CSWwxwidgetsdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWwxwidgetsdevel += /opt/csw/bin/wx-config
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
EXTRA_LINKER_FLAGS += /opt/csw/lib/libncursesw.so

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
CONFIGURE_ARGS_garversion-2.8.5 = --enable-monolithic
CONFIGURE_ARGS += $(CONFIGURE_ARGS_garversion-$(GARVERSION))

INSTALL_SCRIPTS = wxwidgets

include gar/category.mk

install-wxwidgets:
	(cd $(WORKSRC); $(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) install)
	(cd $(WORKSRC)/contrib; $(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) install)
	@$(MAKECOOKIE)
