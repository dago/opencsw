# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = cloog
VERSION = 0.18.0
GARTYPE = v2
DESCRIPTION = Code Generator in the Polyhedral Model
define BLURB
endef
VENDOR_URL = http://www.cloog.org/
MASTER_SITES = http://www.bastoul.net/cloog/pages/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
CONFIGURE_ARGS = $(DIRPATHS)
BUILD64_LIBS_ONLY = 1
GARCOMPILER = GNU

LICENSE = $(FILEDIR)/COPYING

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc

PATCHFILES += 0001-Use-opt-csw-bin-bash-for-tests.patch

# BUILD_DEP_PKGS = CSWlibppl-dev

BUILD_DEP_PKGS = CSWbash

PACKAGES += CSWlibcloog-isl4
PKGFILES_CSWlibcloog-isl4 += $(call baseisadirs,$(libdir),libcloog-isl\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibcloog-isl4 += $(DESCRIPTION), libcloog-isl.so.4
RUNTIME_DEP_PKGS_CSWlibcloog-isl4 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibcloog-isl4 += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWlibcloog-isl4 += CSWlibisl7

PACKAGES += CSWlibisl10
PKGFILES_CSWlibisl10 += $(call baseisadirs,$(libdir),libisl\.so\.10(\.\d+)*)
SPKG_DESC_CSWlibisl10 += $(DESCRIPTION), libisl.so.10
RUNTIME_DEP_PKGS_CSWlibisl10 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibisl10 += CSWlibgmp10

PACKAGES += CSWcloog-dev
SPKG_DESC_CSWcloog-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWcloog-dev += CSWlibcloog-isl4
RUNTIME_DEP_PKGS_CSWcloog-dev += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcloog-dev += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWcloog-dev += CSWlibisl10

CHECKPKG_OVERRIDES_CSWcloog-dev += missing-dependency|CSWpython

# The failed test was:
# - min(n + c0 - (n + c0 + 2) / 3, c0); c1 += 2)
# + min(c0, n + c0 - (n + c0 + 2) / 3); c1 += 2)
# ...which is the same thing. So this is a spurious error.
SKIPTEST = 1

include gar/category.mk
