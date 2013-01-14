NAME = sox
VERSION = 14.4.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Swiss Army Knife of sound processing utilities
define BLURB
  SoX is the Swiss Army Knife of sound processing utilities. It can convert
  audio files to other popular audio file types and also apply sound effects
  and filters during the conversion.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES bz2$(DISTNAME).tar.gz

# There is a hack in there to rewind pipes when detecting file formats.
# As the FILE struct is opaque in 64 bit we must disable this for 64 bit.
# But as we only need the library in 64 bit anyway this shouldn't hurt.
PATCHFILES = 0001-Disable-stdio-hack-to-rePATCHFILES += 0001-Fix-SunStudio-version-string.patch(?:\.\d+)*).tar.gz

VENDOR_URL = http://sox.sourceforge.net/

PACKAGES += CSWsox
CATALOGNAME_CSWsox = sox
SPKG_DESC_CSWsox = $(DESCRIPTION)
RUNTIME_DEP_PKGS_C2

PACKAGES += CSWlibsox2
CATALOGNAME_CSWlibsox2 = libsox2
SPKG_DESC_CSWlibsox2 = SOX Library for audio processing, libsox.so.2
PKGFILES_CSWlibsox2 += $(call pkgfiles_lib,libsox.so.2)
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibvorbisfile3
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibmad0
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibflac8
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibao4
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibwavpack1
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibmagic1
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibsndfile
RUNTIME_DEP_PKGS_CSWlibsox2 += CSWlibid3tag += CSWlibmp3lame0

PACKAGES += CSWlibsox-dev
CATALOGNAME_CSWlibsox-dev = libsox_dev
SPKG_DESC_CSlibrary development files, libsox.so.2
PKGFILES_CSWlibsox-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibsox-dev = CSWlibsox2x-dev = CSWlibsox1

OBSOLETED_BY_CSWlibsox-dev = CSWlibsoxdevel
CATALOGNAME_CSWlibsoxde_stub

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWsox)
BUILD_DEP_PKGS += CSWlibmagic-dev
BUILD_DEP_PKGS += CSWlibmp3lame-devS += CSWlame-devel

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS +=  --withou = 1
ISAEXEC = 1

include gar/category.mk
