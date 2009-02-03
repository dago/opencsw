GARNAME = libxfce4util
CATEGORIES = xfce

DESCRIPTION = Xfce Utilities Library 
define BLURB
  Xfce Utilities Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWlibxfce4util, )
DISTFILES += $(call admfiles,CSWlibxfce4utildoc, )
DISTFILES += $(call admfiles,CSWlibxfce4utildev, )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_DESC_CSWlibxfxe4util    = $(DESCRIPTION)
SPKG_DESC_CSWlibxfxe4utildev = $(DESCRIPTION) development package
SPKG_DESC_CSWlibxfxe4utildoc = $(DESCRIPTION) documentation package

# PATCHFILES += gar-base.diff

PKGFILES_CSWlibxfce4utildev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxfce4utildev += $(prefix)/X11/include/.*
PKGFILES_CSWlibxfce4utildev += $(prefix)/X11/lib/.*\.a
PKGFILES_CSWlibxfce4utildev += $(prefix)/X11/lib/pkgconfig/.*

PKGFILES_CSWlibxfce4utildoc  = $(prefix)/share/doc/.*

REQUIRED_PKGS_CSWlibxfce4util    = 
REQUIRED_PKGS_CSWlibxfce4utildev = CSWlibxfce4util
REQUIRED_PKGS_CSWlibxfce4utildoc = CSWlibxfce4util

include gar/category.mk

