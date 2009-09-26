GARNAME = libXcursor
GARVERSION = 1.1.10
CATEGORIES = x11

DESCRIPTION = X client-side cursor loading library
define BLURB
  Xcursor is a simple library designed to help locate and load cursors for the X Window System.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibfs CSWlibfsdevel

CATALOGNAME_CSWlibfs = libfs
CATALOGNAME_CSWlibfsdevel = libfs_devel

SPKG_DESC_CSWlibfs = X11 Inter-Client Exchange library
SPKG_DESC_CSWlibfsdevel = X11 Inter-Client Exchange library development files

REQUIRED_PKGS_CSWlibfsdevel = CSWlibfs

PKGFILES_CSWlibfsdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
