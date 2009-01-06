GARNAME = libXau
GARVERSION = 1.0.4
CATEGORIES = x11

DESCRIPTION = X11 authorisation library
define BLURB
This package provides the main interface to the X11 authorisation handling, which controls authorisation for X connections, both client-side and server-side. 
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWlibxau = X11 authorisation library
SPKG_DESC_CSWlibxaudevel = X11 authorisation library development package

DISTFILES    += $(call admfiles,CSWlibxaudevel, )
DISTFILES    += $(call admfiles,CSWlibxau, )

PKGFILES_CSWlibxaudevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxaudevel += $(prefix)/X11/include/.*
PKGFILES_CSWlibxaudevel += $(prefix)/X11/lib/.*\.a
PKGFILES_CSWlibxaudevel += $(prefix)/X11/lib/pkgconfig/.*

include gar/category.mk


