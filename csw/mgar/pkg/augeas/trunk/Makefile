GARNAME = augeas
GARVERSION = 0.7.0
CATEGORIES = lib

DESCRIPTION = A configuration editing tool
define BLURB
  Augeas is a configuration editing tool. It parses configuration files in
  their native formats and transforms them into a tree. Configuration changes
  are made by manipulating this tree and saving it back into native config files.
endef

MASTER_SITES = http://augeas.net/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://augeas.net

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
