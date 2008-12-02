GARNAME = quanta
CATEGORIES = kde

DESCRIPTION = The KDE Web Development Tool (gcc3)
define BLURB
  LONG DESCRIPTION
endef

PKGDIST    = kdewebdev-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWquantagcc,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = kdewebdev-(\d+(?:\.\d+)*).tar.bz2

DEPENDS +=

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
