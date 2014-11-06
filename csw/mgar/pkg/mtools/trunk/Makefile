NAME = mtools
VERSION = 4.0.18
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Read/write/list/format DOS disks under Unix
define BLURB
  Mtools is a collection of utilities to access MS-DOS disks from GNU
  and Unix without mounting them. It supports long file names, OS/2 Xdf
  disks, ZIP/JAZ disks and 2m disks (store up to 1992k on a high density
  3 1/2 disk).
endef

MASTER_SITES = $(GNU+= $(DISTNAME).tar.lz

# Use patch until this is fixed
#   https://lists.gnu.org/archive/html/info-mtools/2013-01/msg00003.html
PATCHFILES += 0001-Use-workaround-for-strndup.patch

RUNTIME_DEP_PKGS_CSWmtools += CSWlibiconv2

EXTRA_LINKER_FLAGS = -liconv -lnsl

include gar/category.mk
