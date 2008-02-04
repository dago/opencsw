GARNAME = SDL
GARVERSION = 1.2.13
CATEGORIES = lib

DESCRIPTION = Simple DirectMedia Layer library
define BLURB
  Simple DirectMedia Layer is a cross-platform multimedia library
  designed to provide low level access to audio, keyboard, mouse,
  joystick, 3D hardware via OpenGL, and 2D video framebuffer. 
endef

MASTER_SITES = http://www.libsdl.org/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibsdl)

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
