GARNAME = imlib2
GARVERSION = 1.4.2
CATEGORIES = x11

DESCRIPTION = Imlib 2 is the successor to Imlib, a powerful graphics library
define BLURB
  Imlib 2 is the successor to Imlib. It is NOT a newer version -- it is a completely new library.
  Imlib 2 can be installed alongside Imlib 1.x without any problems since they are effectively
  different libraries which have very similar functionality. Please see the homepage for the
  long description of the differences.
endef

SF_PROJ = enlightenment
MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES   += $(GARNAME)_loaders-$(GARVERSION).tar.bz2

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

RUNTIME_DEP_PKGS += CSWbzip2
RUNTIME_DEP_PKGS += CSWftype2
RUNTIME_DEP_PKGS += CSWgiflibrt
RUNTIME_DEP_PKGS += CSWjpeg
RUNTIME_DEP_PKGS += CSWlibid3tag
RUNTIME_DEP_PKGS += CSWlibxext
RUNTIME_DEP_PKGS += CSWpng
RUNTIME_DEP_PKGS += CSWtiff
RUNTIME_DEP_PKGS += CSWzlib

EXTRA_INC = /opt/csw/include
EXTRA_LIB = /opt/csw/lib
# EXTRA_PKG_CONFIG_DIRS = /opt/csw/lib

BUILD64 = 1
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --x-include=$(prefix)/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/lib/$(MM_LIBDIR))

TEST_TARGET = check

include gar/category.mk
