# $Id$

NAME = gtk2
VERSION = 2.24.14
CATEGORIES = lib
GARTYPE = v2

GARCOMPILER = SOS12U3
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

# This makes the tests work in the first place
PATCHFILES += 0000-Use-absolute-path-to-Xvfb.patch

# This disables a check that I wasn't able to fix
#
# This bug has already been reported by Tim Mooney
#  https://bugzilla.gnome.org/show_bug.cgi?id=643338
PATCHFILES += 0000-Disable-gtk_test_create_widget-g_type_from_name-GtkT.patch

# This patch adds a command line option `--update-modules` to
# gtk-query-immodules-2.0 which has the default location of
# gtk.immodules hardcoded and takes 32/64bit ISAs into account.
PATCHFILES += 0000-Add-update-modules-cmd-line-option.patch

PATCHFILES += 0000-Adjust-hardcoded-path-to-opt-csw-share.patch

PACKAGES += CSWgtk2
SPKG_DESC_CSWgtk2 = $(DESCRIPTION)
# Catchall
RUNTIME_DEP_PKGS_CSWgtk2  = CSWlibgdk-x11-2-0-0
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders will
# called as well
RUNTIME_DEP_PKGS_CSWgtk2 += CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWgtk2 += CSWgtk2-printbackends-file
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgailutil18
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibintl8 += CSWlibxrender
RUNTIME_DEP_PKGS_CSW# This is required for gtk-update-icon-cache, so that it doesn't fail in the
# postinstall script.
RUNTIME_DEP_PKGS_CSWgtk2 += CSWhicoloriconthemeWgtk2 += CSWpango
CHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWgtk2-printbackends-file
CHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependeCHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWhicoloriconthemeency|CSWgdkpixbuf

PACKAGES += CSWgtk2-printbackends-papi
SPKG_DESC_CSWgtk2-printbackends-papi = $(DESCRIPTION), Print Backend
PKGFILES_CSWgtk2-pr = .*/printbackends/libprintbackend-papi.*
PKGFILES_CSWgtk2-printbackends-papi += $(docdir)/gtk2_printbackends_papi.*+= CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2-printbackendlib += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackendsk-x11-2-0-0-papi += CSWpango

PACKAGES += CSWgtk2-printbackends-file
SPKG_DESC_CSWgtk2-printbackends-file = $(DESCRIPTION), File Print Backend
PKGFILES_CSWgtk2-pr = .*/printbackends/libprintbackend-file.*
PKGFILES_CSWgtk2-printbackends-file += $(docdir)/gtk2_printbackends_/libprintbackend-file.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file  = CSWgtk2-printbackends-papi
RUNTIME_DEP_PKGS_CSWgtk2-printbackencairo2ibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackendobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgtk-x11-2-0-0-file += CSWpango
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += surplus-dependency|CSWgtk2-printbackends-papi

PACKAGES += CSWgtk2-printbackends-cups
SPKG_DESC_CSWgtk2-printbackends-cups = $(DESCRIPTION), CUPS Print Backend
PKGFILES_CSWgtk2-pr = .*/printbackends/libprintbackend-cups.*
PKGFILES_CSWgtk2-printbackends-cups += $(docdir)/gtk2_printbackends_/libprintbackend-cups.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups  = CSWgtk2-printbackends-papi
RUNTIME_DEP_PKGS_CSWgtk2-printbackencairo2+= CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibcups2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cx11-cups += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackendobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgtk-x11-2-0-0+= CSWlibgnutls26
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWgtk2-printbackends-papi

PACKAGES += CSWgtk2-printbackends-lpr
SPKG_DESC_CSWgtk2-printbackends-lpr = $(DESCRIPTION), LPR Print Backend
PKGFILES_CSWgtk2-p = .*/printbackends/libprintbackend-lpr.*
PKGFILES_CSWgtk2-printbackends-lpr += $(docdir)/gtk2_printbackends_/libprintbackend-lpr.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr = CSWgtk2-printbackends-papi
RUNTIME_DEP_PKGS_CSWgtk2-printbackecairo2+= CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackenobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgtk-x11-2-0-0s-lpr += CSWpango
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWgtk2-printbackends-papi

PACKAGES += CSWlibgailutil18
SPKG_DESC_CSWlibgailutil18 = $(DESCRIPTION), libgailutil
PKGFILES_ = $(call pkgfiles_lib,libgailutil.so.18)
PKGFILES_CSWlibgailutil18 += $(docdir)/libgailutil18.*
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibatk1CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgaillib += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgailuk-x11-2-0-0 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWpango

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
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWpango


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
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWpango


PACKAGES += CSWlibgtk2-dev
SPKG_DESC_CSWlibgtk2-dev = $(DESCRIPTION), Development files
PKGFILES_CSWlibgtk2-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibgtk2-dev += .*/share/gtk-2.0/demo/.*
# Use this to pick up files in lib/gtk-2.0/include
PKGFILES_CSWlibgtk2-dev += .*/include/.*\.h
PKGFILES_CSWlibgtk2-dev += .*/gtk-demo
PKGFILES_CSWlibgtk2-dev += .*/gtkPKGFILES_CSWlibgtk2-dev += $(docdir)/libgtk2_dev.*k-builder-convert
RUNTIME_DEP_PKGS_CSWlibgtk2-dev  = CSWlibgailutil18
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders
# will be called as well
RUNTIME_DEP_PKGS_CSWlibggdk-pixbuf-dev
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWpangodevel
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibglib2-dev
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibatk-dev
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibcairo-dev2-dev += CSWpango
OBSOLETED_BY_CSWlibgtk2-dev = CSWgtk2devel
CATALOGNAME_CSWgtk2devel = gtk2_devel_stub
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWlCHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWlibcairo-dev
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWlibatk-dev
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWlibglib2-dev
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWpangodevel
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWgtk2
# That's supposed to come with CSWgtk2
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += missing-dependency|CSWlibgtk-x11-2-0-0
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += missing-dependency|CSWlibgdk-pixbuf2-0-0
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += missing-dependency|CSWlibgdk-x11-2-0-0
# That's supposed to come with CSWpangodevel
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += missing-dependency|CSWpango
# That's supposed to come with CSWlibcairo-dev
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += missing-dependency|CSWlibcairo2
# That's supposed to come with CSWlibglib2-dev
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += missing-dependency|CSWlibgobject2-0-0
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += missing-dependency|CSWlibglib2-0-0

libgdk-pixbuf-dev


PACKAGES += CSWgtk2doc
SPKG_DESC_CSWgtk2doc = $(DESCRIPTION), Documentation
ARCHALL_CSWgtk2doc = 1
PKG = .*/share/gtk-doc/.*
PKGFILES_CSWgtk2doc += $(docdir)/gtk2doc.*/share/gtk-doc/.*
CHECKPKG_OVERRIDES_CSWgtk2doc += file-with-bad-content|/usr/local|root/opt/csw/share2/gtk2-Resource-Files.html/share/gtk-doc/.*
CHECKPKG_OVERRIDES_CSWgtk2doc += file-with-bad-content|/usr/local|root/opt/csw/share2/gtk-doc/html/gtk/gtk-running.html

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
BUILD_DEP_PKGS += CSWlibfreetypePKGS += CSWlibpng-dev
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
CONFIGURE_ARGS += --enable-cu += --enable-introspection=no += --enable-cups
CONFIGURE_ARGS-64 += --disable-cups
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

include gar/category.mk

post-merge:
	ginstall -d $(PKGROOT)$(sysconfdir)/64/gtk-2.0
	ginstall $(PKGROOT)$(sysconfdir)/gtk-2.0/im-multipress.conf $(PKGROOT)$(sysconfdir)/64/gtk-2.0/
	gsed -i -e 's|/usr/share/|$(sharedstatedir)/|g' \
		-e 's|/usr/lib|$(libdir)|g' \
		-e 's|/usr/include|$(includedir)|g' `find $(PKGROOT)$(sharedstatedir)/gtk-doc -type f`