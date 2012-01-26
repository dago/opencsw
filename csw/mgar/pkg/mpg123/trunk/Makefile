NAME = mpg123
VERSION = 1.13.3
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A command-line MP3 player
define BLURB
  This is a console based decoder/player for mono/stereo mpeg audio files,
  probably more familiar as MP3 or MP2 files. It's focus is speed.
  It can play MPEG1.0/2.0/2.5 layer I, II, II (1, 2, 3;-) files
  (VBR files are fine, too) and produce output on a number of different ways:
  raw data to stdout and different sound systems depending on your platform.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.bz2

RUNTIME_DEP_PKGS_CSWmpg123 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWmpg123 += CSWlibesd0
RUNTIME_DEP_PKGS_CSWmpg123 += CSWnas
RUNTIME_DEP_PKGS_CSWmpg123 += CSWlibsdl

BUILD64_LIBS_ONLY = 1
EXTRA_BUILD_ISAS = sparcv8plus+vis pentium

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-cpu=generic_fpu

# When we compile 64 bit largefiles are always on
CONFIGURE_ARGS_mm-64 += --disable-largefile
CONFIGURE_ARGS += $(CONFIGURE_ARGS_mm-$(MEMORYMODEL))

# Looks like we do need libtool files for plugins:
#   http://www.opencsw.org/mantis/view.php?id=4145
# Skip for libmpg123, though.
MERGE_EXCLUDE_LIBTOOL = $(libdir)/[^/]*\.la

# The other one is mpg321
# This fixes #4342
ALTERNATIVES = mpg123
ALTERNATIVE_mpg123 = $(bindir)/mpg123 mpg123 $(bindir)/mpg123 100

# Checkpkg can't check this
CHECKPKG_OVERRIDES_CSWmpg123 += surplus-dependency|CSWalternatives

# No package split as nobody seems to use the library
CHECKPKG_OVERRIDES_CSWmpg123 += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWmpg123 += shared-lib-pkgname-mismatch

include gar/category.mk
