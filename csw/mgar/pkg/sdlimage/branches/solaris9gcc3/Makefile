NAME = SDL_image
VERSION = 1.2.10
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = SDL image file loading library
define BLURB
SDL image library loads images as SDL surfaces, and supports the following formats: BMP, PNM, XPM, LBM, PCX, GIF, JPEG, PNG, TGA.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_image/release/
DISTFILES  = $(NAME)-$(GARCOMPILER = GCC3$(VERSION).+= CSWlibsdl-image1-2-0
CATALOGNAME_CSWlibsdl-image1-2-0 = libsdl_image1_2_0
PKGFILES_CSWlibsdl-image1-2-0 += $(call baseisadirs,$(libdir),libSDL_image-1\.2\.so\.0\.8\.4)
PKGFILES_CSWlibsdl-image1-2-0 += $(call baseisadirs,$(libdir),libSDL_image-1\.2\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsdl-image1-2-0 += $(DESCRIPTION), libSDL_image-1.2.so.0

# This creates the stub package that older packages depend on.
OBSOLETED_BY_CSWlibsdl-image1-2-0 += CSWsdlimage

# Split development files into separate package. 
PACKAGES += CSWsdlimage-dev
CATALOGNAME_CSWsdlimage-dev = sdlimage_dev
SPKG_DESC_CSWsdlimage-dev += $(DESCRIPTION), development files
PKGFILES_CSWsdlimage-dev += /opt/csw/lib/libSDL_image.so
PKGFILES_CSWsdlimage-dev += $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWsdlimage-dev += CSWlibsdl-image1-2-0
RUNTIME_DEP_PKGS_CSWlibsdl-image1-2-0 += CSWlibsdl1-2-0_RUNTIME_DEP_PKGS_CSWlibsdl-image1-2-0 += CSWgcc3core
RUNTIME_DEP_PKGS_CSWlibsdl-image1-2-0 += CSWlibgcc-s1

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS) --disable-static

TEST_SCRIPTS =

PACKAGING_PLATFORMS ?= solaris9-sparc solaris9-i386

include gar/category.mk
