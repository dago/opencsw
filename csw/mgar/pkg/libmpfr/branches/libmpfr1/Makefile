# $Id$

NAME = mpfr
VERSION = 2.3.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNU Multiple Precision floating-point arithmetic library
define BLURB
	The MPFR library is a C library for multiple-precision floating-point 
	computations with correct rounding.
endef

MASTER_SITES = http://www.mpfr.org/mpfr-$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSWlibmpfr
CATALOGNAME_CSWlibmpfr = libmpfr
SPKG_DESC_CSWlibmpfr = $(DESCRIPTION)
SPKG_SOURCEURL_CSWlibmpfr = http://www.mpfr.org/

RUNTIME_DEP_PKGS_CSWlibmpfr  = 
#PATCHFILES = patches

BUILD64 = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)

# It's necessary to include architecture-specific headers from gmp.
EXTRA_INC += $(includedir)/$(ISA)

# With the default -xO3, there are failing unit tests.
OPT_FLAGS_SOS = -xO2

EXTRA_INC += $(includedir)/$(ISA)

PACKAGES =
PACKAGES += CSWlibmpfr1
CATALOGNAME_CSWlibmpfr1 = libmpfr1
PKGFILES_CSWlibmpfr1 += $(call baseisadirs,$(libdir),libmpfr\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibmpfr1 += $(DESCRIPTION), libmpfr.so.1
# This could be a problem, because there are binaries already linking against
# libmpfr.so.1 and libgmp.so.3 (not .so.10) at the same time.
RUNTIME_DEP_PKGS_CSWlibmpfr1 += CSWlibgmp10

PACKAGES += CSWlibmpfr-dev
SPKG_DESC_CSWlibmpfr-dev = MPFR development files
RUNTIME_DEP_PKGS_CSWlibmpfr-dev += CSWlibmpfr1

# Obsoleting the CSWlibmpfr package
OBSOLETED_BY_CSWlibmpfr-dev = CSWlibmpfr
OBSOLETED_BY_CSWlibmpfr1 = CSWlibmpfr

# It's only documentation.
CHECKPKG_OVERRIDES_CSWlibmpfr-dev += file-with-bad-content|/usr/local|root/opt/csw/share/info/mpfr.info

include gar/category.mk
