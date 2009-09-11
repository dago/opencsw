GARNAME = gdome2
GARVERSION = 0.8.1
CATEGORIES = lib

DESCRIPTION = A DOM Level 2 Implementation
define BLURB
  libgdome, the DOM C library developped for the Gnome project
endef

MASTER_SITES = http://gdome2.cs.unibo.it/tarball/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = patch-nowall.diff

REQUIRED_PKGS = CSWggettextrt CSWglib2 CSWiconv CSWlibxml2 CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://gdome2.cs.unibo.it/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
