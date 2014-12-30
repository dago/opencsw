NAME = SDL_ttf
VERSION = 2.0.11
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = TrueType font rendering library for SDL applications
define BLURB
  A sample library which allows you to use TrueType fonts in your SDL applications.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_ttf/release/
DISTFILES  = $(NAME)-$iGARCOMPILER = GCC4$iles,CSWsdlttf,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:PACKAGES += CSWlibsdl-ttf2-0-0
CATALOGNAME_CSWlibsdl-ttf2-0-0 = libsdl_ttf2_0_0
PKGFILES_CSWlibsdl-ttf2-0-0 += $(call baseisadirs,$(libdir),libSDL_ttf-2\.0\.so\.0\.10\.1)
PKGFILES_CSWlibsdl-ttf2-0-0 += $(call baseisadirs,$(libdir),libSDL_ttf-2\.0\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibsdl-ttf2-0-0 += $(DESCRIPTION), libSDL_ttf-2.0.so.0
OBSOLETED_BY_CSWlibsdl-ttf2-0-0 = CSWsdlttf

# Split the development files into a separate package.
PACKAGES += CSWlibsdl-ttf-dev
CATALOGNAME_CSWlibsdl-ttf-dev = libsdl_ttf_dev
SPKG_DESC_CSWlibsdl-ttf-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibsdl-ttf-dev += /opt/csw/lib/libSDL_net.so
PKGFILES_CSWlibsdl-ttf-dev += $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWlibsdl-ttf2-0-0 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibsdl-ttf2-0-0 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibsdl-ttf2-0-0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibsdl-ttf-dev += CSWlibsdl-ttf2-0-0

EXTRA_LDFLAGS = -lm -L/opt/csw/lib -liconv

TEST_SCRIPTS =

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
