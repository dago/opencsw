GARNAME = zlib
GARVERSION = 1.2.3
CATEGORIES = lib

DESCRIPTION = Zlib Data Compression Library
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

SF_PROJ=libpng
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

SPKG_SOURCEURL = http://www.zlib.net

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=5624
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES = Makefile.in.diff
PATCHFILES += configure.diff

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS = --prefix=$(prefix) --exec_prefix=$(exec_prefix) 
CONFIGURE_ARGS += --libdir=$(libdir) --includedir=$(includedir)  --shared

include gar/category.mk
