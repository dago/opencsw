GARNAME = libxi
GARVERSION = 1.3
CATEGORIES = x11

DESCRIPTION = Client library for XInput
define BLURB
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXi-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWx11xproto CSWlibx11devel CSWx11xextproto CSWlibxextdevel CSWx11inputproto

PACKAGES = CSWlibxi CSWlibxidevel

CATALOGNAME_CSWlibxi = libxi
CATALOGNAME_CSWlibxidevel = libxi_devel

SPKG_DESC_CSWlibxi = Client library for XInput
SPKG_DESC_CSWlibxi = Client library for XInput development files

#REQUIRED_PKGS_CSWlibxi = 
REQUIRED_PKGS_CSWlibxidevel = CSWlibxi

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibxidevel = $(PKGFILES_DEVEL)

PATCHFILES  = XGetCPtr.c.diff
PATCHFILES += XSetCPtr.c.diff
PATCHFILES += XExtInt.c.diff
PATCHFILES += XIAllowEvents.c.diff
PATCHFILES += XIGrabDevice.c.diff
PATCHFILES += XIQueryDevice.c.diff
PATCHFILES += XIQueryVersion.c.diff
PATCHFILES += XISetDevFocus.c.diff
PATCHFILES += XIGetDevFocus.c.diff
PATCHFILES += XIPassiveGrab.c.diff
PATCHFILES += XIProperties.c.diff
PATCHFILES += XISelEv.c.diff
PATCHFILES += XIWarpPointer.c.diff
PATCHFILES += XIHierarchy.c.diff
PATCHFILES += XIDefineCursor.c.diff
PATCHFILES += XIQueryPointer.c.diff

EXTRA_CFLAGS = -D__solaris__

include gar/category.mk
