NAME = gdome2
VERSION = 0.8.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A DOM Level 2 Implementation
define BLURB
  libgdome, the DOM C library developped for the Gnome project
endef

MASTER_SITES = http://gdome2.cs.unibo.it/tarball/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = patch-nowall.diff
PATCHFILES += patch-doc-destdir.diff
PATCHFILES += patch-use-install.diff

RUNTIME_DEP_PKGS = CSWggettextrt CSWglib2 CSWiconv CSWlibxml2 CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://gdome2.cs.unibo.it/

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
