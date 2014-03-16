# $Id$

NAME = mpc
VERSION = 1.0.2
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = C library for the arithmetic of complex numbers with arbitrarily high precision
defVENDOR_URL = http://www.multiprecision.org/
MASTER_SITES = ftp://ftp.gnu.org/gnu/mpc/
DISTFILES  = $(DISTNAME).tar.gz
PACKAGING_PLATFORMS  = solaris9-i386
PACKAGING_PLATFORMS += solaris9-sparc
PACKAGING_PLATFORMS += solaris10-i386
PACKAGING_PLATFORMS += solaris10-sparc(DISTNAME).tar.gz

STRIP_LIBTOOL = 1
BUILD64_LIBS_ONLY = 1

CONFIGURE_ARG# GCC4_CC_HOME = /opt/csw/gcc4
# GCC4_CC = $(GCC4_CC_HOME)/bin/gcc
# GCC4_CXX = $(GCC4_CC_HOME)/bin/g++
# prefix = $(HOME)/usr-$(GARCH)-$(GAROSREL)
# EXTRA_INC = $(prefix)/include
# EXTRA_INC += $(BUILD_PREFIX)/include
# For linking against the old gcc
# EXTRA_LIB = $(prefix)/gcc4/lib

LICENSE = COPYING.LESSER

PACKAGES =

PACKAGES += CSWlibmpc3
CATALOGNAME_CSWlibmpc3 = libmpc3
PKGFILES_CSWlibmpc3 += $(call baseisadirs,$(libdir),libmpc\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibmpc3 += $(DESCRIPTION), libmpc.so.3
RUNTIME_DEP_PKGS_CSWlibmpc3 += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWlibmpc3P_PKGS_CSWlibmpc2 += CSWlibgmp10

PACKAGES += CSWlibmpc-dev
SPKG_DESC_CSWlibmpc-dev = $(DESCRIPTION), developoment files
RUNTIME_DEP_PKGS_CSWlibmp3-dev = CSWlibmpc2

# Documentation is OK to have /usr/local references
CHECKPKG_OVERRIDES_CSWlibmpc-dev += file-with-bad-content|/usr/local|root/opt/csw/share/info/mpc.info

include 