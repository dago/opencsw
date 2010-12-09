# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
GARNAME = gorilla
GARVERSION = 1.4
CATEGORIES = apps

DESCRIPTION = A cross-platform, Tcl/Tk-based Password Manager
define BLURB
  Long description
endef

VENDOR_URL   = http://www.fpx.de/fp/Software/Gorilla/
MASTER_SITES = http://www.fpx.de/fp/Software/Gorilla/download/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
