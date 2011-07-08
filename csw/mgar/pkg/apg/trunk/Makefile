NAME = apg
VERSION = 2.2.3
GARTYPE = v1
CATEGORIES = utils

DESCRIPTION = Automated Password Generator
define BLURB
endef

MASTER_SITES = http://www.adel.nursat.kz/apg/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += $(call admfiles,CSWapg)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = download/$(NAME)-(\d+(?:\.\d+)*).tar.gz
UPSTREAM_MASTER_SITES = http://www.adel.nursat.kz/apg/download.shtml

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
