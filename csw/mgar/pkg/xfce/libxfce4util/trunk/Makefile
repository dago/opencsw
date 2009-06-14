GARNAME = libxfce4util
CATEGORIES = xfce

DESCRIPTION = Xfce Utilities Library 
define BLURB
  Xfce Utilities Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# Catalog description
PACKAGES = CSWlibxfce4util CSWlibxfce4utildev CSWlibxfce4utildoc

CATALOGNAME_CSWlibxfce4util = libxfce4util
CATALOGNAME_CSWlibxfce4utildev = libxfce4utildev
CATALOGNAME_CSWlibxfce4utildoc = libxfce4utildoc

# Package description
SPKG_DESC_CSWlibxfce4util    = $(DESCRIPTION)
SPKG_DESC_CSWlibxfce4utildev = $(DESCRIPTION) development package
SPKG_DESC_CSWlibxfce4utildoc = $(DESCRIPTION) documentation package

# Dynamic prototype
PKGFILES_CSWlibxfce4utildev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxfce4utildev += /opt/csw/include/xfce4/libxfce4util/.*
PKGFILES_CSWlibxfce4utildoc  = /opt/csw/share/gtk-doc/.*

# Defines dependencies
REQUIRED_PKGS_CSWlibxfce4util    = CSWggettextrt CSWglib2
REQUIRED_PKGS_CSWlibxfce4utildev = CSWlibxfce4util
REQUIRED_PKGS_CSWlibxfce4utildoc = CSWlibxfce4util

# BUILD64 = 1
# NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = 

include gar/category.mk

