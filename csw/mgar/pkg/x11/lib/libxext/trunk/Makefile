GARNAME = libxext
GARVERSION = 1.1.1
CATEGORIES = x11

DESCRIPTION = X11 miscellaneous extensions library1
define BLURB
  LibXext provides an X Window System client interface to several extensions
  to the X protocol, iincluding DOUBLE-BUFFER (DBE), DPMS, Extended-Visual-Information
  (EVI), LBX, MIT-SHM, MIT-SUNDRY-NONSTANDARD, Multi-Buffering, SECURITY, SHAPE,
  SHAPE, SYNC, TOG-CUP, XC-APPGROUP, XC-MISC, XTEST and possibly others.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXext-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWx11xextproto CSWlibx11devel CSWlibxaudevel

PACKAGES = CSWlibxext CSWlibxextdevel

CATALOGNAME_CSWlibxext = libxext
CATALOGNAME_CSWlibxextdevel = libxext_devel

SPKG_DESC_CSWlibxext = X11 miscellaneous extensions library
SPKG_DESC_CSWlibxextdevel = X11 miscellaneous extensions library development files

REQUIRED_PKGS_CSWlibxext = CSWlibx11 CSWlibxau
REQUIRED_PKGS_CSWlibxextdevel = CSWlibxext

PKGFILES_CSWlibxextdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
