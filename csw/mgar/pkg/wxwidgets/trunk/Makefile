# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME    = wxWidgets
VERSION = 2.8.12
CATEGORIES = lib
GARTYPE = v2
define BLURB
  wxWidgets lets developers create applications for Win32, Mac OS X, GTK+, X11,
  Motif, WinCE, and more using one codebase. It can be used from languages such
  as C++, Python, Perl, and C#/.NET. Unlike other cross-platform toolkits,
  wxWidgets applications look and feel native. This is because wxWidgets uses
  the platform's own native controls rather than emulatDISTFILES  = $(NAME)-$(VERSION).tar.bz2
.8.so.VENDOR_URL = http://www.wxwidgets.org/
MASTER_SITES    = $(SF_MIRRORS)
SF_PROJECT      = wxwindows

PACKAGES  = CSWwxwidgets
PACKAGES += CSWwxwidgets-dev
PACKAGES += CSWwxwidgetsgtk2

SPKG_DESC_CSWwxwidgets     = A cross-platform toolkit
SPKG_DESC_CSWwxwidgets-dev = A cross-platform toolkit, header files
SPKG_DESC_CSWwxwidgetsgtk2 = A cross-platform toolkit, gtk2 support

RUNTIME_DEP_PKGS_CSWwxwidgets += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWwxwidgets += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWwxwidgets += CSWlibz1

RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWwxwidgets
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibmspack0
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWmesa
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2 += CSWpango

RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWwxwidgets
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWwxwidgetsgtk2
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWintltool
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWpkgconfig
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWlibgtk2-dev
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWlibpcre-dev
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWfontconfig-dev
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWlibfreetype-dev
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWlibpng-dev
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWsunx11devel
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWlibiconv-dev
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWggettext-dev
RUNTIME_DEP_PKGS_CSWwxwidgets-dev += CSWlibexpat-dev

BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWintltool
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWfontconfig-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWsunx11devel
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWlibexpat-dev

# Easier than defining each individual .so.xxx
PKGFILES_CSWwxwidgets     = $(libdir).*libwx_base.*\.so\..*
PKGFILES_CSWwxwidgets    += $(sharedir)/locale.*

PKGFILES_CSWwxwidgetsgtk2 = $(libdir).*libwx_gtk2.*\.so\..*

PKGFILES_CSWwxwidgets-dev = $(PKGFILES_DEVEL)

CATALOGNAME_CSWwxwidgets       = wxwidgets
CATALOGNAME_CSWwxwidgets-dev   = wxwidgets_dev
CATALOGNAME_CSWwxwidgetsgtk2   = wxwidgetsgtk2
CATALOGNAME_CSWwxwidgetsdevel  = wxwidgets_devel_stub 
CATALOGNAME_CSWwxwidgetscommon = wxwidgets_common_stub

OBSOLETED_BY_CSWwxwidgets     = CSWwxwidgetscommon
OBSOLETED_BY_CSWwxwidgets-dev = CSWwxwidgetsdevel

TEST_SCRIPTS =

BUILD64 = 1LAGS += -lsunmath

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-gtk=2
CONFIGURE_ARGS += --with-gtk-prefix=/opt/csw
CONFIGURE_ARGS += --with-regex
CONFIGURE_ARGS += --with-opengl
CONFIGURE_ARGS += CONFIGURE_ARGS += --enable-printarch=no
CONFIGURE_ARGS += --with-gnomeprint=no

# -norunpath is needed for LDFLAGS as CC is used as linker. Not cc, so no
# problem with it being a C++compiler parameter
EXTRA_CFLAGS     += -xnorunpath
EXTRA_CXXFLAGS   += -norunpath
EXTRA_LDFLAGS    += -norunpath
EXTRA_LD_OPTIONS += -z nolazyload -B direct

# wxWidget contains a bunch of .so, let's keep them together as one big
# happy family
CHECKPKG_OVERRIDES_CSWwxwidgets     = shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWwxwidgetsgtk2 = shared-lib-pkgname-mismatch

# Only samples inside code comments, can be safely ignored at this point
CHECKPKG_OVERRIDES_CSWwxwidgets-dev += file-with-bad-content|/usr/share|root/opt/csw/include/wx-2.8/wx/utils.h
CHECKPKG_OVERRIDES_CSWwxwidgets-dev += file-with-bad-content|/usr/local|root/opt/csw/include/wx-2.8/wx/unix/stdpaths.h
CHECKPKG_OVERRIDES_CSWwxwidgets-dev += file-with-bad-content|/usr/local|root/opt/csw/include/wx-2.8/wx/generic/helpext.h

LICENSE = docs/licence.txt

include gar/category.mk
