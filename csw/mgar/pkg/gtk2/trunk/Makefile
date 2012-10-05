# $Id$

NAME = gtk2
VERSION = 2.24.12
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
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgtk2 += CSWgtk2-printbackends-file
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgailutil18
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2 += CSWpango
CHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWgtk2-printbackends-file
CHECKPKG_OVERRIDES_CSWgtk2 += surplus-dependency|CSWgdkpixbuf

PACKAGES += CSWgtk2-printbackends-papi
SPKG_DESC_CSWgtk2-printbackends-papi = $(DESCRIPTION), Print Backend
PKGFILES_CSWgtk2-printbackends-papi = .*/printbackends/libprintbackend-papi.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi  = CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWpango

PACKAGES += CSWgtk2-printbackends-file
SPKG_DESC_CSWgtk2-printbackends-file = $(DESCRIPTION), File Print Backend
PKGFILES_CSWgtk2-printbackends-file = .*/printbackends/libprintbackend-file.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file  = CSWgtk2-printbackends-papi
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWpango
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-file += surplus-dependency|CSWgtk2-printbackends-papi

PACKAGES += CSWgtk2-printbackends-cups
SPKG_DESC_CSWgtk2-printbackends-cups = $(DESCRIPTION), CUPS Print Backend
PKGFILES_CSWgtk2-printbackends-cups = .*/printbackends/libprintbackend-cups.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups  = CSWgtk2-printbackends-papi
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibcups2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibz1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWpango
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgnutls26
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-cups += surplus-dependency|CSWgtk2-printbackends-papi

PACKAGES += CSWgtk2-printbackends-lpr
SPKG_DESC_CSWgtk2-printbackends-lpr = $(DESCRIPTION), LPR Print Backend
PKGFILES_CSWgtk2-printbackends-lpr = .*/printbackends/libprintbackend-lpr.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr = CSWgtk2-printbackends-papi
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWpango
CHECKPKG_OVERRIDES_CSWgtk2-printbackends-lpr += surplus-dependency|CSWgtk2-printbackends-papi

PACKAGES += CSWlibgailutil18
SPKG_DESC_CSWlibgailutil18 = $(DESCRIPTION), libgailutil
PKGFILES_CSWlibgailutil18 = $(call pkgfiles_lib,libgailutil.so.18)
RUNTIME_DEP_PKGS_CSWlibgailutil18  = CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWpango

PACKAGES += CSWlibgdk-x11-2-0-0
SPKG_DESC_CSWlibgdk-x11-2-0-0 = $(DESCRIPTION), libgdk-x11-2.0
PKGFILES_CSWlibgdk-x11-2-0-0 = $(call pkgfiles_lib,libgdk-x11-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0  = CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgdk-x11-2-0-0 += CSWpango


PACKAGES += CSWlibgtk-x11-2-0-0
SPKG_DESC_CSWlibgtk-x11-2-0-0 = $(DESCRIPTION), libgtk-x11-2.0
PKGFILES_CSWlibgtk-x11-2-0-0 = $(call pkgfiles_lib,libgtk-x11-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0  = CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgtk-x11-2-0-0 += CSWpango


PACKAGES += CSWlibgtk2-dev
SPKG_DESC_CSWlibgtk2-dev = $(DESCRIPTION), Development files
PKGFILES_CSWlibgtk2-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibgtk2-dev += .*/share/gtk-2.0/demo/.*
# Use this to pick up files in lib/gtk-2.0/include
PKGFILES_CSWlibgtk2-dev += .*/include/.*\.h
PKGFILES_CSWlibgtk2-dev += .*/gtk-demo
PKGFILES_CSWlibgtk2-dev += .*/gtk-builder-convert
RUNTIME_DEP_PKGS_CSWlibgtk2-dev  = CSWlibgailutil18
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders
# will be called as well
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgdk-pixbuf-dev
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgtk2-dev += CSWpango
OBSOLETED_BY_CSWlibgtk2-dev = CSWgtk2devel
CATALOGNAME_CSWgtk2devel = gtk2_devel_stub
CHECKPKG_OVERRIDES_CSWlibgtk2-dev += surplus-dependency|CSWlibgdk-pixbuf-dev


PACKAGES += CSWgtk2doc
SPKG_DESC_CSWgtk2doc = $(DESCRIPTION), Documentation
ARCHALL_CSWgtk2doc = 1
PKGFILES_CSWgtk2doc = .*/share/gtk-doc/.*
CHECKPKG_OVERRIDES_CSWgtk2doc += file-with-bad-content|/usr/local|root/opt/csw/share/gtk-doc/html/gtk/gtk-Resource-Files.html
CHECKPKG_OVERRIDES_CSWgtk2doc += file-with-bad-content|/usr/local|root/opt/csw/share/gtk-doc/html/gtk/gtk-running.html

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
BUILD_DEP_PKGS += CSWlibpng-dev
# Needed to make a test work
BUILD_DEP_PKGS += CSWgamin
# Used to adjust documentation
BUILD_DEP_PKGS += CSWgsed

BUILD64 = 1

# failed with: Gtk-WARNING **: cannot open display: :101
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
CONFIGURE_ARGS += --enable-cups
CONFIGURE_ARGS-64 += --disable-cups
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

include gar/category.mk

post-merge:
	ginstall -d $(PKGROOT)$(sysconfdir)/64/gtk-2.0
	ginstall $(PKGROOT)$(sysconfdir)/gtk-2.0/im-multipress.conf $(PKGROOT)$(sysconfdir)/64/gtk-2.0/
	gsed -i -e 's|/usr/share/|$(sharedstatedir)/|g' \
		-e 's|/usr/lib|$(libdir)|g' \
		-e 's|/usr/include|$(includedir)|g' `find $(PKGROOT)$(sharedstatedir)/gtk-doc -type f`
	@$(MAKECOOKIE)
