# Note 1: 32/64bit builds
# ------
#
# The IM Modules stuff expects a file listing all the available
# modules which is created by gtk-query-immodules-2.0. By default this
# file is located at $(sysconfdir)/gtk-2.0/gtk.immodules. Since we
# provide 32/64bit libraries we cannot simply go with the default.
#
# This recipe has two patches which take care of the above mentioned
# problem. The first patch makes 64bit libraries look for
# $(sysconfdir)/gtk-2.0/gtk.immodules-64. 32bit libraries still use
# $(sysconfdir)/gtk-2.0/gtk.immodules.
#
# The second patch modifies gtk-query-immodules-2.0, so that it
# accepts a command line option '--update-modules' which will create
# the proper file in $(sysconfdir)/gtk-2.0/ depending on the ISA,
# i.e. gtk.immodules-64 on 64bit ISAs and gtk.immodules on 32bit
# ISAs. This helps to greatly simplify the postinstall script.

NAME = gtk2
VERSION = 2.24.8
CATEGORIES = lib
GARTYPE = v2

GARCOMPILER = SOS12U1
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
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += CSWgtk2.postinstall
DISTFILES += README.CSW

EXPANDVARS = CSWgtk2.postinstall

# This makes the tests work in the first place
PATCHFILES += 0000-Use-absolute-path-to-Xvfb.patch

# This disables a check that I wasn't able to fix
PATCHFILES += 0000-Disable-gtk_test_create_widget-g_type_from_name-GtkT.patch

# This patch adds a command line option `--update-modules` to
# gtk-query-immodules-2.0 which has the default location of
# gtk.immodules hardcoded and takes 32/64bit ISAs into account.
#
# It goes together with the above patch.
PATCHFILES += 0000-Add-update-modules-cmd-line-option.patch

PATCHFILES += 0000-Adjust-hardcoded-path-to-opt-csw-share.patch

PACKAGES += CSWgtk2
SPKG_DESC_CSWgtk2 = $(DESCRIPTION)
# Catchall
RUNTIME_DEP_PKGS_CSWgtk2  = CSWlibgdk-x112-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWhicoloricontheme
RUNTIME_DEP_PKGS_CSWgtk2 += CSWgtk2-printbackends-papi
RUNTIME_DEP_PKGS_CSWgtk2 += CSWgtk2-printbackends-file
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgailutil18
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgtk-x112-0-0
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders will
# called as well
RUNTIME_DEP_PKGS_CSWgtk2 += CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWgtk2 += CSWfconfig
RUNTIME_DEP_PKGS_CSWgtk2 += CSWftype2
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWgtk2 += CSWpango

PACKAGES += CSWgtk2-printbackends-papi
SPKG_DESC_CSWgtk2-printbackends-papi = $(DESCRIPTION), Print Backend
PKGFILES_CSWgtk2-printbackends-papi = .*/printbackends/libprintbackend-papi.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi = CSWlibgdk-x112-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgtk-x112-0-0
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders will be
# called as well
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWfconfig
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWftype2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWlibz1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-papi += CSWpango

PACKAGES += CSWgtk2-printbackends-file
SPKG_DESC_CSWgtk2-printbackends-file = $(DESCRIPTION), File Print Backend
PKGFILES_CSWgtk2-printbackends-file = .*/printbackends/libprintbackend-file.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file = CSWgtk2-printbackends-papi
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgdk-x112-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgtk-x112-0-0
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders will be
# called as well
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWfconfig
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWftype2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWlibz1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-file += CSWpango

PACKAGES += CSWgtk2-printbackends-cups
SPKG_DESC_CSWgtk2-printbackends-cups = $(DESCRIPTION), CUPS Print Backend
PKGFILES_CSWgtk2-printbackends-cups = .*/printbackends/libprintbackend-cups.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups = CSWgtk2-printbackends-papi
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgdk-x112-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgtk-x112-0-0
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders will be
# called as well
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWfconfig
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWftype2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibcups2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWlibz1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWosslrt
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-cups += CSWpango

PACKAGES += CSWgtk2-printbackends-lpr
SPKG_DESC_CSWgtk2-printbackends-lpr = $(DESCRIPTION), LPR Print Backend
PKGFILES_CSWgtk2-printbackends-lpr = .*/printbackends/libprintbackend-lpr.*
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr = CSWgtk2-printbackends-papi
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgdk-x112-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgtk-x112-0-0
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders will be
# called as well
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWfconfig
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWftype2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWlibz1
RUNTIME_DEP_PKGS_CSWgtk2-printbackends-lpr += CSWpango

PACKAGES += CSWlibgailutil18
SPKG_DESC_CSWlibgailutil18 = $(DESCRIPTION), libgailutil
PKGFILES_CSWlibgailutil18 = $(call pkgfiles_lib,libgailutil.so.18)
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgailutil18 += CSWpango


PACKAGES += CSWlibgdk-x112-0-0
SPKG_DESC_CSWlibgdk-x112-0-0 = $(DESCRIPTION), libgdk-x11-2.0
PKGFILES_CSWlibgdk-x112-0-0 = $(call pkgfiles_lib,libgdk-x11-2.0.so.0)
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders will be
# called as well
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 = CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgdk-x112-0-0 += CSWpango


PACKAGES += CSWlibgtk-x112-0-0
SPKG_DESC_CSWlibgtk-x112-0-0 = $(DESCRIPTION), libgtk-x11-2.0
PKGFILES_CSWlibgtk-x112-0-0 = $(call pkgfiles_lib,libgtk-x11-2.0.so.0)
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0  = CSWlibgdk-x112-0-0
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders will
# called as well
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWfconfig
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibgtk-x112-0-0 += CSWpango


PACKAGES += CSWgtk2-dev
SPKG_DESC_CSWgtk2-dev = $(DESCRIPTION), Development files
PKGFILES_CSWgtk2-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWgtk2-dev += .*/share/gtk-2.0/demo/.*
# Use this to pick up files in lib/gtk-2.0/include
PKGFILES_CSWgtk2-dev += .*/include/.*\.h
PKGFILES_CSWgtk2-dev += .*/gtk-demo
PKGFILES_CSWgtk2-dev += .*/gtk-builder-convert
RUNTIME_DEP_PKGS_CSWgtk2-dev  = CSWlibgdk-x112-0-0
# I pull the whole gdk pixbuf to make sure gdk-pixbuf-query-loaders
# will be called as well
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWgdkpixbuf
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWfconfig
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWftype2
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibpixman1-0
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWlibz1
RUNTIME_DEP_PKGS_CSWgtk2-dev += CSWpango


PACKAGES += CSWgtk2-doc
SPKG_DESC_CSWgtk2-doc = $(DESCRIPTION), Documentation
ARCHALL_CSWgtk2-doc = 1
PKGFILES_CSWgtk2-doc = .*/share/gtk-doc/.*

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

# This is because gtk.immodules resides in $(sysconfdir)/gtk-2.0. If
# we don't take the memory model into account, 32/64 bit libs would
# get the wrong IM Modules list in gtk.immodules (see also the pango
# recipe).
sysconfdir-suffix-64 = /64
sysconfdir = /etc/opt/csw$(sysconfdir-suffix-$(MEMORYMODEL))

# We need the binaries to query 64 bit modules
MERGE_DIRS_isa-extra = $(bindir) $(libdir)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shm
CONFIGURE_ARGS += --enable-xkb
CONFIGURE_ARGS += --enable-xinerama
CONFIGURE_ARGS += --enable-cups
CONFIGURE_ARGS-64 += --disable-cups
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

include gar/category.mk

post-merge:
	gsed -i -e 's|/usr/share/|$(sharedstatedir)/|g' \
		-e 's|/usr/lib|$(libdir)|g' \
		-e 's|/usr/include|$(includedir)|g' `find $(PKGROOT)$(sharedstatedir)/gtk-doc -type f`
	@$(MAKECOOKIE)