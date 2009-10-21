GARNAME = libXxf86misc
GARVERSION = 1.0.1
CATEGORIES = x11

DESCRIPTION = X11 XFree86 miscellaneous extension library
define BLURB
  libXxf86misc provides an interface to the XFree86-Misc extension, which allows client applications to query the current keyboard and mouse settings of the running XFree86-based (XFree86, Xorg) server.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxxf86misc CSWlibxxf86miscdevel

CATALOGNAME_CSWlibxxf86misc = libxxf86misc
CATALOGNAME_CSWlibxxf86miscdevel = libxxf86misc_devel

SPKG_DESC_CSWlibxxf86misc = $(DESCRIPTION)
SPKG_DESC_CSWlibxxf86miscdevel = $(DESCRIPTION) development files

PREREQUISITE_PKGS = CSWxf86miscproto
REQUIRED_PKGS_CSWlibxxf86misc = CSWlibx11 CSWlibxext
REQUIRED_PKGS_CSWlibxxf86miscdevel = CSWlibxxf86misc

PKGFILES_CSWlibxxf86miscdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
