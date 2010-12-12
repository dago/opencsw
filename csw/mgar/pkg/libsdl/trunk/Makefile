NAME = SDL
VERSION = 1.2.14
CATEGORIES = lib

DESCRIPTION = Simple DirectMedia Layer library
define BLURB
  Simple DirectMedia Layer is a cross-platform multimedia library
  designed to provide low level access to audio, keyboard, mouse,
  joystick, 3D hardware via OpenGL, and 2D video framebuffer. 
endef

MASTER_SITES = http://www.libsdl.org/release/
DISTFILES = $(NAME)-$(VERSION).tar.gz
PATCHFILES = 0001-Fix-nasm-options.patch

SPKG_SOURCEURL = http://www.libsdl.org/

PACKAGES = CSWlibsdl CSWlibsdldevel

RUNTIME_DEP_PKGS_CSWlibsdl = CSWiconv

CATALOGNAME_CSWlibsdl      = libsdl
CATALOGNAME_CSWlibsdldevel = libsdl_devel

SPKG_DESC_CSWlibsdl       = Simple DirectMedia Layer library
SPKG_DESC_CSWlibsdldevel  = Simple DirectMedia Layer library development files

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# needs esound in 64 bit

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS) --disable-static

PKGFILES_CSWlibsdldevel = $(PKGFILES_DEVEL)

include gar/category.mk
