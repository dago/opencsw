# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = libxpm
VERSION = 3.5.8
CATEGORIES = x11
GARTYPE = v2

DESCRIPTION = X11 pixmap library
define BLURB
  LibXpm provides support and common operation for the XPM pixmap format,
  which is commonly used in legacy X applications. XPM is an extension of
  the monochrome XBM bitmap.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXpm-$(VERSION)
DISTFILES  = $(DISTNAME).tar.bz2

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# CSWxpm is the legacy library
PACKAGES = CSWlibxpm CSWlibxpmdevel CSWxpm

CATALOGNAME_CSWlibxpm = libxpm
CATALOGNAME_CSWlibxpmdevel = libxpm_devel

SPKG_DESC_CSWlibxpm = X11 pixmap library
SPKG_DESC_CSWlibxpmdevel = X11 pixmap library development files

BUILD_DEP_PKGS += CSWx11xproto
BUILD_DEP_PKGS += CSWlibx11devel

RUNTIME_DEP_PKGS_CSWlibxpm_sparc += CSWggettextrt
RUNTIME_DEP_PKGS_CSWxpm          += CSWggettextrt

RUNTIME_DEP_PKGS_CSWlibxpm += $(RUNTIME_DEP_PKGS_CSWlibxpm_$(GARCH))

PKGFILES_CSWlibxpmdevel += $(PKGFILES_DEVEL)
PKGFILES_CSWlibxpm      += $(PKGFILES_RT)

BUILD64 = 1
EXTRA_BUILD_ISAS = sparcv8plus+vis
CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --disable-silent-rules

PATCHFILES = 0001-Forcing-lintl-on-cxpm.patch

# We don't want optimized binaries, optimized libs are sufficient
        MERGE_DIRS_isa-sparcv9 = $(libdir)
MERGE_DIRS_isa-sparcv8plus+vis = $(libdir)
          MERGE_DIRS_isa-amd64 = $(libdir)

# Reset the prefix set by the x11 category
prefix = /opt/csw

include gar/category.mk

post-install-modulated:
	ln -s libXpm.so.4.11.0 $(DESTDIR)$(libdir)/libXpm.so.4.11
	@$(MAKECOOKIE)
