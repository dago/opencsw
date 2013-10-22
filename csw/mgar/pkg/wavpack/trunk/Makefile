NAME = wavpack
VERSION = 4.70.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Open audio compression format
define BLURB
  WavPack is a completely open audio compression format providing lossless,
  high-quality lossy, and a unique hybrid compression mode. Although the
  technology is loosely based on previous versions of WavPack, the new version 4
  format has been designed from the ground up to offer unparalleled performance
  and functionality.
endef

MASTER_SITES = http://www.wavpac+= $(DISTNAME).tar.bz2

PATCHFILES += 0001-Includes-are-needed-for-other-compilers-too.patchNSE = license.txt

PACKAGES += CSWlibwavpack1
SPKG_DESC_CSWlibwavpack1 = Open audio compression format library, libwavpack.so.1
PKGFILES_CSWlibwavpack1 = $(call pkgfiles_lib,ack1 += CSWiconv

PACKAGES += CSWwavpack
SPKG_DESC_CSWwavpack = Wavpack audio compression format tools
# PKGFILES is catchall
RUNTIME_DEP_PKGS_libiconv2vpack += CSWiconv
RUNTIME_DEP_PKGS_CSWwavpack += CSWlibwavpack1

PACKAGES += CSWlibwavpack-dev
SPKG_DESC_CSWlibwavpack-dev = Development files for libwavpack.so.1
PKGFILES_CSWlibwavpack-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibwavpack-dev = CSWlib = 1
ISAEXEC = 1

include gar/category.mk
