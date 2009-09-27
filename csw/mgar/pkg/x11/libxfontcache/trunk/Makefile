GARNAME = libXfontcache
GARVERSION = 1.0.4
CATEGORIES = x11

DESCRIPTION = X-TrueType font cache extension client library
define BLURB
  FontCache is an extension that is used by X-TrueType to cache information about fonts. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxfontcache CSWlibxfontcachedevel

CATALOGNAME_CSWlibxfontcache = libxfontcache
CATALOGNAME_CSWlibxfontcachedevel = libxfontcache_devel

SPKG_DESC_CSWlibxfontcache = $(DESCRIPTION)
SPKG_DESC_CSWlibxfontcachedevel = $(DESCRIPTION) development files

PREREQUISITE_PKGS = CSWfontcacheproto
REQUIRED_PKGS_CSWlibxfontcachedevel = CSWlibxfontcache
REQUIRED_PKGS_CSWlibxfontcache      = CSWlibx11 CSWlibxext

PKGFILES_CSWlibxfontcachedevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
