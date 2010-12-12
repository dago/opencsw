NAME = libxrender
VERSION = 0.9.5
CATEGORIES = x11

DESCRIPTION = X Render Extension Library
define BLURB
  The X Rendering Extension (Render) introduces digital image composition as
  the foundation of a new rendering model within the X Window System.
  Rendering geometric figures is accomplished by client-side tesselation
  into either triangles or trapezoids.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTNAME = libXrender-$(VERSION)
DISTFILES = $(DISTNAME).tar.gz

EXTRA_MODULATORS = X11
MODULATIONS_X11 = sunwx11 cswx11

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = libXrender-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibxrender CSWcxlibxrender

CATALOGNAME_CSWlibxrender   = libxrender
CATALOGNAME_CSWcxlibxrender = cx_libxrender

BUILD_DEP_PKGS = CSWx11renderproto CSWsunx11devel

RUNTIME_DEP_PKGS_CSWlibxrenderdevel = CSWlibxrender
RUNTIME_DEP_PKGS_CSWcxlibxrender += CSWlibx11

SPKG_DESC_CSWlibxrender = $(DESCRIPTION)
SPKG_DESC_CSWcxlibxrender = $(DESCRIPTION) (bound against OpenCSW X11)

PKGFILES_CSWlibxrender = /opt/csw/lib/.* /opt/csw/include/.*
PKGFILES_CSWcxlibxrender = /opt/csw/X11/.* /opt/csw/share/doc/cx.*

prefix_cswx11 = $(BUILD_PREFIX)/X11
prefix = $(or $(prefix_$(X11)),$(BUILD_PREFIX))

STRIP_LIBTOOL = 1

BUILD64 = 1 
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

MERGE_SCRIPTS_isa-default-x11-sunwx11 = copy-all
MERGE_SCRIPTS_isa-default64-x11-sunwx11 = copy-relocated-only
MERGE_DIRS_isa-default64-x11-sunwx11 = $(libdir)
MERGE_SCRIPTS_isa-default-x11-cswx11 = copy-only
MERGE_DIRS_isa-default-x11-cswx11 = $(libdir) $(includedir)
MERGE_SCRIPTS_isa-default64-x11-cswx11 = copy-relocated-only
MERGE_DIRS_isa-default64-x11-cswx11 = $(libdir)

CHECKPKG_OVERRIDES_CSWlibxrenderdevel += surplus-dependency|CSWlibxrender
CHECKPKG_OVERRIDES_CSWlibxrender += linked-against-discouraged-library|libXrender.so.1.3.0|libX11.so.4
CHECKPKG_OVERRIDES_CSWlibxrender += linked-against-discouraged-library|libXrender.so.1.3.0|libX11.so.4

include gar/category.mk

# if we're doing the cx version (/opt/csw/X11), then kill the devel bits that
# are shipped with x11_xrenderproto
post-install-modulated:
	@( cd $(DESTDIR)/opt/csw/; \
		if [ -d X11/include ]; then \
			rm -rf X11/include; \
			find . -name pkgconfig -type d | xargs rm -rf; \
		fi )
	@$(MAKECOOKIE)
