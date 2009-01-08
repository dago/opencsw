GARNAME = libXdmcp
GARVERSION = 1.0.2
CATEGORIES = lib

DESCRIPTION = X11 authorisation library
define BLURB
This package provides the main interface to the X11 display manager control protocol library, which allows for remote logins to display managers. 
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWlibxdmcp = X11 authorisation library
SPKG_DESC_CSWlibxdmcpdevel = X11 authorisation library development package

DISTFILES    += $(call admfiles,CSWlibxdmcpdevel, )
DISTFILES    += $(call admfiles,CSWlibxdmcp, )

PKGFILES_CSWlibxdmcpdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxdmcpdevel += $(prefix)/X11/include/.*
PKGFILES_CSWlibxdmcpdevel += $(prefix)/X11/lib/.*\.a
PKGFILES_CSWlibxdmcpdevel += $(prefix)/X11/lib/pkgconfig/.*

include gar/category.mk
