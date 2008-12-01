GARNAME = cabextract
GARVERSION = 1.2
CATEGORIES = utils

DESCRIPTION = Extract Microsoft cabinet files
define BLURB
  cabextract is Free Software for extracting Microsoft cabinet files, also
  called .CAB files, on UNIX or UNIX-like systems. cabextract is distributed
  under the GPL license. It is based on the portable LGPL libmspack library.
  cabextract supports all special features and all compression formats of
  Microsoft cabinet files.
endef

MASTER_SITES = http://www.kyz.uklinux.net/downloads/

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWcabextract,prototype depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

# cabextract doesn't have a test target
TEST_TARGET =

SPKG_SOURCEURL = http://www.kyz.uklinux.net/cabextract.php

include gar/category.mk

# cabextract is forgetting to link against libintl, so reminding it
LDFLAGS += -lintl
