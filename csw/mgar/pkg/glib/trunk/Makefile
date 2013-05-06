# $Id$

NAME = glib
VERSION = 1.2.10
GARTYPE = v2

DESCRIPTION = General-purpose utility libraryth GNOME programs
define BLURB
  GLib is a library containing many useful C routines for things such as trees,
  hashes, aMASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-libiconv

TEST_SCRIPTS = $(WORKSRC)/Makefile

#provided by iconv
MERGE_EXCLUDE_FILES = .*/charset.alias

PACKAGES += CSWglib-dev
SPKG_DESC_CSWglib-dev = $(DESCRIPTION), development files
PKGFILES_CSWglib-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWglib-dev += $(sharedstatedir)/gtk-doc/.*
RUNTIME_DEP_PKGS_CSWglib-dev += CSWlibgmodule1-2-0
RUNTIME_DEP_PKGS_CSWglib-dev += CSWlibglib1-2-0
RUNTIME_DEP_PKGS_CSWglib-dev += CSWlibgthread1-2-0
# Historical reasons

OBSOLETED_BY_CSWglib-dev = CSWglib-devel
CATALOGNAME_CSWglibdevel = glib_devel
# CHECKPKG_OVERRIDES_CSWglibdevel += catalogname-does-not-match-pkgname|pkgname=CSWglibdevel|catalogname=glib_devel|expected-catalogname=glibdevel

PACKAGES += CSWlibglib1-2-0
CATALOGNAME_CSWlibglib1-2-0 = libglib1_2_0
PKGFILES_CSWlibglib1-2-0 += $(call baseisadirs,$(libdir),libglib-1\.2\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibglib1-2-0 += $(DESCRIPTION), libglib-1.2.so.0
OBSOLETED_BY_CSWlibglib1-2-0 = CSWglib

PACKAGES += CSWlibgmodule1-2-0
CATALOGNAME_CSWlibgmodule1-2-0 = libgmodule1_2_0
PKGFILES_CSWlibgmodule1-2-0 += $(call baseisadirs,$(libdir),libgmodule-1\.2\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgmodule1-2-0 += $(DESCRIPTION), libgmodule-1.2.so.0
OBSOLETED_BY_CSWlibgmodule1-2-0 = CSWglib

PACKAGES += CSWlibgthread1-2-0
PKGFILES_CSWlibgthread1-2-0 += $(call baseisadirs,$(libdir),libgthread-1\.2\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgthread1-2-0 += $(DESCRIPTION), libgthread-1.2.so.0
OBSOLETED_BY_CSWlibgthread1-2-0 = CSWglibtedir)/gtk-doc/.*

include