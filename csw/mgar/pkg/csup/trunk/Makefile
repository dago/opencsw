GARNAME = csup
GARVERSION = snap
PATCHLEVEL = 20060318
CATEGORIES = apps

DESCRIPTION = A replacement for CVSup
define BLURB
A solid replacement for CVSup for checkout-only functionality.
endef

MASTER_SITES = http://www.mu.org/~mux/
DISTFILES  = $(GARNAME)-$(GARVERSION)-$(PATCHLEVEL).tgz
DISTFILES += $(call admfiles,CSWcsup,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
