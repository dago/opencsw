NAME = libXxf86vm
VERSION = 1.1.0
CATEGORIES = x11

DESCRIPTION = X11 XFree86 video mode extension library
define BLURB
  libXxf86vm provides an interface to the XFree86-VidModeExtension extension, which allows client applications to get and set video mode timings in extensive detail. It is used by the xvidtune program in particular. 
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibxxf86vm CSWlibxxf86vmdevel

CATALOGNAME_CSWlibxxf86vm = libxxf86vm
CATALOGNAME_CSWlibxxf86vmdevel = libxxf86vm_devel

SPKG_DESC_CSWlibxxf86vm = $(DESCRIPTION)
SPKG_DESC_CSWlibxxf86vmdevel = $(DESCRIPTION) development files

BUILD_DEP_PKGS = CSWx11xf86vidmdproto
RUNTIME_DEP_PKGS_CSWlibxxf86vm = CSWlibx11 CSWlibxext
RUNTIME_DEP_PKGS_CSWlibxxf86vmdevel = CSWlibxxf86vm

PKGFILES_CSWlibxxf86vmdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
