NAME = libvorbis
VERSION = 1.3.2
CATEGORIES = lib

DESCRIPTION = Vorbis codec library
define BLURB
  Ogg Vorbis is a high-quality lossy audio codec that is free of intellectual
  property restrictions. libvorbis is the main vorbis codec library. It depends
  on libogg for bitstream and framing support.
endef

MASTER_SITES = http://downloads.xiph.org/releases/vorbis/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# This is obsoleted
PACKAGES += CSWvorbis
CATALOGNAME_CSWvorbis = libvorbis

PACKAGES += CSWlibvorbis0
CATALOGNAME_CSWlibvorbis0 = libvorbis0
SPKG_DESC_CSWlibvorbis0 = Vorbis codec library, libvorbis.so.0
PKGFILES_CSWlibvorbis0 += $(call baseisadirs,$(libdir),libvorbis\.so\.0(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibvorbis0 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibvorbis0 += CSWsunmath
OBSOLETES_CSWlibvorbis0 = CSWvorbis

PACKAGES += CSWlibvorbisenc2
CATALOGNAME_CSWlibvorbisenc2 = libvorbisenc2
SPKG_DESC_CSWlibvorbisenc2 = Vorbis codec library, libvorbisenc.so.2
PKGFILES_CSWlibvorbisenc2 += $(call baseisadirs,$(libdir),libvorbisenc\.so\.2(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibvorbisenc2 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibvorbisenc2 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibvorbisenc2 += CSWsunmath
OBSOLETES_CSWlibvorbisenc2 = CSWvorbis

PACKAGES += CSWlibvorbisfile3
CATALOGNAME_CSWlibvorbisfile3 = libvorbisfile3
SPKG_DESC_CSWlibvorbisfile3 = Vorbis codec library, libvorbisfile.so.3
PKGFILES_CSWlibvorbisfile3 += $(call baseisadirs,$(libdir),libvorbisfile\.so\.3(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibvorbisfile3 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibvorbisfile3 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibvorbisfile3 += CSWsunmath
OBSOLETES_CSWlibvorbisfile3 = CSWvorbis

PACKAGES += CSWlibvorbis-dev
CATALOGNAME_CSWlibvorbis-dev = libvorbis_dev
SPKG_DESC_CSWlibvorbis-dev = Development files for libvorbis*.so
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibvorbis-dev += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibvorbis-dev += CSWlibvorbisfile3
RUNTIME_DEP_PKGS_CSWlibvorbis-dev += CSWlibvorbisenc2

VENDOR_URL = http://www.vorbis.com/

BUILD64 = 1

EXTRA_LD_FLAGS = -L$(libdir) -lsunmath -lm

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
