NAME = xchm
VERSION = 1.18
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Cross-platform GUI front-end to chmlib (.chm reader)
define BLURB
  xCHM is a cross-platform GUI front-end to chmlib, with borrowed bits from Pabs' chmdeco project.
  xCHM can show the content tree if one is available, print pages, change font face and size,
  remember bookmarks, display a searchable index, and search for words in the current page and the whole book.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES  = 0001-Fix-extra-comma-at-end-of-enum.patch
PATCHFILES += 0002-Remove-W-Wall-for-Sun-Studio.patch
PATCHFILES += 0003-Use-inttypes-instead-of-stdint.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWxchm  = CSWchmlib
RUNTIME_DEP_PKGS_CSWxchm += CSWwxwidgetscommon
RUNTIME_DEP_PKGS_CSWxchm += CSWwxwidgetsgtk2
RUNTIME_DEP_PKGS_CSWxchm += CSWsunmath
RUNTIME_DEP_PKGS_CSWxchm += CSWncurses

BUILD_DEP_PKGS = $(REQUIRED_PGKS) CSWwxwidgetsdevel

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
