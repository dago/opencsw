NAME = mplex
VERSION = 0.9.3
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Allows multiplexing of port 443 for ssh and https at the same time
define BLURB
endef

MASTER_SITES = http://www.pond-weed.com/multiplex/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_LDFLAGS = -lsocket -lnsl

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
