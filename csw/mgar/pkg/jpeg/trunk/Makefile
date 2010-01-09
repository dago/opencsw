GARNAME = jpeg
GARVERSION = 6
CATEGORIES = lib

DESCRIPTION = JPEG library and tools by the Independent JPEG Group
define BLURB
  Long description
endef

MASTER_SITES = http://www.ijg.org/files/
DISTFILES  = $(GARNAME)src.v$(GARVERSION).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

EXTRA_CC_FLAGS = -g -w
EXTRA_CXX_FLAGS = -g -w
EXTRA_LD_FLAGS = -g
OPT_FLAGS_SOS =

STRIP_LIBTOOL = 1

include gar/category.mk
