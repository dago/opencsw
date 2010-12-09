# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! libxcursor packages missing (currently only available in the CSW
#   X11 stack which should be obsoleted)
#
GARNAME = freerdp
GARVERSION = 0.8.2
CATEGORIES = utils

DESCRIPTION = RDP client. Fork of the rdesktop project.
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
