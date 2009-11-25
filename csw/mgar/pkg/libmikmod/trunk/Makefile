GARNAME = libmikmod
GARVERSION = 3.2.0
RELEASE = beta2
DISTVERSION = $(GARVERSION)-$(RELEASE)
DISTNAME = $(GARNAME)-$(DISTVERSION)
CATEGORIES = lib
DESCRIPTION = library for MOD audio files and other types
define BLURB
  library supporting many formats, including mod, s3m, it, and xm. Originally a player for MS-DOS,
endef

MASTER_SITES = http://mikmod.raphnet.net/files/
DISTFILES  = $(GARNAME)-$(GARVERSION)-$(RELEASE).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
