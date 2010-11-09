GARNAME = sox
GARVERSION = 14.3.1
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

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://sox.sourceforge.net/

PACKAGES = CSWsox CSWlibsox1 CSWlibsoxdevel

CATALOGNAME_CSWsox         = sox
CATALOGNAME_CSWlibsox1     = libsox1
CATALOGNAME_CSWlibsoxdevel = libsox_devel

SPKG_DESC_CSWsox         = $(DESCRIPTION)
SPKG_DESC_CSWlibsox1     = SOX Library for Audio Processing
SPKG_DESC_CSWlibsoxdevel = SOX Library Development Files

RUNTIME_DEP_PKGS_CSWsox = CSWlibsox1 CSWvorbis CSWlibogg CSWlibmad CSWlame CSWlibid3tag
RUNTIME_DEP_PKGS_CSWsox += CSWflac CSWlibao CSWlibsndfile CSWpng CSWwavpack CSWzlib CSWlibmagic

RUNTIME_DEP_PKGS_CSWlibsox1 = CSWvorbis CSWlibogg CSWlibmad CSWlame CSWlibid3tag
RUNTIME_DEP_PKGS_CSWlibsox1 += CSWflac CSWlibao CSWlibsndfile CSWpng CSWwavpack CSWzlib CSWlibmagic

RUNTIME_DEP_PKGS_CSWlibsoxdevel = CSWlibsox1

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWsox)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS +=  --without-libltdl

BUILD64 = 1
NOISAEXEC = 1
TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

PKGFILES_CSWlibsox1 = $(PKGFILES_RT)
PKGFILES_CSWlibsoxdevel = $(PKGFILES_DEVEL)

include gar/category.mk
