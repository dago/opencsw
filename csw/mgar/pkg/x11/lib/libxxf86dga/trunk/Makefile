GARNAME = libXxf86dga
GARVERSION = 1.0.2
CATEGORIES = x11

DESCRIPTION = X11 Direct Graphics Access extension library
define BLURB
  libXxf86dga provides the XFree86-DGA extension, which allows direct graphics access to a framebuffer-like region, and also allows relative mouse reporting, et al. It is mainly used by games and emulators for games. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxxf86dga CSWlibxxf86dgadevel

CATALOGNAME_CSWlibxxf86dga = libxxf86dga
CATALOGNAME_CSWlibxxf86dgadevel = libxxf86dga_devel

SPKG_DESC_CSWlibxxf86dga = $(DESCRIPTION)
SPKG_DESC_CSWlibxxf86dgadevel = $(DESCRIPTION) development files

PREREQUISITE_PKGS = CSWxf86dgaproto

REQUIRED_PKGS_CSWlibxxf86dga = CSWlibx11 CSWlibxext
REQUIRED_PKGS_CSWlibxxf86dgadevel = CSWlibxxf86dga

PKGFILES_CSWlibxxf86dgadevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
