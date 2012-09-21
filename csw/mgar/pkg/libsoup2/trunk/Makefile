NAME = libsoup
VERSION = 2.33.92
CATEGORIES = lib
GARTYPE = v2
  

DESCRIPTION = HTTP client/server library for GNOME
define BLURB
endef
MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGING_PLATFORMS = Solaris10-sparc Solaris10-i386

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.bz2

PACKAGES += CSWlibsoup2-4-1
CATALOGNAME_CSWlibsoup2-4-1 = libsoup2_4_1
PKGFILES_CSWlibsoup2-4-1 += $(call baseisadirs,$(libdir),libsoup-2\.4\.so\.1\.3\.0)
PKGFILES_CSWlibsoup2-4-1 += $(call baseisadirs,$(libdir),libsoup-2\.4\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibsoup2-4-1 += $(DESCRIPTION), libsoup-2.4.so.1
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibgio2-0-0
OBSOLETED_BY_CSWlibsoup2-4-1 = CSWlibsoup

PACKAGES += CSWlibsoup-gnome2-4-1
CATALOGNAME_CSWlibsoup-gnome2-4-1 = libsoup_gnome2_4_1
PKGFILES_CSWlibsoup-gnome2-4-1 += $(call baseisadirs,$(libdir),libsoup-gnome-2\.4\.so\.1\.3\.0)
PKGFILES_CSWlibsoup-gnome2-4-1 += $(call baseisadirs,$(libdir),libsoup-gnome-2\.4\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibsoup-gnome2-4-1 += $(DESCRIPTION), libsoup-gnome-2.4.so.1
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibgnome-keyring0
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibsoup2-4-1
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibgio2-0-0
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibglib2-0-0
OBSOLETED_BY_CSWlibsoup-gnome2-4-1 = CSWlibsoup

PACKAGES += CSWlibsoupdoc
SPKG_DESC_CSWlibsoupdoc += $(DESCRIPTION), documentation
PKGFILES_CSWlibsoupdoc += $(sharedstatedir)/gtk-doc/.*
ARCHALL_CSWlibsoupdoc = 1

PACKAGES += CSWlibsoup2-dev
CATALOGNAME_CSWlibsoup2-dev = libsoup2_dev
SPKG_DESC_CSWlibsoup2-dev += $(DESCRIPTION), development files
# PKGFILES_CSWlibsoup2-dev += /opt/csw/lib/libsoup-2.4.so
PKGFILES_CSWlibsoup2-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibsoup2-dev += CSWlibsoup2-4-1
RUNTIME_DEP_PKGS_CSWlibsoup2-dev += CSWlibsoup-gnome2-4-1
OBSOLETED_BY_CSWlibsoup2-dev = CSWlibsoupdevel
CATALOGNAME_CSWlibsoupdevel = libsoup_devel_stub

# EXTRA_INC = /opt/csw/X11/include
# EXTRA_LIB = /opt/csw/X11/lib 
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib 
STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS) 
CONFIGURE_ARGS += --disable-static 
CONFIGURE_ARGS += --disable-tls-check

# Test disabled because of missing Apache stuff
TEST_TARGET = 

include gar/category.mk
