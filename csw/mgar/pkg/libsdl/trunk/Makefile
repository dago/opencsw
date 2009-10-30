GARNAME = SDL
GARVERSION = 1.2.14
CATEGORIES = lib

DESCRIPTION = Simple DirectMedia Layer library
define BLURB
  Simple DirectMedia Layer is a cross-platform multimedia library
  designed to provide low level access to audio, keyboard, mouse,
  joystick, 3D hardware via OpenGL, and 2D video framebuffer. 
endef

MASTER_SITES = http://www.libsdl.org/release/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://www.libsdl.org/

PACKAGES = CSWlibsdl CSWlibsdldevel

REQUIRED_PKGS_CSWlibsdl = CSWiconv CSWlibx11 CSWlibxext
REQUIRED_PKGS_CSWlibsdldevel = CSWlibsdl

CATALOGNAME_CSWlibsdl      = libsdl
CATALOGNAME_CSWlibsdldevel = libsdl_devel

SPKG_DESC_CSWlibsdl       = Simple DirectMedia Layer library
SPKG_DESC_CSWlibsdldevel  = Simple DirectMedia Layer library development files

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# needs esound in 64 bit
# make sure it binds completely against new X11

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS) --disable-static
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

PKGFILES_CSWlibsdldevel = $(PKGFILES_DEVEL)

include gar/category.mk
