GARNAME = libxrender
GARVERSION = 0.9.4
CATEGORIES = x11

DESCRIPTION = X Render Extension Library
define BLURB
  The X Rendering Extension (Render) introduces digital image composition as
  the foundation of a new rendering model within the X Window System.
  Rendering geometric figures is accomplished by client-side tesselation
  into either triangles or trapezoids.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXrender-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz

# Legacy libraries
# The idea is to have the legacy libs in /opt/csw/lib to guarantee the existing
# apps will continue to work. The new lib in /opt/csw/X11/lib relies on the
# OpenCSW-specific X11 libs, whereas the existing one in /opt/csw/lib links
# against the Sun X11.
LEGACYLIB = libXrender.so.1.2.2
DISTFILES += $(LEGACYLIB)-i386
DISTFILES += $(LEGACYLIB)-sparc

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = libXrender-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibxrender CSWlibxrenderdevel

CATALOGNAME_CSWlibxrender      = libxrender
CATALOGNAME_CSWlibxrenderdevel = libxrender_devel

PREREQUISITE_PKGS = CSWxrenderproto
REQUIRED_PKGS_CSWlibxrenderdevel = CSWlibxrender
REQUIRED_PKGS_CSWlibxrender = CSWx11common CSWlibx11

SPKG_DESC_CSWlibxrender = $(DESCRIPTION)
SPKG_DESC_CSWlibxrenderdevel  = $(DESCRIPTION) Development Package

PKGFILES_CSWlibxrenderdevel  = $(PKGFILES_DEVEL)

BUILD64 = 1 
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-merge:
	ginstall -d $(PKGROOT)$(BUILD_PREFIX)/lib
	cp $(DOWNLOADDIR)/$(LEGACYLIB)-$(GARCH)  $(PKGROOT)$(BUILD_PREFIX)/lib/$(LEGACYLIB)
	gln -s $(LEGACYLIB) $(PKGROOT)$(BUILD_PREFIX)/lib/libXrender.so.1
	gln -s $(LEGACYLIB) $(PKGROOT)$(BUILD_PREFIX)/lib/libXrender.so
	@$(MAKECOOKIE)
