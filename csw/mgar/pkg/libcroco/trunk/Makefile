GARNAME = libcroco
GARVERSION = 0.6.2
CATEGORIES = gnome

DESCRIPTION = A CSS parsing and manipulation toolkit
define BLURB
  The Libcroco project is an effort to build a generic Cascading Style
  Sheet (CSS) parsing and manipulation toolkit that can be used by GNOME
  applications in need of CSS support.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

REQUIRED_PKGS = CSWggettextrt CSWglib2 CSWlibxml2

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
