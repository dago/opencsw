NAME = SDL_net
VERSION = 1.2.8
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = A small cross-platform network library for SDL
define BLURB
This is a small sample cross-platform networking library, with a sample chat client and server application. The chat client uses the GUIlib GUI framework library.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_net/release/
DISTFILES  = $(NAME)-$lPACKAGES += CSWlibsdl-net1-2-0
CATALOGNAME_CSWlibsdl-net1-2-0 = libsdl_net1_2_0
SPKG_DESC_CSWlibsdl-net1-2-0 += $(DESCRIPTION), libSDL_net-1.2.so.0
OBSOLETED_BY_CSWlibsdl-net1-2-0 = CSWsdlnet

# Split the development files into a separate package.
PACKAGES += CSWlibsdl-net1-2-0-dev
CATALOGNAME_CSWlibsdl-net1-2-0-dev = libsdl_net1_2_0_dev
SPKG_DESC_CSWlibsdl-net1-2-0-dev += $(DESCRIPTION), development files
PKGFILES_CSWlibsdl-net1-2-0-dev += /opt/csw/lib/libSDL_net.so
PKGFILES_CSWlibsdl-net1-2-0-dev += $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWlibsdl-net1-2-0 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibsdl-net1-2-0-dev += CSWlibsdl-net1-2-0$lnet, prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:BUILD64_LIBS_ONLY = 1?:EXTRA_LDFLAGS = -lsocket -lnsl?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS) --disable-static
TEST_SCRIPTS =

include gar/category.mk

pre-configure:
	( cd $(WORKSRC) ; ./autogen.sh )