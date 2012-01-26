NAME = twolame
VERSION = 0.3.12
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = An optimised MPEG Audio Layer 2 (MP2) encoder based on tooLAME
define BLURB
endef

SF_PROJ = twolame
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
