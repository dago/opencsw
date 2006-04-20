GARNAME = fontconfig
GARVERSION = 2.2.1
CATEGORIES = lib

SPKG_PKGNAME = CSWfconfig
SPKG_BITNAME = fontconfig

DESCRIPTION = A library for configuring and customizing font access.
define BLURB
  Fontconfig is a library for configuring and customizing font access. It
  contains two essential modules, the configuration module which builds an
  internal configuration from XML files and the matching module which accepts
  font patterns and returns the nearest matching font.
endef

MASTER_SITES = http://freedesktop.org/~fontconfig/release/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz 

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
