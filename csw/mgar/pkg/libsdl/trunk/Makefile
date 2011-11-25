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

VENDOR_URL = http://www.libsdl.org/

PACKAGES += CSWlibsdl
SPKG_DESC_CSWlibsdl = Simple DirectMedia Layer library
RUNTIME_DEP_PKGS_CSWlibsdl += CSWiconv

PACKAGES += CSWlibsdldevel
SPKG_DESC_CSWlibsdldevel  = Simple DirectMedia Layer library development files
PKGFILES_CSWlibsdldevel = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS += CSWlibsdl
CATALOGNAME_CSWlibsdldevel = libsdl_devel

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS) --disable-static

include gar/category.mk
