GARNAME = SDL_image
GARVERSION = 1.2.8
CATEGORIES = lib

DESCRIPTION = SDL image file loading library
define BLURB
SDL image library loads images as SDL surfaces, and supports the following formats: BMP, PNM, XPM, LBM, PCX, GIF, JPEG, PNG, TGA.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_image/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWsdlimage
REQUIRED_PKGS = CSWlibsdl

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS) --disable-static
TEST_SCRIPTS =
include gar/category.mk
