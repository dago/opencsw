NAME = zlib
VERSION = 1.2.5
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Zlib data compression library
define BLURB
 zlib is designed to be a free, general-purpose, legally unencumbered -- that
 is, not covered by any patents -- lossless data-compression library for use 
 on virtually any computer hardware and operating system. The zlib data format
 is itself portable across platforms. Unlike the LZW compression method used
 in Unix compress(1) and in the GIF image format, the compression method
 currently used in zlib essentially never expands the data. (LZW can double or
 triple the file size in extreme cases.) zlib's memory footprint is also
 independent of the input data and can be reduced, if necessary, at some cost
 in compression
endef

MASTER_SITES = http://www.zlib.net/
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += COPYING

PATCHFILES += Makefile.in.diff
PATCHFILES += configure.diff

PACKAGES += CSWlibz1
SPKG_DESC_CSWlibz1 = Zlib data compression library, libz.so.1
PKGFILES_CSWlibz1 = $(call pkgfiles_lib,libz.so.1)
OBSOLETED_BY_CSWlibz1 = CSWzlib

PACKAGES += CSWlibz-dev
SPKG_DESC_CSWlibz-dev = Development files for libz.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibz-dev = CSWlibz1

BUILD64_LIBS_ONLY = 1

EXTRA_BUILD_ISAS = sparcv8plus sparcv8plus+vis pentium_pro+mmx pentium

CONFIGURE_ARGS += --prefix=$(prefix)
CONFIGURE_ARGS += --eprefix=$(exec_prefix) 
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURE_ARGS += --includedir=$(includedir)
CONFIGURE_ARGS += --shared

include gar/category.mk
