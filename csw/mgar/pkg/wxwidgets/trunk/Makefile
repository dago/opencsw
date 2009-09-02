# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = wxWidgets
GARVERSION = 2.8.10
CATEGORIES = lib
DESCRIPTION = A portable widget library
define BLURB
endef
SPKG_SOURCEURL = http://www.wxwidgets.org/
MASTER_SITES  = $(SF_MIRRORS)
SF_PROJ = wxwindows
PATCHFILES  = 0001-Patches-from-http-trac.wxwidgets.org-ticket-10660.patch
PATCHFILES += 0002-Fixing-retarded-checks-for-libGL.patch
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
CATALOGNAME = wxwidgets
PACKAGES  = CSWwxwidgetscommon
PACKAGES += CSWwxwidgetsdevel
PACKAGES += CSWwxwidgetsgtk2
ARCHALL_CSWwxwidgetsdevel  = 1
REQUIRED_PKGS  = CSWexpat
REQUIRED_PKGS += CSWfconfig
REQUIRED_PKGS += CSWftype2
REQUIRED_PKGS += CSWggettextrt
REQUIRED_PKGS += CSWglib2
REQUIRED_PKGS += CSWgtk2
REQUIRED_PKGS += CSWiconv
REQUIRED_PKGS += CSWjpeg
REQUIRED_PKGS += CSWlibatk
REQUIRED_PKGS += CSWmesa
REQUIRED_PKGS += CSWpango
REQUIRED_PKGS += CSWpng
REQUIRED_PKGS += CSWtiff
REQUIRED_PKGS += CSWzlib

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
PKGFILES_CSWwxwidgetsgtk2  = /opt/csw/lib/wx/(include|config)/gtk2-.*
PKGFILES_CSWwxwidgetsgtk2 += /opt/csw/lib/libwx_gtk2.*
PKGFILES_CSWwxwidgetsgtk2 += /opt/csw/bin/wx(-config|rc(|-2.8))

REQUIRED_PKGS_CSWwxwidgetsgtk2 = CSWwxwidgetscommon
REQUIRED_PKGS_CSWwxwidgetsdevel = CSWwxwidgetscommon

CATALOGNAME_CSWwxwidgetscommon = wxwidgets_common
CATALOGNAME_CSWwxwidgetsdevel  = wxwidgets_devel
CATALOGNAME_CSWwxwidgetsgtk2   = wxwidgets_gtk2
TEST_SCRIPTS =
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-gtk=2
CONFIGURE_ARGS += --with-gtk-prefix=/opt/csw
CONFIGURE_ARGS += --without-regex
CONFIGURE_ARGS += --with-opengl
# Unicode-enabled build on Solaris 8 fails with:
# "./src/common/wxchar.cpp", line 1693: Error: The function "vswscanf" must have
# a prototype.
# Building Unicode support for Solaris 9 and 10 only.
CONFIGURE_ARGS_5.8  = --disable-unicode
CONFIGURE_ARGS_5.9  = --enable-unicode
CONFIGURE_ARGS_5.10 = --enable-unicode
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GAROSREL))
EXTRA_CFLAGS = -fast -xstrconst -xnolibmopt
EXTRA_INC = /opt/csw/X11/include /usr/X11/include /usr/openwin/share/include
EXTRA_LIB = /opt/csw/X11/lib
PKG_CONFIG_PATH = /opt/csw/lib/pkgconfig:/opt/csw/X11/lib/pkgconfig

INSTALL_SCRIPTS = wxwidgets

install-wxwidgets:
	(cd $(WORKSRC); $(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) install)
	(cd $(WORKSRC)/contrib; $(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) install)
	@$(MAKECOOKIE)

include gar/category.mk
