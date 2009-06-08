GARNAME = libxrender
GARVERSION = 0.9.4
CATEGORIES = x11

DESCRIPTION = X Render extension library
define BLURB
  The X Rendering Extension (Render) introduces digital image composition as
  the foundation of a new rendering model within the X Window System.
  Rendering geometric figures is accomplished by client-side tesselation
  into either triangles or trapezoids.
endef

MASTER_SITES = http://xorg.freedesktop.org/releases/individual/lib/
DISTNAME = libXrender-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = libXrender-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibxrender CSWrenderdev

PREREQUISITE_PKGS = CSWrenderproto
REQUIRED_PKGS_CSWrenderdev = CSWlibxrender
REQUIRED_PKGS_CSWlibxrender = CSWx11common CSWlibx11

SPKG_DESC_CSWlibxrender = $(DESCRIPTION)
SPKG_DESC_CSWrenderdev  = $(DESCRIPTION) development package

PKGFILES_CSWrenderdev  = $(PKGFILES_DEVEL)

BUILD64 = 1 
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-merge:
	ginstall -d $(PKGROOT)$(BUILD_PREFIX)/lib
	gln -s ../X11/lib/libXrender.so.1 $(PKGROOT)$(BUILD_PREFIX)/lib/libXrender.so.1
	@$(MAKECOOKIE)
