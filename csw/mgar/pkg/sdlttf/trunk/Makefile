GARNAME = SDL_ttf
GARVERSION = 2.0.9
CATEGORIES = lib

DESCRIPTION = TrueType font rendering library for SDL applications
define BLURB
  A sample library which allows you to use TrueType fonts in your SDL applications.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_ttf/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsdlttf,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

#PATCHFILES = SDL_ttf.c.diff

TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

#pre-configure:
#	( cd $(WORKSRC) ; ./autogen.sh )
#	@$(MAKECOOKIE)
