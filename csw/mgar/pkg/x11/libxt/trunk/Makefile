GARNAME = libxt
GARVERSION = 1.0.6
CATEGORIES = x11

DESCRIPTION = X11 toolkit intrinsics library
define BLURB
  LibXt provides the X Toolkit Intrinsics, an abstract widget library
  upon which other toolkits are based. Xt is the basis for many toolkits,
  including the Athena widgets (Xaw), and LessTif.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXt-$(GARVERSION)
DISTFILES  = $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PREREQUISITE_PKGS = CSWlibsmdevel

PACKAGES = CSWlibxt CSWlibxtdevel

CATALOGNAME_CSWlibxt = libxt
CATALOGNAME_CSWlibxtdevel = libxt_devel

SPKG_DESC_CSWlibxt = X11 toolkit intrinsics library
SPKG_DESC_CSWlibxtdevel = X11 toolkit intrinsics library development files

REQUIRED_PKGS_CSWlibxtdevel = CSWlibxt

PKGFILES_CSWlibxtdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxtdevel += .*/makestrs.*

BUILD64 = 1
NOISALIST = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

# No need for 64 bit makestrs
MERGE_DIRS_isa-sparcv9 = $(libdir)
MERGE_DIRS_isa-amd64 = $(libdir)

include gar/category.mk
