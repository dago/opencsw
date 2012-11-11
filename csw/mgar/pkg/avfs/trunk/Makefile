# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! build state unknown, work in progress, please verify
#
NAME = avfs
VERSION = 0.9.8
GARTYPE = v2

DESCRIPTION = Virtual file system to access archives, disk images, remote locations
define BLURB
  Long description
endef

VENDOR_URL   = http://avf.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
SF_PROJ      = avf
DISTFILES    = $(NAME)-$(VERSION).tar.bz2
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
