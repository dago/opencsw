NAME = sox
VERSION = 14.3.2
CATEGORIES = apps

DESCRIPTION = Swiss Army Knife of sound processing utilities
define BLURB
  SoX is the Swiss Army Knife of sound processing utilities. It can convert
  audio files to other popular audio file types and also apply sound effects
  and filters during the conversion.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(DISTNAME).tar.gz

# There is a hack in there to rewind pipes when detecting file formats.
# As the FILE struct is opaque in 64 bit we must disable this for 64 bit.
# But as we only need the library in 64 bit anyway this shouldn't hurt.
PATCHFILES = 0001-Disable-stdio-hack-to-rewind-pipes.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://sox.sourceforge.net/

PACKAGES += CSWsox
CATALOGNAME_CSWsox = sox
SPKG_DESC_CSWsox = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWsox += CSWlibsox1
RUNTIME_DEP_PKGS_CSWsox += CSWvorbis
RUNTIME_DEP_PKGS_CSWsox += CSWlibogg
RUNTIME_DEP_PKGS_CSWsox += CSWlibmad
RUNTIME_DEP_PKGS_CSWsox += CSWlibid3tag
RUNTIME_DEP_PKGS_CSWsox += CSWflac
RUNTIME_DEP_PKGS_CSWsox += CSWlibao
RUNTIME_DEP_PKGS_CSWsox += CSWlibsndfile
RUNTIME_DEP_PKGS_CSWsox += CSWpng
RUNTIME_DEP_PKGS_CSWsox += CSWwavpack
RUNTIME_DEP_PKGS_CSWsox += CSWlibmagic1
RUNTIME_DEP_PKGS_CSWsox += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWsox += CSWzlib

PACKAGES += CSWlibsox1
CATALOGNAME_CSWlibsox1 = libsox1
SPKG_DESC_CSWlibsox1 = SOX Library for Audio Processing
PKGFILES_CSWlibsox1 += $(PKGFILES_RT)
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWvorbis
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWlibogg
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWlibmad
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWlibid3tag
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWflac
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWlibao
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWlibsndfile
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWpng
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWwavpack
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWlibmagic1
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWlibmp3lame0

PACKAGES += CSWlibsox-dev
CATALOGNAME_CSWlibsox-dev = libsox_dev
SPKG_DESC_CSWlibsox-dev = SOX Library Development Files
PKGFILES_CSWlibsox-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibsox-dev = CSWlibsox1

OBSOLETED_BY_CSWlibsox-dev = CSWlibsoxdevel
CATALOGNAME_CSWlibsoxdevel = libsox_devel

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWsox)
BUILD_DEP_PKGS += CSWlibmagic-dev
BUILD_DEP_PKGS += CSWlame-devel

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS +=  --without-libltdl

BUILD64 = 1

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
