NAME = pakchois
VERSION = 0.4
CATEGORIES = lib

DESCRIPTION = Just another PKCS \#11 wrapper library
define BLURB
  pakchois is just another PKCS \#11 wrapper library. pakchois aims to provide
  a thin wrapper over the PKCS \#11 interface.
endef

MASTER_SITES = http://www.manyfish.co.uk/pakchois/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += COPYING

VENDOR_URL = http://www.manyfish.co.uk/pakchois/

PACKAGES += CSWlibpakchois0
SPKG_DESC_CSWlibpakchois0 = Just another PKCS \#11 wrapper library, libpakchois.so.0
PKGFILES_CSWlibpakchois0 = $(call pkgfiles_lib,libpakchois.so.0)
RUNTIME_DEP_PKGS_CSWlibpakchois0 += CSWlibintl8
OBSOLETED_BY_CSWlibpakchois0 = CSWpakchois

PACKAGES += CSWlibpakchois-dev
SPKG_DESC_CSWlibpakchois-dev = Development files for libpakchois.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibpakchois-dev = CSWlibpakchois0

BUILD64_LIBS_ONLY = 1
NOISALIST = 1
EXTRA_LINKER_FLAGS = -lintl

include gar/category.mk
