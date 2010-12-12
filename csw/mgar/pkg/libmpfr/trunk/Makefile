NAME = mpfr
VERSION = 2.4.2
CATEGORIES = lib

DESCRIPTION = GNU Multiple Precision floating-point arithmetic library
define BLURB
	The MPFR library is a C library for multiple-precision floating-point 
	computations with correct rounding.
endef

MASTER_SITES = http://www.mpfr.org/mpfr-current/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PACKAGES = CSWlibmpfr
CATALOGNAME_CSWlibmpfr = libmpfr
SPKG_DESC_CSWlibmpfr = $(DESCRIPTION)
SPKG_SOURCEURL_CSWlibmpfr = http://www.mpfr.org/

RUNTIME_DEP_PKGS_CSWlibmpfr  = 
#PATCHFILES = patches

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk
