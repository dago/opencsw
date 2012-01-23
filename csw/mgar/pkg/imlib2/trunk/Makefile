NAME = imlib2
VERSION = 1.4.4
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
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS = CSWbzip2 CSWftype2 CSWgiflibrt CSWjpeg CSWlibid3tag
RUNTIME_DEP_PKGS += CSWpng CSWtiff CSWzlib

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_SCRIPTS_isa-extra = copy-relocated-only copy-config-only
MERGE_DIRS_isa-extra = $(libdir)

CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/bmp.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/tiff.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/bz2.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/jpeg.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/pnm.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/zlib.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/lbm.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/xpm.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/gif.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libImlib2.so.1.4.4
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/tga.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/png.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/argb.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/filters/colormod.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/filters/bumpmap.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/filters/testfilter.so
CHECKPKG_OVERRIDES_CSWimlib2 += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/imlib2/loaders/id3.so

include gar/category.mk
