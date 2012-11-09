# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = openslp
VERSION = 1.2.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Service location protocol
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

# OpenSSL is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://www.openslp.org/

PACKAGES += CSWlibslp1
PKGFILES_CSWlibslp1 += $(call pkgfiles_lib,libslp.so.1)
SPKG_DESC_CSWlibslp1 += Service location protocol, libslp.so.1
RUNTIME_DEP_PKGS_CSWlibslp1 += CSWlibssl1-0-0

PACKAGES += CSWlibslp-dev
SPKG_DESC_CSWlibslp-dev = Development files for libslp.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibslp-dev += CSWlibslp1
RUNTIME_DEP_PKGS_CSWlibslp-dev += CSWlibssl-dev
OBSOLETED_BY_CSWlibslp-dev += CSWopenslp-devel

# These are just docs
CHECKPKG_OVERRIDES_CSWlibslp-dev += file-with-bad-content|/usr/local|root/opt/csw/doc/openslp-1.2.1/html/UsersGuide/Installation.html
CHECKPKG_OVERRIDES_CSWlibslp-dev += file-with-bad-content|/usr/share|root/opt/csw/doc/openslp-1.2.1/html/UsersGuide/FileLocations.html

PACKAGES += CSWopenslp
SPKG_DESC_CSWopenslp = Open service locator protocol
PKGFILES_CSWopenslp += $(sysconfdir)/.*
PKGFILES_CSWopenslp += $(bindir)/.*
PKGFILES_CSWopenslp += $(sbindir)/.*
RUNTIME_DEP_PKGS_CSWopenslp += CSWlibslp1
RUNTIME_DEP_PKGS_CSWopenslp += CSWlibssl1-0-0

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-slpv2-security

PRESERVECONF += $(sysconfdir)/slp.conf
PRESERVECONF += $(sysconfdir)/slp.reg
PRESERVECONF += $(sysconfdir)/slp.spi

# Testsuite must be run as root
SKIPTEST ?= 1

include gar/category.mk
