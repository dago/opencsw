GARNAME = fontconfig
GARVERSION = 2.2.1
CATEGORIES = lib

DESCRIPTION = A library for configuring and customizing font access.
define BLURB
  Fontconfig is a library for configuring and customizing font access. It
  contains two essential modules, the configuration module which builds an
  internal configuration from XML files and the matching module which accepts
  font patterns and returns the nearest matching font.
endef

MASTER_SITES = http://www.fontconfig.org/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWfconfig,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
