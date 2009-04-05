GARNAME      = gcc
GARVERSION   = 4.3.3
CATEGORIES   = lang

DESCRIPTION  = The GNU Compiler Collection
define BLURB
	The GNU Compiler Collection includes front ends for C, C++, 
	Objective-C, Fortran, Java, and Ada, as well as libraries 
	for these languages (libstdc++, libgcj,...).
endef

DISTFILES    = $(GARNAME)-$(GARVERSION).tar.bz2
MASTER_SITES = $(GNU_MIRROR)/$(GARNAME)-$(GARVERSION)/

# We define upstream file regex so we can be notifed 
# of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

## build options
CONFIGURE_ARGS  = --prefix=$(BUILD_PREFIX)/gcc4
CONFIGURE_ARGS += --exec-prefix=$(BUILD_PREFIX)/gcc4
CONFIGURE_ARGS += --with-gnu-as
CONFIGURE_ARGS += --with-as=/opt/csw/bin/gas
CONFIGURE_ARGS += --without-gnu-ld
CONFIGURE_ARGS += --with-ld=/usr/ccs/bin/ld
CONFIGURE_ARGS += --enable-nls
CONFIGURE_ARGS += --with-included-gettext
CONFIGURE_ARGS += --with-libiconv-prefix=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-x
CONFIGURE_ARGS += --with-mpfr=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-gmp=$(BUILD_PREFIX)
CONFIGURE_ARGS += --enable-java-awt=xlib
CONFIGURE_ARGS += --enable-libada
CONFIGURE_ARGS += --enable-libssp
CONFIGURE_ARGS += --enable-objc-gc
CONFIGURE_ARGS += --enable-threads=posix 
CONFIGURE_ARGS += --enable-stage1-languages=c
CONFIGURE_ARGS += --enable-languages=ada,c,c++,fortran,java,objc

## For cleanliness I split the Configuration into separate files
include files/amd_merge.mk
include files/gar_override.mk
include files/package_def.mk
include files/pkg_scripts.mk
## include mGar definitions
include gar/category.mk
