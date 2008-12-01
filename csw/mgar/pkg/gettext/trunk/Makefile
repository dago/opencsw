GARNAME = gettext
GARVERSION = 0.17
CATEGORIES = lib

DESCRIPTION = GNU gettext
define BLURB
endef

MASTER_SITES = $(GNU_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWggettext)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

EXTRA_BUILD_ISAS_sparc = sparcv9
EXTRA_BUILD_ISAS_i386  = amd64

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

LIBS = -lsec
export LIBS
