NAME = libao
VERSION = 1.1.0
CATEGORIES = lib

DESCRIPTION = Cross-platform audio library
define BLURB
  libao is a way to easily add cross-platform audio output to your program.
  Output devices are implemented as dynamic plugins, and support for OSS, ESD,
  ALSA, aRTs, Solaris, and Irix outputs are currently supported.
endef

MASTER_SITES = http://downloads.xiph.org/releases/ao/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.xiph.org/ao/

FOREIGN_PACKAGES += CSWlibao2
OBSOLETES_CSWlibao2 = CSWlibao

PACKAGES += CSWlibao4
CATALOGNAME_CSWlibao4 = libao4
SPKG_DESC_CSWlibao4 = Cross-platform audio library, libao.so.4
PKGFILES_CSWlibao4 += $(call pkgfiles_lib,libao.so.4)
# These are private libraries
PKGFILES_CSWlibao4 += $(call baseisadirs,$(libdir),ao/.*)
RUNTIME_DEP_PKGS_CSWlibao4 += CSWesound
OBSOLETES_CSWlibao4 = CSWlibao

PACKAGES += CSWlibao-dev
CATALOGNAME_CSWlibao-dev = libao_dev
SPKG_DESC_CSWlibao-dev = Development files for libao.so.4
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibao-dev = CSWlibao4

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
