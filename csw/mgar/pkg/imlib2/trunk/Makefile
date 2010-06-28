GARNAME = imlib2
GARVERSION = 1.4.4
CATEGORIES = lib

DESCRIPTION = Imlib 2 is the successor to Imlib, a powerful graphics library
define BLURB
  Imlib 2 is the successor to Imlib. It is NOT a newer version -- it is a completely new library.
  Imlib 2 can be installed alongside Imlib 1.x without any problems since they are effectively
  different libraries which have very similar functionality. Please see the homepage for the
  long description of the differences.
endef

SF_PROJ = enlightenment
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWbzip2 CSWftype2 CSWgiflibrt CSWjpeg CSWlibid3tag
RUNTIME_DEP_PKGS += CSWpng CSWtiff CSWzlib

BUILD64 = 1
NOISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_SCRIPTS_isa-extra = copy-relocated-only copy-config-only
MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk
