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

PACKAGES += CSWlibsdl1-2-0
SPKG_DESC_CSWlibsdl1-2-0 = Simple DirectMedia Layer library, libsdl-1.2.so.0
PKGFILES_CSWlibsdl1-2-0 += $(call pkgfiles_lib,libSDL-1.2.so.0)
RUNTIME_DEP_PKGS_CSWlibsdl1-2-0 += CSWlibiconv2
OBSOLETED_BY_CSWlibsdl1-2-0 += CSWlibsdl

PACKAGES += CSWlibsdl-dev
SPKG_DESC_CSWlibsdl-dev  = Simple DirectMedia Layer library development files for libsdl-1.2.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS += CSWlibsdl1-2-0
OBSOLETED_BY_CSWlibsdl-dev += CSWlibsdldevel
CATALOGNAME_CSWlibsdldevel = libsdl_devel

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS) --disable-static

TEST_TARGET = test

include gar/category.mk
