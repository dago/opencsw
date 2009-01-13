GARNAME = libxrender
GARVERSION = 0.9.4
CATEGORIES = x11

DESCRIPTION = X Render extension library
define BLURB
The X Rendering Extension (Render) introduces digital image composition as the foundation of a new rendering model within the X Window System. Rendering geometric figures is accomplished by client-side tesselation into either triangles or trapezoids.
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = libXrender-$(GARVERSION).tar.gz
PKGDIST = libXrender-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = libXrender-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWlibxrender = $(DESCRIPTION)
SPKG_DESC_CSWrenderdev  = $(DESCRIPTION) development package

DISTFILES    += $(call admfiles,CSWlibxrender, )
DISTFILES    += $(call admfiles,CSWrenderdev, )

PKGFILES_CSWrenderdev  = $(PKGFILES_DEVEL)
PKGFILES_CSWrenderdev += $(prefix)/X11/include/.*
PKGFILES_CSWrenderdev += $(prefix)/X11/lib/.*\.a
PKGFILES_CSWrenderdev += $(prefix)/X11/lib/pkgconfig/.*

REQUIRED_PKGS_CSWrenderdev  = CSWlibxrender
REQUIRED_PKGS_CSWlibxrender = CSWlibx11

post-extract:
	( cd  $(WORKROOTDIR)/build-$(firstword $(MODULATIONS)) ; \
		mv libXrender-$(GARVERSION) $(DISTNAME) )
	@$(MAKECOOKIE)

include gar/category.mk


