# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! libxcursor packages missing (currently only available in the CSW
#   X11 stack which should be obsoleted)
#
NAME = freerdp
VERSION = 0.8.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = RDP client. Fork of the rdesktop project.
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
