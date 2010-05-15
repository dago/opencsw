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
PACKAGES += CSWcxlibxrender CSWcxlibxrenderdevel

CATALOGNAME_CSWlibxrender      = libxrender
CATALOGNAME_CSWlibxrenderdevel = libxrender_devel
CATALOGNAME_CSWcxlibxrender      = cx_libxrender
CATALOGNAME_CSWcxlibxrenderdevel = cx_libxrender_devel

BUILD_DEP_PKGS = CSWx11renderproto CSWsunx11devel
RUNTIME_DEP_PKGS_CSWlibxrenderdevel = CSWlibxrender
RUNTIME_DEP_PKGS_CSWlibxrender = CSWx11common CSWlibx11

SPKG_DESC_CSWlibxrender = $(DESCRIPTION)
SPKG_DESC_CSWlibxrenderdevel  = $(DESCRIPTION) Development Package
SPKG_DESC_CSWcxlibxrender = $(DESCRIPTION) (bound against OpenCSW X11)
SPKG_DESC_CSWcxlibxrenderdevel  = $(DESCRIPTION) Development Package (bound against OpenCSW X11)

PKGFILES_CSWlibxrenderdevel  = $(PKGFILES_DEVEL)

MERGE_SCRIPTS_isa-default-x11-sunwx11 = copy-all
MERGE_SCRIPTS_isa-default64-x11-sunwx11 = copy-relocated-only
MERGE_DIRS_isa-default64-x11-sunwx11 = $(libdir)
MERGE_SCRIPTS_isa-default-x11-cswx11 = copy-only
MERGE_DIRS_isa-default-x11-cswx11 = $(libdir) $(includedir)
MERGE_SCRIPTS_isa-default64-x11-cswx11 = copy-relocated-only
MERGE_DIRS_isa-default64-x11-cswx11 = $(libdir)

BUILD64 = 1 
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

STRIP_LIBTOOL = 1

include gar/category.mk

# this needs to be after the include as it's not a ?= in the x11
# category...
prefix_cswx11 = $(BUILD_PREFIX)/X11
prefix = $(or $(prefix_$(X11)),$(BUILD_PREFIX))

post-merge:
	ginstall -d $(PKGROOT)$(BUILD_PREFIX)/lib
	cp $(DOWNLOADDIR)/$(LEGACYLIB)-$(GARCH)  $(PKGROOT)$(BUILD_PREFIX)/lib/$(LEGACYLIB)
	gln -s $(LEGACYLIB) $(PKGROOT)$(BUILD_PREFIX)/lib/libXrender.so.1
	gln -s $(LEGACYLIB) $(PKGROOT)$(BUILD_PREFIX)/lib/libXrender.so
	@$(MAKECOOKIE)
