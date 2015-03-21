# $Id$

NAME = libffi
VERSION = 3.2.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A portable foreign function interface library
define BLURB
	FFI stands for Foreign Function Interface. A
	interface is the popular name for the interface that allows codethat allows code 
	written in one language to call code written in 
	The libffi library really only provides the lowest, machine
	dependent layer of a fully featured foreign function interface.
	A layer must exist above libffi that handles type conversions for
	values passed between the two languages.e two languages. 
endef

MASTER_SITES = ftp://sourceware.org/pub/libffi/
SPKG_SOURCEURL = http://sourceware.org/libffi/
DISTFILES  = $(NAME)-$
#where can we build?
PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386$
BUILD64 = 1
$
#fix unwind test
PATCHFILES += configure.patch
# Not needed unless using SOS compiler
#ing SOS compiler
PATCHFILES += Makefile.in.patch
# Not really needed for build, but for SOS comp (not neeeded for recent libffi)
#PATCHFILES += ffi_common.h.patch

#PATCHFILES += ffi_target.h.patch
fi_target.h.patch
# Fix needed for amd64 using SOS compiler
# found at http://software.intel.com/en-us/forums/showthread.php?t=56652
# originally for icc, but at least get the # PATCHFILES += ffi64.c.patch

PACKAGES += CSWlibffi6
SPKG_DESC_CSWlibffi6 += $(DESCRIPTION), libffi.so.6
PKGFILES_CSWlibffi6 += $(call pkgfiles_lib,libffi.so.6)
RUNTIME_DEP_PKGS_CSWlibffi6 += CSWlibgcc-s1

PACKAGES += CSWlibffi-dev
SPKG_DESC_CSWlibffi-dev = $(DESCRIPTION) - developer package
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibffi-dev += CSWlibffi6

LICENSE = LICENSE

BUILD64 = 1
GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-portable-binary

# We need objdump
CONFIGURE_ENV_PATH = $(PATH):/opt/csw/gnu

# disabled because they need DejaGNU
SKIPTEST ?= 1ck
TEST_TARGET = 

include gar/category.mk


# v9.S is not needed when building 32-bit
pre-configure-isa-sparcv8:
	@( cd $(WORKSRC); gsed -e "s|src/sparc/v9.S||" -e "s/AM_CFLAGS = .*/AM_CFLAGS = /" -i Makefile.am ; \
		aclocal; \
		automake)

# v8.S will not build when building 64-bit
pre-configure-isa-sparcv9:
	@( cd $(WORKSRC); gsed -e "s|src/sparc/v8.S||" -e "s/AM_CFLAGS = .*/AM_CFLAGS = /" -i Makefile.am ; \
		aclocal; \
		automake