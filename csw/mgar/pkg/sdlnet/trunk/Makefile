NAME = SDL_net
VERSION = 1.2.8
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A small cross-platform network library for SDL
define BLURB
This is a small sample cross-platform networking library, with a sample chat client and server application. The chat client uses the GUIlib GUI framework library.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_net/release/
DISTFILES  = $(NAME)-$lnet, prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS) --disable-static
TEST_SCRIPTS =

include gar/category.mk

pre-configure:
	( cd $(WORKSRC) ; ./autogen.sh )