NAME = pango
VERSION = 1.28.4
CATEGORIES = lib

DESCRIPTION = A framework for the layout and rendering of international text
define BLURB
  The goal of the Pango project is to provide an Open Source framework for the
  layout and rendering of internationalized text. It uses Unicode for all of its
  encoding, and will eventually support output in all the world's major
  languages.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += CSWpango.postinstall

# Use patch unless this is fixed
#   https://bugzilla.gnome.org/show_bug.cgi?id=652228
PATCHFILES += 0001-Do-not-use-gcc-specific-flags-unconditionally.patch
# Use patch unless this is fixed:
#   https://bugzilla.gnome.org/show_bug.cgi?id=652227
PATCHFILES += 0002-Use-inttypes.h-when-stdint.h-is-not-available.patch

VENDOR_URL = http://www.pango.org/

PACKAGES += CSWpango
CATALOGNAME_CSWpango = libpango
CHECKPKG_OVERRIDES_CSWpango += catalogname-does-not-match-pkgname|pkgname=CSWpango|catalogname=libpango|expected-catalogname=pango
SPKG_DESC_CSWpango = Pango, a framework for the layout and rendering of international text
RUNTIME_DEP_PKGS_CSWpango += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpango += CSWlibxft2
RUNTIME_DEP_PKGS_CSWpango += CSWglib2
RUNTIME_DEP_PKGS_CSWpango += CSWlibxrender
RUNTIME_DEP_PKGS_CSWpango += CSWftype2
RUNTIME_DEP_PKGS_CSWpango += CSWfconfig
RUNTIME_DEP_PKGS_CSWpango += CSWlibcairo2

# No split for now as it is unclear how the plugins depend on each one
CHECKPKG_OVERRIDES_CSWpango += shared-lib-pkgname-mismatch

#RUNTIME_DEP_PKGS_CSWpango += CSWlibpango1-0-0
#RUNTIME_DEP_PKGS_CSWpango += CSWlibpangocairo-1-0-0
#RUNTIME_DEP_PKGS_CSWpango += CSWlibpangoft2-1-0-0
#RUNTIME_DEP_PKGS_CSWpango += CSWlibpangox1-0-0
#RUNTIME_DEP_PKGS_CSWpango += CSWlibpangoxft1-0-0

#PACKAGES += CSWlibpango1-0-0
#SPKG_DESC_CSWlibpango1-0-0 = Pango, a framework for the layout and rendering of international text, libpango-1.0.so.0
#PKGFILES_CSWlibpango1-0-0 = $(call pkgfiles_lib,libpango-1.0.so.0)
#
#PACKAGES += CSWlibpangocairo-1-0-0
#SPKG_DESC_CSWlibpangocairo-1-0-0 = Cairo bindings for Pango, libpangocairo-1.0.so.0
#PKGFILES_CSWlibpangocairo1-0-0 = $(call pkgfiles_lib,libpangocairo-1.0.so.0)
#
#PACKAGES += CSWlibpangoft2-1-0-0
#SPKG_DESC_CSWlibpangoft2-1-0-0 = Freetype bindings for Pango, libpangoft2-1.0.so.0
#PKGFILES_CSWlibpangoft2-1-0-0 = $(call pkgfiles_lib,libpangoft2-1.0.so.0)
#
#PACKAGES += CSWlibpangox1-0-0
#SPKG_DESC_CSWlibpangox1-0-0 = X11 bindings for Pango, libpangox-1.0.so.0
#PKGFILES_CSWlibpangox1-0-0 = $(call pkgfiles_lib,libpangox-1.0.so.0)
#
#PACKAGES += CSWlibpangoxft1-0-0
#SPKG_DESC_CSWlibpangoxft1-0-0 = XFT bindings for Pango, libpangoxft-1.0.so.0
#PKGFILES_CSWlibpangoxft1-0-0 = $(call pkgfiles_lib,libpangoxft-1.0.so.0)

PACKAGES += CSWpangodevel
CATALOGNAME_CSWpangodevel = libpango_devel
CHECKPKG_OVERRIDES_CSWpangodevel += catalogname-does-not-match-pkgname|pkgname=CSWpangodevel|catalogname=libpango_devel|expected-catalogname=pangodevel
SPKG_DESC_CSWpangodevel = Developer files for libpango-1.0.so.0 and assorted libs
PKGFILES_CSWpangodevel = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWpangodevel += CSWpango
RUNTIME_DEP_PKGS_CSWpangodevel += CSWlibcairo-dev
#RUNTIME_DEP_PKGS_CSWpango-dev += CSWlibpango1-0-0
#RUNTIME_DEP_PKGS_CSWpango-dev += CSWlibpangocairo-1-0-0
#RUNTIME_DEP_PKGS_CSWpango-dev += CSWlibpangoft2-1-0-0
#RUNTIME_DEP_PKGS_CSWpango-dev += CSWlibpangox1-0-0
#RUNTIME_DEP_PKGS_CSWpango-dev += CSWlibpangoxft1-0-0

PACKAGES += CSWpangodoc
# This is a legacy name
CATALOGNAME_CSWpangodoc = libpango_doc
CHECKPKG_OVERRIDES_CSWpangodoc += catalogname-does-not-match-pkgname|pkgname=CSWpangodoc|catalogname=libpango_doc|expected-catalogname=pangodoc
SPKG_DESC_CSWpangodoc = Documentation for Pango
PKGFILES_CSWpangodoc = $(sharedstatedir)/gtk-doc/.*
ARCHALL_CSWpangodoc = 1

BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWgtk-doc
BUILD_DEP_PKGS += CSWlibxslt
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWlibxft2devel

BUILD64 = 1

sysconfdir-suffix-64 = /64
sysconfdir = /etc/opt/csw$(sysconfdir-suffix-$(MEMORYMODEL))

# EXTRA_ISAEXEC_EXCLUDE_FILES = $(bindir)/pango-querymodules
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-x --enable-gtk-doc
# CONFIGURE_ARGS += --with-included-modules 

STRIP_LIBTOOL = 1

# Lots of compiler-specific tests failing (Sun Studio?)
SKIPTEST ?= 1

EXTRA_MERGE_EXCLUDE_FILES = .*/preload\.1\.gz

# We need the binaries to query 64 bit modules
MERGE_DIRS_isa-extra = $(bindir) $(libdir)

include gar/category.mk

post-extract-modulated:
	-perl -pi \
		-e 's,#!/bin/sh,#!/bin/bash,' \
		$(WORKSRC)/pango/check.defs
	@$(MAKECOOKIE)

post-merge:
	mkdir -p $(PKGROOT)$(sysconfdir)/64/pango
	@$(MAKECOOKIE)
