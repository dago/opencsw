NAME = mtools
VERSION = 4.0.16
CATEGORIES = utils

DESCRIPTION = Read/write/list/format DOS disks under Unix
define BLURB
  Mtools is a collection of utilities to access MS-DOS disks from GNU
  and Unix without mounting them. It supports long file names, OS/2 Xdf
  disks, ZIP/JAZ disks and 2m disks (store up to 1992k on a high density
  3 1/2 disk).
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.lz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.lz

RUNTIME_DEP_PKGS = CSWiconv

EXTRA_LINKER_FLAGS = -liconv -lnsl

include gar/category.mk
