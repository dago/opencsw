NAME = mtools
VERSION = 4.0.17
CATEGORIES = utils

DESCRIPTION = Read/write/list/format DOS disks under Unix
define BLURB
  Mtools is a collection of utilities to access MS-DOS disks from GNU
  and Unix without mounting them. It supports long file names, OS/2 Xdf
  disks, ZIP/JAZ disks and 2m disks (store up to 1992k on a high density
  3 1/2 disk).
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.lz

RUNTIME_DEP_PKGS = CSWiconv

EXTRA_LINKER_FLAGS = -liconv -lnsl

include gar/category.mk
