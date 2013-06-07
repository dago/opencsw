# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = wxWidgets
VERSION = 2.9.3
CATEGORIES = lib
GARTYPE = v2
define BLURB
  wxWidgets lets developers create applications for Win32, Mac OS X, GTK+, X11,
  Motif, WinCE, and more using one codebase. It can be used from languages such
  as C++, Python, Perl, and C#/.NET. Unlike other cross-platform toolkits,
  wxWidgets applications look and feel native. This is because wxWidgets uses
  the platform's own native controls rather than emulatSF_PROJ = wxwindows
MASTER_SITES += $(SF_MIRRORS)

DESCRIPTION = WX Widgets Cross-Platform GUI  Library
DISTFILES += $(DISTNAME).tar.bz2

VENDOR_URL = http://www.wxwidgets.org/

LICENSE = docs/licence.txt2.8.10 = copy-all

SOURCEFILES = $(foreach VERSION,$(MODULATIONS_VERSION),$(NAME)-$(VERSION).tar.gz)
NOEXTRACT = $(filter-out $(NAME)-$(VERSION).tar.gz,$(SOURCEFILES))
DISTFILES  = $(SOURCEFILES)
DISTFILES += libwx_gtk2u-2.8.so.0.2.0-i386
DISTFILES += libwx_gtk2u-2.8.so.0.2.0-sparc
DISTFILES += libwx_gtk2u_gl-2.8.so.0.2.0-i386
DISTFILES += libwx_gtk2u_gl-2.8.so.0.2.0-sparc
SPKG_SOURCEURL = http://www.wxwidgets.org/
MASTER_SITES  = $(SFECT_MIRRORS)
SF_PBUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += SUNWxwinc

#PATCHFILES_isa-i386-version-2.8.5  = 0500-wxT-macro-first-iteration.patch
#PATCHFILES_isa-i386-version-2.8.5 += 0501-a-possible-fix-to-wxchar.h.patch
#o-wxchar.h.patch
PATCHFILES_isa-i386-version-2.8.5 += 0002-Fixing-retarded-checks#-for-libGL.patch
PATCHFILES_isa-i386-version-2.8.5 += 0003-vsscanf-support-vi#PATCHFILES_isa-i386-version-2.8.5 += 0004-add-monodll_appbase.so-to-wxrc.patch
#PATCHFILES_isa-i386-version-2.8.5 += 0005-stupid-vwscanf-workaround.patch
#PATCHFILES_isa-sparcv8-version-2.8.5  = 0500-wxT-macro-first-iteration.patch
#-iteration.patch
PATCHFILES_isa-sparcv8-version-2.8.5 += 0501-a-possible-fix-t#PATCHFILES_isa-sparcv8-version-2.8.5 += 0002-Fixing-retarded-checks-for-libGL.patch
#PATCHFILES_isa-sparcv8-version-2.8.5 += 0003-vsscanf-support-via-ncursesw.patch
#PATCHFILES_isa-sparcv8-version-2.8.5 += 0004-add-monodll_appbase.so-to-wxrc.patch
#so-to-wxrc.patch
PATCHFILES_isa-sparcv8-version-2.8.5 += 0005-stupid-vwscanf-#PATCHFILES_isa-i386-version-2.8.10  = 0001-Patches-from-http-trac.wxwidgets.org-ticket-10660.patch
#PATCHFILES_isa-i386-version-2.8.10 += 0002-Fixing-retarded-checks-for-libGL.patch
#-for-libGL.patch
PATCHFILES_isa-i386-version-2.8.10 += 0003-vsscanf-support-vi#PATCHFILES_isa-i386-version-2.8.10 += 0005-stupid-vwscanf-workaround.patch
#PATCHFILES_isa-sparcv8-version-2.8.10  = 0001-Patches-from-http-trac.wxwidgets.org-ticket-10660.patch
#cket-10660.patch
PATCHFILES_isa-sparcv8-version-2.8.10 += 0002-Fixing-retarded-checks#PATCHFILES_isa-sparcv8-version-2.8.10 += 0003-vsscanf-support-via-ncursesw.patch
#PATCHFILES_isa-sparcv8-version-2.8.10 += 0005-stupid-vwscanf-workaround.patch

#PACKAGES += CSWwxwidgetscommon
CATALOGNAME_CSWwxwidgetscommon = wxwidgets_common_stub
SPKG_DESC_CSWwxwidgetscommon = common

#PACKAGES += CSWwxwidgetsgtk2
CATALOGNAME_CSWwxwidgetsgtk2   = wxwidgets_gtk2_stub
SPKG_DESC_CSWwxwidgetsgtk2 = gtk2

#PACKAGES += CSWwxwidgetsdevel
CATALOGNAME_CSWwxwidgetsdevel  = wxwidgets_devel_stub
SPKG_DESC_CSWwxwidgetsdevel = devel

PACKAGES += CSWlibwx-gtk2u-adv2-9-3
SPKG_DESC_CSWlibwx-gtk2u-adv2-9-3 += $(DESCRIPTION), libwx_gtk2u_adv-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-adv2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_adv-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-adv2-9-3 += CSWlibgio2-0-0

PACKAGES += CSWlibwx-gtk2u-aui2-9-3
SPKG_DESC_CSWlibwx-gtk2u-aui2-9-3 += $(DESCRIPTION), libwx_gtk2u_aui-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-aui2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_aui-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibwx-gtk2u-adv2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-aui2-9-3 += CSWlibglib2-0-0


PACKAGES += CSWlibwx-gtk2u-core2-9-3
SPKG_DESC_CSWlibwx-gtk2u-core2-9-3 += $(DESCRIPTION), libwx_gtk2u_core-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-core2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_core-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-core2-9-3 += CSWlibgio2-0-0

PACKAGES += CSWlibwx-gtk2u-gl2-9-3
SPKG_DESC_CSWlibwx-gtk2u-gl2-9-3 += $(DESCRIPTION), libwx_gtk2u_gl-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-gl2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_gl-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWmesa
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-gl2-9-3 += CSWlibglib2-0-0

PACKAGES += CSWlibwx-gtk2u-html2-9-3
SPKG_DESC_CSWlibwx-gtk2u-html2-9-3 += $(DESCRIPTION), libwx_gtk2u_html-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-html2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_html-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibmspack0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-html2-9-3 += CSWlibglib2-0-0

PACKAGES += CSWlibwx-gtk2u-media2-9-3
SPKG_DESC_CSWlibwx-gtk2u-media2-9-3 += $(DESCRIPTION), libwx_gtk2u_media-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-media2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_media-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWgstplugins
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWgstreamer
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-media2-9-3 += CSWlibglib2-0-0

PACKAGES += CSWlibwx-gtk2u-propgrid2-9-3
SPKG_DESC_CSWlibwx-gtk2u-propgrid2-9-3 += $(DESCRIPTION), libwx_gtk2u_propgrid-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-propgrid2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_propgrid-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibwx-gtk2u-adv2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-propgrid2-9-3 += CSWlibglib2-0-0

PACKAGES += CSWlibwx-gtk2u-qa2-9-3
SPKG_DESC_CSWlibwx-gtk2u-qa2-9-3 += $(DESCRIPTION), libwx_gtk2u_qa-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-qa2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_qa-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibwx-baseu-xml2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-qa2-9-3 += CSWlibglib2-0-0

PACKAGES += CSWlibwx-gtk2u-ribbon2-9-3
SPKG_DESC_CSWlibwx-gtk2u-ribbon2-9-3 += $(DESCRIPTION), libwx_gtk2u_ribbon-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-ribbon2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_ribbon-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibwx-gtk2u-adv2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-ribbon2-9-3 += CSWlibatk1-0-0

PACKAGES += CSWlibwx-gtk2u-richtext2-9-3
SPKG_DESC_CSWlibwx-gtk2u-richtext2-9-3 += $(DESCRIPTION), libwx_gtk2u_richtext-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-richtext2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_richtext-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibwx-gtk2u-html2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibwx-gtk2u-adv2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibwx-baseu-xml2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-richtext2-9-3 += CSWlibglib2-0-0

PACKAGES += CSWlibwx-gtk2u-stc2-9-3
SPKG_DESC_CSWlibwx-gtk2u-stc2-9-3 += $(DESCRIPTION), libwx_gtk2u_stc-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-stc2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_stc-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-stc2-9-3 += CSWlibatk1-0-0

PACKAGES += CSWlibwx-gtk2u-xrc2-9-3
SPKG_DESC_CSWlibwx-gtk2u-xrc2-9-3 += $(DESCRIPTION), libwx_gtk2u_xrc-2.9.so.3
PKGFILES_CSWlibwx-gtk2u-xrc2-9-3 += $(call pkgfiles_lib,libwx_gtk2u_xrc-2.9.so.3)
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibwx-gtk2u-html2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibwx-gtk2u-adv2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibwx-baseu-xml2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-gtk2u-xrc2-9-3 += CSWlibglib2-0-0

PACKAGES += CSWlibwx-baseu2-9-3
SPKG_DESC_CSWlibwx-baseu2-9-3 += $(DESCRIPTION), libwx_baseu-2.9.so.3
PKGFILES_CSWlibwx-baseu2-9-3 += $(call pkgfiles_lib,libwx_baseu-2.9.so.3)
RUNTIME_DEP_PKGS_CSWwxwidgetscommon += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-baseu2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-baseu2-9-3 += CSWlibz1

PACKAGES += CSWlibwx-baseu-net2-9-3
SPKG_DESC_CSWlibwx-baseu-net2-9-3 += $(DESCRIPTION), libwx_baseu_net-2.9.so.3
PKGFILES_CSWlibwx-baseu-net2-9-3 += $(call pkgfiles_lib,libwx_baseu_net-2.9.so.3)
RUNTIME_DEP_PKGS_CSWwxwidgetscommon += CSWlibwx-baseu-net2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-baseu-net2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-baseu-net2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-baseu-net2-9-3 += CSWlibz1

PACKAGES += CSWlibwx-baseu-xml2-9-3
SPKG_DESC_CSWlibwx-baseu-xml2-9-3 += $(DESCRIPTION), libwx_baseu_xml-2.9.so.3
PKGFILES_CSWlibwx-baseu-xml2-9-3 += $(call pkgfiles_lib,libwx_baseu_xml-2.9.so.3)
RUNTIME_DEP_PKGS_CSWwxwidgetscommon += CSWlibwx-baseu-xml2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-baseu-xml2-9-3 += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWlibwx-baseu-xml2-9-3 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibwx-baseu-xml2-9-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibwx-baseu-xml2-9-3 += CSWlibz1

PACKAGES += CSWwxwidgetsgtk2-dev
SPKG_DESC_CSWwxwidgetsgtk2-dev += $(DESCRIPTION), development files
PKGFILES_CSWwxwidgetsgtk2-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWwxwidgetsgtk2-dev += $(bindir)/wxrc.*
PKGFILES_CSWwxwidgetsgtk2-dev += $(libdir)/wx/config/.*
PKGFILES_CSWwxwidgetsgtk2-dev += $(libdir)/wx/include/.*
PKGFILES_CSWwxwidgetsgtk2-dev += $(sharedstatedir)/bakefile/.*
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-gl2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-xrc2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-richtext2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-core2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-aui2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-html2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-baseu2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-media2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-ribbon2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-stc2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-qa2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-baseu-net2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-adv2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-baseu-xml2-9-3
RUNTIME_DEP_PKGS_CSWwxwidgetsgtk2-dev += CSWlibwx-gtk2u-propgrid2-9-3
OBSOLETED_BY_CSWwxwidgetsgtk2-dev += CSWwxwidgetsdevel
CATALOGNAME_CSWwxwidgetsdevel = wxwidgets_devel_stub

PACKAGES += CSWwxwidgets
SPKG_DESC_CSWwxwidgets = catchall
# PKGFILES is catchall

# There is no testsuite
TEST_SCRIPTS =

# For vsscanf support
# EXTRA_LINKER_FLAGS += /opt/csw/lib/libncursesw.so
#EXTRA_LINKER_FLAGS += -lncursesw
# To fix the __sincos problem on x86
#EXTRA_LINKER_FLAGS += -lsunmath

# We need 64 bit gstreamer, disable for now
# BUILD64_LIBS_ONLY = 1LAGS += -lsunmath

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-gtk=2
CONFIGURE_ARGS += -$(prefix)k-prefix=/opt/csw
CONFIGURE_ARGS += --with-regex
CONFIGURE_ARGS += --with-opengl
CONFIGURE_ARGS += CONFIGURE_ARGS += --with-libmspack

#EXTRA_CFLAGS = -fast -xstrconst -xnolibmopt -D__EXTENSIONS__
#EXTRA_CXXFLAGS = -fast -xstrconst -xnolibmopt -D__EXTENSIONS__

EXTRA_LDFLAGS += -norunpath

#INSTALL_SCRIPTS = wxwidgets

include gar/category.mk

#install-wxwidgets:
#	(cd $(WORKSRC); $(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) install)
#	(cd $(WORKSRC)/contrib; $(INSTALL_ENV) gmake DESTDIR=$(DESTDIR) install)
#	@$(MAKECOOKIE)

#post-merge:
#	ginstall -m 755 \
#	  $(FILEDIR)/libwx_gtk2u-2.8.so.0.2.0-$(GARCH) \
#	  $(PKGROOT)$(libdir)/libwx_gtk2u-2.8.so.0.2.0
#	ginstall -m 755 \
#	  $(FILEDIR)/libwx_gtk2u_gl-2.8.so.0.2.0-$(GARCH) \
#	  $(PKGROOT)$(libdir)/libwx_gtk2u_gl-2.8.so.0.2.0
#_gl-2.8.so.0.2.0