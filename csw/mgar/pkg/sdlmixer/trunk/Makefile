NAME = SDL_mixer
VERSION = 1.2.11
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Multi-channel audio mixer library
define BLURB
SDL mixer supports any number of simultaneously playing channels of 16 bit stereo audio, plus a single channel of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis, and SMPEG MP3 libraries.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_mixer/release/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES = CSWsdlmixer
RUNTIME_DEP_PKGS = CSWlibsdl
EXTRA_LDFLAGS = -lm

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = --prefix=$(prefix) --disable-static
TEST_SCRIPTS =

include gar/category.mk
