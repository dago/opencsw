# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = cloog
VERSION = 0.16.3
CATEGORIES = lib
DESCRIPTION = Code Generator in the Polyhedral Model
define BLURB
endef
VENDOR_URL = http://www.cloog.org/
MASTER_SITES = http://www.bastoul.net/cloog/pages/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64 = 1
GARCOMPILER = GNU

LICENSE = $(FILEDIR)/COPYING

BUILD_DEP_PKGS = CSWlibppl-dev

PACKAGES += CSWlibcloog-isl2
PKGFILES_CSWlibcloog-isl2 += $(call baseisadirs,$(libdir),libcloog-isl\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibcloog-isl2 += $(DESCRIPTION), libcloog-isl.so.2
RUNTIME_DEP_PKGS_CSWlibcloog-isl2 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibcloog-isl2 += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWlibcloog-isl2 += CSWlibisl7

PACKAGES += CSWlibisl7
PKGFILES_CSWlibisl7 += $(call baseisadirs,$(libdir),libisl\.so\.7(\.\d+)*)
SPKG_DESC_CSWlibisl7 += $(DESCRIPTION), libisl.so.7
RUNTIME_DEP_PKGS_CSWlibisl7 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibisl7 += CSWlibgmp10

PACKAGES += CSWcloog-dev
SPKG_DESC_CSWcloog-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWcloog-dev += CSWlibcloog-isl2
RUNTIME_DEP_PKGS_CSWcloog-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcloog-dev += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWcloog-dev += CSWlibisl7

include gar/category.mk
