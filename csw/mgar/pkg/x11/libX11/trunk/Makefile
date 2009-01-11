GARNAME = libX11
GARVERSION = 1.1.5
CATEGORIES = x11

DESCRIPTION = X11 client-side library
define BLURB
This package provides a client interface to the X Window System, otherwise known as 'Xlib'. It provides a complete API for the basic functions of the window system. 
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWlibx11 = $(DESCRIPTION)
SPKG_DESC_CSWlibx11devel = $(DESCRIPTION) development package

DISTFILES    += $(call admfiles,CSWlibx11devel, )
DISTFILES    += $(call admfiles,CSWlibx11, )

PKGFILES_CSWlibx11devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibx11devel += $(prefix)/X11/include/.*
PKGFILES_CSWlibx11devel += $(prefix)/X11/lib/.*\.a
PKGFILES_CSWlibx11devel += $(prefix)/X11/lib/pkgconfig/.*

include gar/category.mk

