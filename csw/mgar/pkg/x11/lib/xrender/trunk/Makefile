GARNAME = libxrender
GARVERSION = 0.9.5
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

EXTRA_MODULATORS = X11
MODULATIONS_X11 = sunwx11 cswx11

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = libXrender-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibxrender CSWlibxrenderdevel
PACKAGES += CSWcxlibxrender CSWcxlibxrenderdevel

CATALOGNAME_CSWlibxrender      = libxrender
CATALOGNAME_CSWlibxrenderdevel = libxrender_devel
CATALOGNAME_CSWcxlibxrender      = cx_libxrender
CATALOGNAME_CSWcxlibxrenderdevel = cx_libxrender_devel

BUILD_DEP_PKGS = CSWx11renderproto CSWsunx11devel

RUNTIME_DEP_PKGS_CSWlibxrenderdevel = CSWlibxrender
RUNTIME_DEP_PKGS_CSWcxlibxrender += CSWlibx11

SPKG_DESC_CSWlibxrender = $(DESCRIPTION)
SPKG_DESC_CSWlibxrenderdevel  = $(DESCRIPTION) Development Package
SPKG_DESC_CSWcxlibxrender = $(DESCRIPTION) (bound against OpenCSW X11)
SPKG_DESC_CSWcxlibxrenderdevel  = $(DESCRIPTION) Development Package (bound against OpenCSW X11)

ARCHALL_CSWcxlibxrenderdevel = 1
ARCHALL_CSWlibxrenderdevel = 1

PKGFILES_CSWlibxrenderdevel = /opt/csw/lib/.*\.pc /opt/csw/.*\.h
PKGFILES_CSWlibxrender = /opt/csw/lib/.*so.* /opt/csw/share/doc/libxender/.*
PKGFILES_CSWcxlibxrenderdevel = /opt/csw/X11/.*\.pc /opt/csw/X11.*\.h
PKGFILES_CSWcxlibxrender = /opt/csw/X11/lib/.*so.* /opt/csw/share/doc/cx_libxrender/.*

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

PKGFILES_CSWlibxrenderdevel  = $(PKGFILES_DEVEL)

CHECKPKG_OVERRIDES_CSWlibxrenderdevel += surplus-dependency|CSWlibxrender
CHECKPKG_OVERRIDES_CSWlibxrender += linked-against-discouraged-library|libXrender.so.1.3.0|libX11.so.4
CHECKPKG_OVERRIDES_CSWlibxrender += linked-against-discouraged-library|libXrender.so.1.3.0|libX11.so.4

CHECKPKG_OVERRIDES_CSWcxlibxrenderdevel += archall-with-arch-paths|/opt/csw/X11/lib/amd64
CHECKPKG_OVERRIDES_CSWcxlibxrenderdevel += archall-with-arch-paths|/opt/csw/X11/lib/amd64/pkgconfig
CHECKPKG_OVERRIDES_CSWcxlibxrenderdevel += archall-with-arch-paths|/opt/csw/X11/lib/amd64/pkgconfig/xrender.pc
CHECKPKG_OVERRIDES_CSWlibxrenderdevel += archall-with-arch-paths|/opt/csw/lib/amd64/pkgconfig
CHECKPKG_OVERRIDES_CSWlibxrenderdevel += archall-with-arch-paths|/opt/csw/lib/amd64/pkgconfig/xrender.pc

include gar/category.mk
