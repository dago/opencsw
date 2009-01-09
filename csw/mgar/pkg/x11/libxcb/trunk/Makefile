GARNAME = libxcb
GARVERSION = 1.1
CATEGORIES = x11

DESCRIPTION = The XCB library
define BLURB
The XCB library provides an interface to the X Window System protocol, designed to replace the Xlib interface
endef

MASTER_SITES =http://xcb.freedesktop.org/dist/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWlibxcb = The XCB library
SPKG_DESC_CSWlibxcbdevel = The XCB library development package

DISTFILES    += $(call admfiles,CSWlibxcbdevel, )
DISTFILES    += $(call admfiles,CSWlibxcb, )

PKGFILES_CSWlibxcbdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxcbdevel += $(prefix)/X11/include/.*
PKGFILES_CSWlibxcbdevel += $(prefix)/X11/lib/.*\.a
PKGFILES_CSWlibxcbdevel += $(prefix)/X11/lib/pkgconfig/.*

include gar/category.mk



