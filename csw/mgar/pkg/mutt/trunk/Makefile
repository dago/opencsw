GARNAME = mutt
GARVERSION = 1.5.19
CATEGORIES = apps

DESCRIPTION = A text-based mail client for Unix operating systems.
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS_CSWmutt = CSWggettextrt CSWiconv CSWlibidn CSWncurses

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include gar/category.mk
