GARNAME = libWindowsWM
GARVERSION = 1.0.1
CATEGORIES = x11

DESCRIPTION = Cygwin/X rootless window management extension
define BLURB
  WindowsWM is a simple library designed to interface with the Windows-WM extension.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibwindowswm CSWlibwindowswmdevel

CATALOGNAME_CSWlibwindowswm = libwindowswm
CATALOGNAME_CSWlibwindowswmdevel = libwindowswm_devel

SPKG_DESC_CSWlibwindowswm = $(DESCRIPTION)
SPKG_DESC_CSWlibwindowswmdevel = $(DESCRIPTION) development files

PREREQUISITE_PKGS = CSWx11windowswmproto

REQUIRED_PKGS_CSWlibwindowswm =  CSWlibx11 CSWlibxext
REQUIRED_PKGS_CSWlibwindowswmdevel = CSWlibwindowswm

PKGFILES_CSWlibwindowswmdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
