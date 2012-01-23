# $Id$

NAME = mpfr
VERSION = 3.1.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNU Multiple Precision floating-point arithmetic library
define BLURB
	The MPFR library is a C library for multiple-precision floating-point 
	computations with correct rounding.
endef

DL_VER = $(shell echo $(VERSION) | gsed -e 's/\([^-]\+\)\(-.*\)/\1/')

MASTER_SITES = http://www.mpfr.org/mpfr-$(DL_VER)/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

BUILD_DEP_PKGS = CSWlibgmp-dev

BUILD64_LIBS_ONLY = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)

# With the default -xO3, there are failing unit tests.
OPT_FLAGS_SOS = -xO2

PACKAGES =
PACKAGES += CSWlibmpfr4
CATALOGNAME_CSWlibmpfr4 = libmpfr4
PKGFILES_CSWlibmpfr4 += $(call baseisadirs,$(libdir),libmpfr\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibmpfr4 += $(DESCRIPTION), libmpfr.so.4
RUNTIME_DEP_PKGS_CSWlibmpfr4 += CSWlibgmp10

PACKAGES += CSWlibmpfr-dev
SPKG_DESC_CSWlibmpfr-dev = MPFR development files
RUNTIME_DEP_PKGS_CSWlibmpfr-dev += CSWlibmpfr4

# It's only documentation.
CHECKPKG_OVERRIDES_CSWlibmpfr-dev += file-with-bad-content|/usr/local|root/opt/csw/share/info/mpfr.info
CHECKPKG_OVERRIDES_CSWlibmpfr-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mpfr/FAQ.html

# The LD_OPTIONS setting breaks the test suite, because it makes
# /opt/csw/lib/$ISALIST be always in front, while the tests require a local
# directory be in front instead.
# http://websympa.loria.fr/wwsympa/arc/mpfr/2011-09/msg00009.html
# http://wiki.opencsw.org/porting-faq#toc9
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

include gar/category.mk
