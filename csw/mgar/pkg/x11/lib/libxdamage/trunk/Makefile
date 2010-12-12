NAME = libXdamage
VERSION = 1.1.2
CATEGORIES = x11

DESCRIPTION = X11 Font Services library
define BLURB
  libxdamage, the Font Services library, provides various functions useful to X11 font servers, and clients connecting to font servers. It is not used outside of these implementations.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxdamage CSWlibxdamagedevel

CATALOGNAME_CSWlibxdamage = libxdamage
CATALOGNAME_CSWlibxdamagedevel = libxdamage_devel

SPKG_DESC_CSWlibxdamage = $(DESCRIPTION)
SPKG_DESC_CSWlibxdamagedevel = $(DESCRIPTION) development files

RUNTIME_DEP_PKGS_CSWlibxdamage =  CSWlibx11 CSWlibxfixes
RUNTIME_DEP_PKGS_CSWlibxdamagedevel = CSWlibxdamage

# BUILD_DEP_PKGS = CSWdamageproto

PKGFILES_CSWlibxdamagedevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
