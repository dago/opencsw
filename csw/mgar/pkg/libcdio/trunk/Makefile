GARNAME = libcdio
GARVERSION = 0.82
CATEGORIES = lib

DESCRIPTION = Encapsulate CD-ROM reading and control
define BLURB
  The Compact Disc Input and Control library encapsulates CD-ROM reading and control and
  can be used in applications wishing to be oblivious of the OS- and device-dependant
  properties of a CD-ROM. 
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GNU

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
