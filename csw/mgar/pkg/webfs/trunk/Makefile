# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
GARNAME = webfs
GARVERSION = 1.21
CATEGORIES = apps

DESCRIPTION = Lightweight HTTP server for static content
define BLURB
  Long description
endef

VENDOR_URL   = http://linux.bytesex.org/misc/webfs.html
MASTER_SITES = http://dl.bytesex.org/releases/webfs/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =

include gar/category.mk

PATH := $(prefix)/gnu:$(PATH)
