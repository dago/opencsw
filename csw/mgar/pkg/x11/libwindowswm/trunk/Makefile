NAME = libWindowsWM
VERSION = 1.0.1
CATEGORIES = x11
GARTYPE = v2

DESCRIPTION = Cygwin/X rootless window management extension
define BLURB
  WindowsWM is a simple library designed to interface with the Windows-WM extension.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibwindowswm CSWlibwindowswmdevel

CATALOGNAME_CSWlibwindowswm = libwindowswm
CATALOGNAME_CSWlibwindowswmdevel = libwindowswm_devel

SPKG_DESC_CSWlibwindowswm = $(DESCRIPTION)
SPKG_DESC_CSWlibwindowswmdevel = $(DESCRIPTION) development files

BUILD_DEP_PKGS = CSWx11windowswmproto

RUNTIME_DEP_PKGS_CSWlibwindowswm =  CSWlibx11 CSWlibxext
RUNTIME_DEP_PKGS_CSWlibwindowswmdevel = CSWlibwindowswm

PKGFILES_CSWlibwindowswmdevel  = $(PKGFILES_DEVEL)

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

include gar/category.mk
