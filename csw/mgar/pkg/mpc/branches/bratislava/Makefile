# $Id$

NAME = mpc
VERSION = 0.9
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = C library for the arithmetic of complex numbers with arbitrarily high precision
define BLURB
endef

MASTER_SITES = http://www.multiprecision.org/mpc/download/
DISTFILES  = $(DISTNAME).tar.gz

STRIP_LIBTOOL = 1
BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)

LICENSE = COPYING.LIB

PACKAGES =
PACKAGES += CSWlibmpc2
CATALOGNAME_CSWlibmpc2 = libmpc2
PKGFILES_CSWlibmpc2 += $(call baseisadirs,$(libdir),libmpc\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibmpc2 += $(DESCRIPTION), libmpc.so.2
RUNTIME_DEP_PKGS_CSWlibmpc2 += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWlibmpc2 += CSWlibgmp10

PACKAGES += CSWlibmpc-dev
SPKG_DESC_CSWlibmpc-dev = $(DESCRIPTION), developoment files
RUNTIME_DEP_PKGS_CSWlibmpc-dev = CSWlibmpc2

# Documentation is OK to have /usr/local references
CHECKPKG_OVERRIDES_CSWlibmpc-dev += file-with-bad-content|/usr/local|root/opt/csw/share/info/mpc.info

include gar/category.mk

