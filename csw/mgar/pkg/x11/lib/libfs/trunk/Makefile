GARNAME = libFS
GARVERSION = 1.0.2
CATEGORIES = x11

DESCRIPTION = X11 Font Services library
define BLURB
  libFS, the Font Services library, provides various functions useful to X11 font servers, and clients connecting to font servers. It is not used outside of these implementations.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWlibfs CSWlibfsdevel

CATALOGNAME_CSWlibfs = libfs
CATALOGNAME_CSWlibfsdevel = libfs_devel

SPKG_DESC_CSWlibfs = $(DESCRIPTION)
SPKG_DESC_CSWlibfsdevel = $(DESCRIPTION) development files

REQUIRED_PKGS_CSWlibfsdevel = CSWlibfs

PKGFILES_CSWlibfsdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1

include gar/category.mk
