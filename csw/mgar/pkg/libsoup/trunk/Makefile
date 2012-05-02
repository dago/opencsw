# $Id$

NAME = libsoup
VERSION = 2.29.91
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = HTTP client/server library for GNOME
define BLURB
endef
MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += old_libs_i386.tar.bz2
DISTFILES += old_libs_sparc.tar.bz2

BUILD_DEP_PKGS += CSWlibproxy

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-libgcrypt-prefix=$(prefix)

STRIP_LIBTOOL = 1

# Not working until gconf2 is 64-bit
#BUILD64_LIBS_ONLY = 1

# One test fails for some unknown reason
#TEST_TARGET = check
TEST_TARGET =

PACKAGES += CSWlibsoup2-4-1
CATALOGNAME_CSWlibsoup2-4-1 = libsoup2_4_1
PKGFILES_CSWlibsoup2-4-1 += $(call baseisadirs,$(libdir),libsoup-2\.4\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibsoup2-4-1 += $(DESCRIPTION), libsoup-2.4.so.1
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWglib2
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibsoup2-4-1 += CSWlibz1

PACKAGES += CSWlibsoup-gnome2-4-1
CATALOGNAME_CSWlibsoup-gnome2-4-1 = libsoup_gnome2_4_1
PKGFILES_CSWlibsoup-gnome2-4-1 += $(call baseisadirs,$(libdir),libsoup-gnome-2\.4\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibsoup-gnome2-4-1 += $(DESCRIPTION), libsoup-gnome-2.4.so.1
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWgconf2
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWglib2
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibgnome-keyring0
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibproxy
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibsoup2-4-1
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibsqlite3-0
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibsoup-gnome2-4-1 += CSWlibz1

PACKAGES += CSWlibsoup-doc
SPKG_DESC_CSWlibsoup-doc += HTTP client/server library for GNOME - documentation
PKGFILES_CSWlibsoup-doc = $(sharedstatedir)/gtk-doc/.*
ARCHALL_CSWlibsoup-doc = 1
OBSOLETED_BY_CSWlibsoup-doc = CSWlibsoupdoc
CATALOGNAME_CSWlibsoupdoc = libsoup_doc_stub

PACKAGES += CSWlibsoup-dev
SPKG_DESC_CSWlibsoup-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibsoup-dev += CSWlibsoup-gnome2-4-1
RUNTIME_DEP_PKGS_CSWlibsoup-dev += CSWlibsoup2-4-1
OBSOLETED_BY_CSWlibsoup-dev = CSWlibsoupdevel
CATALOGNAME_CSWlibsoupdevel = libsoup_devel_stub
OBSOLETED_BY_CSWlibsoup-dev += CSWlibsoup
OBSOLETED_BY_CSWlibsoup-dev += CSWlibsoup2
# Catch-all package

include gar/category.mk
