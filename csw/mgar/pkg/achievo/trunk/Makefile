NAME = achievo
VERSION = 1.4.3
GARTYPE = v2

DESCRIPTION = A flexible web-based resource management tool for business environments
define BLURB
  Achievo is a flexible web-based resource management tool for business environments.
  Achievo's resource management capabilities will enable organisations to support their
  business processes in a simple, but effective manner.
endef

MASTER_SITES = http://www.achievo.org/downloads/achievo/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.achievo.org

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
