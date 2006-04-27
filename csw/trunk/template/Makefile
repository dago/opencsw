GARNAME = SDL
GARVERSION = 1.2.9
CATEGORIES = lib

DESCRIPTION = Simple DirectMedia Layer library
define BLURB
   Simple DirectMedia Layer is a cross-platform multimedia library designed to provide low level access to audio, keyboard, mouse, joystick, 3D hardware via OpenGL, and 2D video framebuffer. It is used by MPEG playback software, emulators, and many popular games, including the award winning Linux port of "Civilization: Call To Power."
endef

MASTER_SITES = http://www.libsdl.org/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibsdl,)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
