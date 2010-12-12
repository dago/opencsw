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
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWiconv

LICENSE = license.txt

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
