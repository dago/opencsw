GARNAME = libmikmod
GARVERSION = 3.1.11
DISTVERSION = $(GARVERSION)
DISTNAME = $(GARNAME)-$(DISTVERSION)
CATEGORIES = lib
DESCRIPTION = Library for MOD audio files and other types
define BLURB
  Library supporting many formats, including mod, s3m, it, and xm. Originally a player for MS-DOS,
endef

PACKAGES = CSWmikmod
CATALOGNAME = libmikmod
MASTER_SITES = http://mikmod.raphnet.net/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = libmikmod-3.1.11-a.diff
PATCHFILES += 0001-fix-compiling-on-Solaris.patch
LICENSE = COPYING.LIB

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
