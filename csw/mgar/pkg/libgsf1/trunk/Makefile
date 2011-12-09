NAME = libgsf
VERSION = 1.9.1
CATEGORIES = gnome

DESCRIPTION = GNOME Structured File Library
define BLURB
	The GNOME Structured File Library (GSF) is an I/O abstraction for
	reading/writing compound files. GSF is released under the GNU Lesser
	General Public License (GNU LGPL), which allows for flexible licensing of
	client applications. 
endef

DISTFILES += libgsf-1.so.1.9.1.i386
DISTFILES += libgsf-1.so.1.9.1.sparc
DISTFILES += libgsf-gnome-1.so.1.9.1.i386
DISTFILES += libgsf-gnome-1.so.1.9.1.sparc

# The updated libgsf is only released for Solaris 10 due to new glib only on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://ftp.gnome.org/pub/GNOME/sources/libgsf/

PACKAGES += CSWlibgsf
SPKG_DESC_CSWlibgsf = GNOME structured file library, legacy libgsf-1.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgsf += CSWorbit2
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibz-dev
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibintl3
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibbonobo2
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgsf += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibgsf += CSWlibgmodule2-0-0

# This is old crud, just override
CHECKPKG_OVERRIDES_CSWlibgsf += license-missing|/opt/csw/share/doc/libgsf/license
CHECKPKG_OVERRIDES_CSWlibgsf += bad-rpath-entry|/usr/ucblib|opt/csw/lib/libgsf-gnome-1.so.1
CHECKPKG_OVERRIDES_CSWlibgsf += shared-lib-pkgname-mismatch

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall $(WORKDIR)/libgsf-1.so.1.9.1.$(GARCH) $(DESTDIR)$(libdir)/libgsf-1.so.1
	ginstall $(WORKDIR)/libgsf-gnome-1.so.1.9.1.$(GARCH) $(DESTDIR)$(libdir)/libgsf-gnome-1.so.1
	@$(MAKECOOKIE)
