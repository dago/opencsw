GARNAME = SDL_image
GARVERSION = 1.2.4
CATEGORIES = lib

DESCRIPTION = SDL image file loading library
define BLURB
SDL image library loads images as SDL surfaces, and supports the following formats: BMP, PNM, XPM, LBM, PCX, GIF, JPEG, PNG, TGA.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_image/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsdlimage,)

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =
include ../category.mk

