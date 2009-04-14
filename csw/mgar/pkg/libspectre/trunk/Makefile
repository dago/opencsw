GARNAME = libspectre
GARVERSION = 0.2.2
CATEGORIES = lib

DESCRIPTION = A small library for rendering Postscript documents
define BLURB
endef

MASTER_SITES = http://libspectre.freedesktop.org/releases/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = patch-stdint.diff

SPKG_SOURCEURL = http://libspectre.freedesktop.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWgs

# Disable for now as libgs is missing 64 bit
#BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
