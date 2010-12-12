NAME = mpg123
VERSION = 1.10.0
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
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWesound CSWlibsdl CSWlibtoolrt

BUILD64 = 1
NOISAEXEC = 1
EXTRA_BUILD_ISAS = sparcv8plus+vis pentium
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-cpu=generic_fpu

# When we compile 64 bit largefiles are always on
CONFIGURE_ARGS_mm-64 += --disable-largefile
CONFIGURE_ARGS += $(CONFIGURE_ARGS_mm-$(MEMORYMODEL))

TEST_TARGET = check

# Looks like we do need libtool files for plugins:
#   http://www.opencsw.org/mantis/view.php?id=4145
# Skip for libmpg123, though.
MERGE_EXCLUDE_LIBTOOL = $(libdir)/[^/]*\.la

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
