GARNAME = wavpack
GARVERSION = 4.60.0
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
PATCHFILES += 0001-Add-support-for-Sun-Studio-compiler.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

REQUIRED_PKGS = CSWiconv

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
