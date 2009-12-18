GARNAME = mpg123
GARVERSION = 1.10.0
CATEGORIES = apps

DESCRIPTION = A command-line MP3 player
define BLURB
  This is a console based decoder/player for mono/stereo mpeg audio files,
  probably more familiar as MP3 or MP2 files. It's focus is speed.
  It can play MPEG1.0/2.0/2.5 layer I, II, II (1, 2, 3;-) files
  (VBR files are fine, too) and produce output on a number of different ways:
  raw data to stdout and different sound systems depending on your platform.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

REQUIRED_PKGS = CSWesound CSWlibsdl CSWlibtoolrt

BUILD64 = 1
NO_ISAEXEC = 1
EXTRA_BUILD_ISAS = sparcv8plus+vis pentium
CONFIGURE_ARGS = $(DIRPATHS)

# When we compile 64 bit largefiles are always on
CONFIGURE_ARGS_mm-64 += --disable-largefile
CONFIGURE_ARGS += $(CONFIGURE_ARGS_mm-$(MEMORYMODEL))

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
