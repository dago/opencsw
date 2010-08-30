# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
GARNAME = ddrescue
GARVERSION = 1.13
CATEGORIES = utils

DESCRIPTION = A data recovery tool
define BLURB
  GNU ddrescue is a data recovery tool. It copies data from one file or block device
  (hard disc, cdrom, etc) to another, trying hard to rescue data in case of read errors.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.lz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.lz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
