GARNAME = libXft
GARVERSION = 2.1.13
CATEGORIES = x11

DESCRIPTION = X11 authorisation library
define BLURB
  Xft provides a client-side font API for X applications, making the
  FreeType font rasterizer available to X clients. Fontconfig is used
  for font specification resolution. Where available, the RENDER
  extension handles glyph drawing; otherwise, the core X protocol is used.
endef

MASTER_SITES = $(X11_LIB_MASTER_SITE)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# Legacy libraries
# The idea is to have the legacy libs in /opt/csw/lib to guarantee the existing
# apps will continue to work. The new lib in /opt/csw/X11/lib relies on the
# OpenCSW-specific X11 libs, whereas the existing one in /opt/csw/lib links
# against the Sun X11.
LEGACYLIB = libXft.so.2.1.2
DISTFILES += $(LEGACYLIB)-i386
DISTFILES += $(LEGACYLIB)-sparc

PACKAGES = CSWlibxft2 CSWlibxft2devel

CATALOGNAME_CSWlibxft2 = libxft2
CATALOGNAME_CSWlibxft2devel = libxft2_devel

REQUIRED_PKGS_CSWlibxft2 = CSWzlib CSWfconfig CSWftype2 CSWlibx11 CSWlibxrender
REQUIRED_PKGS_CSWlibxft2devel = CSWlibxft2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibxft2devel = $(PKGFILES_DEVEL)

include gar/category.mk

post-merge:
	ginstall -d $(PKGROOT)$(BUILD_PREFIX)/lib
	cp $(DOWNLOADDIR)/$(LEGACYLIB)-$(GARCH)  $(PKGROOT)$(BUILD_PREFIX)/lib/$(LEGACYLIB)
	gln -s $(LEGACYLIB) $(PKGROOT)$(BUILD_PREFIX)/lib/libXft.so.2
	gln -s $(LEGACYLIB) $(PKGROOT)$(BUILD_PREFIX)/lib/libXft.so
	@$(MAKECOOKIE)
