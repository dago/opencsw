# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gtk+
VERSION = 1.2.10
GARTYPE = v2

DESCRIPTION = GIMP Toolkit, for creating graphical user interfaces

MASTER_SITES = http://ftp.gnome.org/pub/gnome/sources/gtk+/1.2/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64_LIB_ONLY = 1

PACKAGES += CSWlibgdk1-2-0
PKGFILES_CSWlibgdk1-2-0 += $(call baseisadirs,$(libdir),libgdk-1\.2\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgdk1-2-0 += $(DESCRIPTION), libgdk-1.2.so.0
RUNTIME_DEP_PKGS_CSWlibgdk1-2-0 += CSWlibglib1-2-0
OBSOLETED_BY_CSWlibgdk1-2-0 = CSWgtk

PACKAGES += CSWlibgtk1-2-0
PKGFILES_CSWlibgtk1-2-0 += $(call baseisadirs,$(libdir),libgtk-1\.2\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgtk1-2-0 += $(DESCRIPTION), libgtk-1.2.so.0
RUNTIME_DEP_PKGS_CSWlibgtk1-2-0 += CSWlibgmodule1-2-0
RUNTIME_DEP_PKGS_CSWlibgtk1-2-0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgtk1-2-0 += CSWlibglib1-2-0
OBSOLETED_BY_CSWlibgtk1-2-0 = CSWgtk

PACKAGES += CSWgtk-dev
SPKG_DESC_CSWgtk-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWgtk-dev += CSWlibgtk1-2-0
RUNTIME_DEP_PKGS_CSWgtk-dev += CSWperl
RUNTIME_DEP_PKGS_CSWgtk-dev += CSWlibgdk1-2-0

# There are .el and .pl files there, but we don't necessarily want to install
# Perl and/or Emacs because of that.
CHECKPKG_OVERRIDES_CSWgtk-dev += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWgtk-dev += missing-dependency|CSWemacs-common

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
