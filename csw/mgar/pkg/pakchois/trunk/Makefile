GARNAME = pakchois
GARVERSION = 0.4
CATEGORIES = lib

DESCRIPTION = Just another PKCS #11 wrapper library
define BLURB
  pakchois is just another PKCS #11 wrapper library. pakchois aims to provide
  a thin wrapper over the PKCS#11 interface.
endef

MASTER_SITES = http://www.manyfish.co.uk/pakchois/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.manyfish.co.uk/pakchois/

BUILD64 = 1
NOISALIST = 1
EXTRA_LINKER_FLAGS = -lintl
CONFIGURE_ARGS = $(DIRPATHS)

REQUIRED_PKGS = CSWggettextrt

include gar/category.mk
