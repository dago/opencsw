NAME = SDL_image
VERSION = 1.2.12
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = SDL image file loading library
define BLURB
SDL image library loads images as SDL surfaces, and supports the following formats: BMP, PNM, XPM, LBM, PCX, GIF, JPEG, PNG, TGA.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_image/release/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWsdlimage
RUNTIME_DEP_PKGS = CSWlibsdl

UFILES_REGEX = $(NAME)-(\d+(?:BUILD64_LIBS_ONLY = 1?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS) --disable-static
TEST_SCRIPTS =
include