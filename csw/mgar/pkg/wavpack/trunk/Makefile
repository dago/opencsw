NAME = wavpack
VERSION = 4.60.1
CATEGORIES = lib

DESCRIPTION = Open audio compression format
define BLURB
  WavPack is a completely open audio compression format providing lossless,
  high-quality lossy, and a unique hybrid compression mode. Although the
  technology is loosely based on previous versions of WavPack, the new version 4
  format has been designed from the ground up to offer unparalleled performance
  and functionality.
endef

MASTER_SITES = http://www.wavpack.com/
DISTFILES  = $(DISTNAME).tar.bz2

LICENSE = license.txt

PACKAGES += CSWlibwavpack1
SPKG_DESC_CSWlibwavpack1 = Open audio compression format library, libwavpack.so.1
PKGFILES_CSWlibwavpack1 = $(call pkgfiles_lib,libwavpack.so.1)
RUNTIME_DEP_PKGS_CSWlibwavpack1 += CSWiconv

PACKAGES += CSWwavpack
SPKG_DESC_CSWwavpack = Wavpack audio compression format tools
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWwavpack += CSWiconv
RUNTIME_DEP_PKGS_CSWwavpack += CSWlibwavpack1

PACKAGES += CSWlibwavpack-dev
SPKG_DESC_CSWlibwavpack-dev = Development files for libwavpack.so.1
PKGFILES_CSWlibwavpack-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibwavpack-dev = CSWlibwavpack1

BUILD64_LIBS_ONLY = 1

include gar/category.mk
