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
PACKAGES += CSWwxwidgetsrt
ARCHALL_CSWwxwidgetscommon = 1
ARCHALL_CSWwxwidgetsdevel  = 1
ARCHALL_CSWwxwidgetsgtk2   = 1
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
PKGFILES_CSWwxwidgetsdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWwxwidgetsdevel += /opt/csw/lib/wx/include/.*
PKGFILES_CSWwxwidgetsrt = $(PKGFILES_RT)
PKGFILES_CSWwxwidgetsgtk2 = non-existing

REQUIRED_PKGS_CSWwxwidgetsgtk2 = CSWwxwidgetsrt
REQUIRED_PKGS_CSWwxwidgetsrt   = CSWwxwidgetscommon

CATALOGNAME_CSWwxwidgetscommon = wxwidgets_common
CATALOGNAME_CSWwxwidgetsdevel  = wxwidgets_devel
CATALOGNAME_CSWwxwidgetsgtk2   = wxwidgets_gtk2
CATALOGNAME_CSWwxwidgetsrt   = wxwidgets_rt
TEST_SCRIPTS =
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-gtk=2 --with-gtk-prefix=/opt/csw --without-regex
CONFIGURE_ARGS += --disable-unicode --with-opengl
EXTRA_CFLAGS = -fast -xstrconst -xnolibmopt
EXTRA_INC = /opt/csw/X11/include
EXTRA_LIB = /opt/csw/X11/lib
PKG_CONFIG_PATH = /opt/csw/lib/pkgconfig:/opt/csw/X11/lib/pkgconfig

include gar/category.mk
