NAME = mpg123
VERSION = 1.18.0
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
DISTFILES  = $(DPACKAGES += CSWmpg123
SPKG_DESC_CSWmpg123 = A command-line MP3 player
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWmpg123 += CSWlibmpg123-0
RUNTIME_DEP_PKGS_CSWmpg123 += CSWlibltdl7

PACKAGES += CSWlibmpg123-dev
SPKG_DESC_CSWlibmpg123-dev = Development files for libmpg123.so.0
# The .la files are needed for the main library for dynamically loading the output libs
PKGFILES_DEVEL_LIBTOOL =
PKGFILES_CSWlibmpg123-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibmpg123-dev += CSWlibmpg123-0

PACKAGES += CSWlibmpg123-0
SPKG_DESC_CSWlibmpg123-0 = MP3 decoding library, libmpg123.so.0
PKGFILES_CSWlibmpg123-0 += $(call pkgfiles_lib,libmpg123.so.0)
# These are output libraries, bundle with primary library for now
PKGFILES_CSWlibmpg123-0 += $(call baseisadirs,$(libdir),mpg123/.*)
RUNTIME_DEP_PKGS_CSWlibmpg123-0 += CSWnas
RUNTIME_DEP_PKGS_CSWlibmpg123-0 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibmpg123-0 += CSWlibesd0pg123 +=  = 1
ISAEXEC
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
MERGE_EXCLUDE_LIBTOOL = $(linclude gar/category.mk
