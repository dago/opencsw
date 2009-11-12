GARNAME = xchm
GARVERSION = 1.17
CATEGORIES = utils

DESCRIPTION = Cross-platform GUI front-end to chmlib (.chm reader)
define BLURB
  xCHM is a cross-platform GUI front-end to chmlib, with borrowed bits from Pabs' chmdeco project.
  xCHM can show the content tree if one is available, print pages, change font face and size,
  remember bookmarks, display a searchable index, and search for words in the current page and the whole book.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES  = 0001-Fix-extra-comma-at-end-of-enum.patch
PATCHFILES += 0002-Remove-W-Wall-for-Sun-Studio.patch
PATCHFILES += 0003-Use-inttypes.h-instead-of-stdint.h.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWchmlib CSWwxwidgetscommon CSWwxwidgetsgtk2
PREREQUISITE_PKGS = $(REQUIRED_PGKS) CSWwxwidgetsdevel

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
