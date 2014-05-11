# $Id$
#
# TODO: remove CHECKPKG_OVERRIDES_ += soname-unused as soon as issue
# between sparc/i386 is sorted out. Also remove dependencies which had
# to be added due to issue. --raos 2013-11-04

NAME = gtk2
VERSION = 2.24.22
GARTYPE = v2

GARCOMPILER = GNUOMPILER = SOS12U3
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = GTK+, the multiplatform X11 toolkit for GUI development
define BLURB
  GTK, which stands for the Gimp ToolKit, is a library for creating graphical
  user interfaces. It is designed to be small and efficient, but still flexible
  enough to allow the programmer freedom in the interfaces created. GTK provides
  some unique features over standard widget libraries.
endef

GNOME_PROJ = gtk+
MASTER_SITES = $(GNOME_MIRROR)

DISTNAME = gtk+-$(VERSION)
DISTFILES = $(DISTNAME).tar.xz
DISTFILES += CSWgtk2.postinstall
DISTFILES += README.CSW

EXPANDVARS = CSWgtk2.postinstall

# This makes the tests work inPATCHFILES += 0000-Use-absolute-path-to-Xvfb.patch

PATCHFILES += 0000-Disable-gtk_test_create_widget-g_type_from_name-GtkT.patch

PATCHFILES += 0003-Adjust-hardcoded-path-to-opt-csw-share.patch
PATCHFILES += 0004-Initialize-pap_status_t-with-PAPI_OK-instead-of-NULL-to-opt-csw-share.patch

PACKAGES += CSWgtk2
SPKG_DESC_CSWgtk2 = $(DESCRIPTION)
# Catchall
RUNTIME_DEP_PKgdkpixbufWlibgdk-x11-2-0-0
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders will
# called as well
RUNTIME_DEP_PKGtk2-printbackends-file
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibatk1-0-02 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgailutil18
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_Ctk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgdk-x11- CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_intl8
RUNTIME_DEP_PKGS_CSWgtk2 += CSWpango
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2 += CSWglib2
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgcc-s1W# This is required for gtk-update-icon-cache, so that it doesn't fail in the
# postinstall script.
RUNTIME_DEP_PKGS_CSWgtk2 += CSWhicoloriconthemeWgtk2 += CSWpango
CHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWgtk2-printbackends-file
CHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependeCHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWhicoloriconthemeeCHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWglib2e# Remove after -z ignore issue has been resolved
CHECKPKG_OVERRIDES_CSWgtk2 += soname-unused
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWlibxrender
CHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWlibgio2-0-0
CHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWlibfreetype6ency|CSWgdkpixbuf

PACKAGES += CSWgtk2-prARCHALL_CSWgtk2-printbackends-papi = 1
SPKG_DESC_CSWgtk2-printbackends-papi = $(DESCRIPTION), Print Backend (OBSOLETE)
PKGFILES_CSWgtk2-printbackends-papi = intentionally_empty-papi += CSWpango

PACKAGES += CSWgtk2-printbackends-file
SPKG_DESC_CSWgtk2-printbackends-file = $(DESCRIPTION), File Print Backend
PKGFILES_CSWgtk2-pr = .*/printbackends/libprintbackend-file.*
PKGFILES_CSWgtk2-printbackends-file += $(docdir)/gtk2_printbackends_/libprintbackend-file.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackencairo2ibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackendobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgtk-x11-2-0-0-RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgcc-s1-# Remove after -z ignore issue has been resolved
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += soname-unused
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWpango
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += surplus-dependency|CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += surplus-dependency|CSWlibxrender
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += surplus-dependency|CSWpango
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += surplus-dependency|CSWlibatk1-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += surplus-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += surplus-dependency|CSWlibgdk-pixbuf2-0-0rintbackends-papi

PACKAGES += CSWgtk2-printbackends-cups
SPKG_DESC_CSWgtk2-printbackends-cups = $(DESCRIPTION), CUPS Print Backend
PKGFILES_CSWgtk2-pr = .*/printbackends/libprintbackend-cups.*
PKGFILES_CSWgtk2-printbackends-cups += $(docdir)/gtk2_printbackends_/libprintbackend-cups.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackencairo2+= CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibcups2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cx11-cups += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackendobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgtk-x11-2-0-0+RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgcc-s1+# Remove after -z ignore issue has been resolved
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += soname-unused
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibz1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWpango
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgio2-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibxrender
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibgpg-error0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWpango
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibatk1-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibgdk-pixbuf2-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibgnutls28
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWlibgio2-0-0
rintbackends-papi

PACKAGES += CSWgtk2-printbackends-lpr
SPKG_DESC_CSWgtk2-printbackends-lpr = $(DESCRIPTION), LPR Print Backend
PKGFILES_CSWgtk2-p = .*/printbackends/libprintbackend-lpr.*
PKGFILES_CSWgtk2-printbackends-lpr += $(docdir)/gtk2_printbackends_/libprintbackend-lpr.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackecairo2+= CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackenobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgtk-x11-2-0-0sRUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgcc-s1s# Remove once -z ignore issue has been resolved
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += soname-unused
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWpango
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibatk1-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWlibxrender
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWpango
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWlibgdk-x11-2-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWlibatk1-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWlibgdk-pixbuf2-0-0
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWlibgio2-0-0rintbackends-papi

PACKAGES += CSWlibgailutil18
SPKG_DESC_CSWlibgailutil18 = $(DESCRIPTION), libgailutil
PKGFILES_ = $(call pkgfiles_lib,libgailutil.so.18)
PKGFILES_CSWlibgailutil18 += $(docdir)/libgailutil18.*
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibatk1CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgaillib += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgailuk-x11-2-0-0 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgailutRUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgcc-s1t# Remove once -z ignore issue has been resolved
CHECKPKG_OVERRIDES_CSWlibgailutil18 += soname-unused
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWlibgailutil18 += surplus-dependency|CSWlibfontconfig1
CHECKPKG_OVERRIDES_CSWlibgailutil18 += surplus-dependency|CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWlibgailutil18 += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWlibgailutil18 += surplus-dependency|CSWlibcairo2
CHECKPKG_OVERRIDES_CSWlibgailutil18 += surplus-dependency|CSWlibxrender
CHECKPKG_OVERRIDES_CSWlibgailutil18 += surplus-dependency|CSWlibgio2-0-0
CHECKPKG_OVERRIDES_CSWlibgailutil18 += surplus-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWlibgailutil18 += surplus-dependency|CSWlibgdk-pixbuf2-0-0til18 += CSWpango

PACKAGES += CSWlibgdk-x11-2-0-0
SPKG_DESC_CSWlibgdk-x11-2-0-0 = $(DESCRIPTION), libgdk-x11-2.0
PKGFILES_CSW = $(call pkgfiles_lib,libgdk-x11-2.0.so.0)
PKGFILES_CSWlibgdk-x11-2-0-0 += $(docdir)/libgdk_x11_2_0_0.*gdk-x11-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0  = CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x11object += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibgcc-s1-# Remove once -z ignore issue has been resolved
CHECKPKG_OVERRIDES_CSWlibgdk-x11-2-0-0 += soname-unused
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWlibgdk-x11-2-0-0 += surplus-dependency|CSWlibgmodule2-0-0-0-0 += CSWpango


PACKAGES += CSWlibgtk-x11-2-0-0
SPKG_DESC_CSWlibgtk-x11-2-0-0 = $(DESCRIPTION), libgtk-x11-2.0
PKGFILES_CSW = $(call pkgfiles_lib,libgtk-x11-2.0.so.0)
PKGFILES_CSWlibgtk-x11-2-0-0 += $(docdir)/libgtk_x11_2_0_0.*gtk-x11-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0  = CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x1intl8 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibgcc-s1-# remove after -z ignore issue has been resolved
CHECKPKG_OVERRIDES_CSWlibgtk-x11-2-0-0 += soname-unused
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWlibgtk-x11-2-0-0 += surplus-dependency|CSWlibfreetype6
CHECKPKG_OVERRIDES_CSWlibgtk-x11-2-0-0 += surplus-dependency|CSWlibxrender-0-0 += CSWpango


PACKAGES += CSWlibgtk2-dev
SPKG_DESC_CSWlibgtk2-dev = $(DESCRIPTION), Development files
PKGFILES_CSWlibgtk2-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibgtk2-dev += .*/sharePKGFILES_CSWlibgtk2-dev += .*/gtk-demoe/gtk-2.0/demo/.*
# Use this to pick up files in lib/gtk-2.0/include
PKGFILES_CSWlibgtk2-dev += .*/include/.*\.h
PKGFILES_CSWlibgtk2-dev += .*/gtkPKGFILES_CSWlibgtk2-dev += $(docdir)/libgtk2_dev.*k-builder-convert
RUNTIME_DEP_PKGS_CSWlibgtk2-dev  = CSWlibgailutil18
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders
# will be called as well
RUNTIME_DEP_PKGS_CSWlgdkpixbuf
# We wan't to make sure the CSWgtk2 postinstall is called
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibatk-dev
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibcairo-dev
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgdk-pixbuf-dev
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibglib2-dev
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWpango
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWpangodevel2-dev += CSWpango
OBSOLETED_BY_CSWlibgtk2-dev = CSWgtk2devel
CATALOGNAME_CSWgtk2devel = gtk2_devel_stub
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWlCHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWlibcairo-dev
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWlibatk-dev
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWlibglib2-dev
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWpangodevel
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWgtk2
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWgdkpixbuf
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += soname-unused
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWlibintl8
lgdk-pixbuf-dev


PACKAGES += CSWgtk2doc
SPKG_DESC_CSWgtk2doc = $(DESCRIPTION), Documentation
ARCHALL_CSWgtk2doc = 1
PKG = .*/share/gtk-doc/.*
PKGFILES_CSWgtk2doc += $(docdir)/gtk2doc.*//gtk-running.html

SPKG_SOURCEURL = http://www.gtk.org/

BUILD_DEP_PKGS  = CSWpkgconfig
BUILD_DEP_PKGS += CSWcups-dev
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWlibatk-dev
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWlibcairo-dev
BUILD_DEP_PKGS += CSWlibgdk-pixbuf-dev
BUILD_DEP_PKGS += CSWsunx11devel
BUILD_DEP_PKGS += CSWggettext-dev
# Because cups depends on krb
BUILD_DEP_PKGS += CSWlibkrb5-dev
BUILD_DEP_PKGS += CSWggettext
BUILD_DEP_PKGS += CSWlibpixman-dev
BUILD_DEP_PKGS BUILD_DEP_PKGS += CSWfontconfig-dev
BUILD_DEP_PKGS += CSWlibfreetypePKGS BUILD_DEP_PKGS += CSWlibgcrypt-dev
BUILD_DEP_PKGS += CSWlibgpg-error-dev
BUILD_DEP_PKGS += CSWlibgnutls-dev  += CSWlibpng-dev
# Needed to make a test work
BUILD_DEP_PKGS += CSWgamin
# Used to adjust documentation
BUILD_DEP_PKGS += CSWgsed
SKIPTEST = 1

# This is because gtk.immodules resides in $(sysconfdir)/gtk-2.0. If
# we don't take the memory model into account, 32/64 bit libs would
# get the wrong IM Modules list in gtk.immodules (see also the pango
# recipe).
sysconfdir-suffix-64 = /64
sysconfdir = /etc/opt/csw$(sysconfdir-suffix-$(MEMORYMODEL))

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shm
CONFIGURE_ARGS += --enable-xkb
CONFIGURE_ARGS += --enable-xinerama
CONFIGURE_ARGS += --enable-cu += --disable-papi += --enable-cu += --disable-introspection+= --disable-cups
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

include gar/category.mk

post-merge:
	ginstall -d $(PKGROgtk-2.0
	[ -f $(PKGROOT)$(sysconfdir)/gtk-2.0/im-multipress.conf ] || ginstall $(PKGROOT)/etc/opt/csw/gtk-2.0/im-multipress.conf $(PKGROOT)$(sysconfdir))$(sysconfdir)/64/gtk-2.0/
	gsed -i -e 's|/usr/share/|$(sharedstatedir)/|g' \
		-e 's|/usr/lib|$(libdir)|g' \
		-e 's|/usr/include|$(includedir)|g' `find $(PKGROOT)$(sharedstatedir)/gtk-doc -type f`