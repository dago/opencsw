GARNAME = mtools
GARVERSION = 4.0.12
CATEGORIES = utils

DESCRIPTION = read/write/list/format DOS disks under Unix
define BLURB
  Mtools is a collection of utilities to access MS-DOS disks from GNU
  and Unix without mounting them. It supports long file names, OS/2 Xdf
  disks, ZIP/JAZ disks and 2m disks (store up to 1992k on a high density
  3 1/2 disk).
endef

MASTER_SITES = http://ftp.gnu.org/gnu/mtools/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
PATCHFILES = 0001-Removeprototypes-unknown-to-Sun-Studio.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# X11 is also used, but Openwin X11 is sufficient.
REQUIRED_PKGS = CSWiconv

EXTRA_LINKER_FLAGS = -liconv

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
