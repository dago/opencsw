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
RUNTIME_DEP_PKGS_CSWlibsdldevel = CSWlibsdl

CATALOGNAME_CSWlibsdl      = libsdl
CATALOGNAME_CSWlibsdldevel = libsdl_devel

SPKG_DESC_CSWlibsdl       = Simple DirectMedia Layer library
SPKG_DESC_CSWlibsdldevel  = Simple DirectMedia Layer library development files

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS) --disable-static

PKGFILES_CSWlibsdldevel = $(PKGFILES_DEVEL)

CHECKPKG_OVERRIDES_CSWlibsdl += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libSDL-1.2.so.0.11.3
CHECKPKG_OVERRIDES_CSWlibsdldevel += surplus-dependency|CSWlibsdl

include gar/category.mk
