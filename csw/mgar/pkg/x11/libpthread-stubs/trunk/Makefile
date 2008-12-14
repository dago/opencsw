GARNAME = libpthread-stubs
GARVERSION = 0.1
CATEGORIES = x11

DESCRIPTION = pthread stubs not provided by native libc
define BLURB
This library provides weak aliases for pthread functions not provided in libc or otherwise available by default. Libraries like libxcb rely on pthread stubs to use pthreads optionally, becoming thread-safe when linked to libpthread, while avoiding any performance hit when running single-threaded. libpthread-stubs supports this behavior even on platforms which do not supply all the necessary pthread stubs. On platforms which already supply all the necessary pthread stubs, this package has no content. 
endef

MASTER_SITES = $(XCB_MASTER_SITES)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES    += $(call admfiles,CSWlibpthreadstubs, depend)

include gar/category.mk

