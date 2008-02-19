GARNAME = SDL_net
GARVERSION = 1.2.5
CATEGORIES = lib

DESCRIPTION = A small cross-platform network library for SDL
define BLURB
This is a small sample cross-platform networking library, with a sample chat client and server application. The chat client uses the GUIlib GUI framework library.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_net/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsdlnet,)

CONFIGURE_ARGS = $(DIRPATHS)
TEST_SCRIPTS =

include ../category.mk

pre-configure:
	( cd $(WORKSRC) ; ./autogen.sh )
	@$(MAKECOOKIE)
