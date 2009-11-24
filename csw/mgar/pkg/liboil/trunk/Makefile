GARNAME = liboil
GARVERSION = 0.3.16
CATEGORIES = lib

DESCRIPTION = A library of simple functions that are optimized for various CPUs
define BLURB
  Liboil is a library of simple functions that are optimized for various CPUs.
  These functions are generally loops implementing simple algorithms, such as
  converting an array of N integers to floating-point numbers or multiplying
  and summing an array of N numbers. Such functions are candidates for significant
  optimization using various techniques, especially by using extended instructions
  provided by modern CPUs (Altivec, MMX, SSE, etc.).
endef

MASTER_SITES = http://liboil.freedesktop.org/download/
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
