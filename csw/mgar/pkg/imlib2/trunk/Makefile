GARNAME = imlib2
GARVERSION = 1.4.2
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
DISTFILES += $(GARNAME)_loaders-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

REQUIRED_PKGS = CSWbzip2 CSWftype2 CSWgiflibrt CSWjpeg CSWlibid3tag
REQUIRED_PKGS += CSWlibxext CSWpng CSWtiff CSWzlib

#EXTRA_INC = $(prefix)/X11/include
#EXTRA_LIB = $(prefix)/X11/lib
#EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
#CONFIGURE_ARGS += --x-include=$(prefix)/X11/include
#CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

TEST_TARGET = check

include gar/category.mk
