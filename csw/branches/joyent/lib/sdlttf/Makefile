GARNAME = SDL_ttf
GARVERSION = 2.0.6
CATEGORIES = lib

DESCRIPTION = TrueType font rendering library for SDL applications
define BLURB
  This is a sample library which allows you to use TrueType fonts in your SDL applications. It comes with an example program "showfont" which displays an example string for a given TrueType font file. 
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_ttf/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsdlttf,)

PATCHFILES = SDL_ttf.c.diff
ENABLE_TEST = 0
CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk

pre-configure:
	( cd $(WORKSRC) ; ./autogen.sh )
	@$(MAKECOOKIE)
