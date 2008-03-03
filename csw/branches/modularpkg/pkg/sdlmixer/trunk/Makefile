GARNAME = SDL_mixer
GARVERSION = 1.2.6
CATEGORIES = lib

DESCRIPTION = multi-channel audio mixer library
define BLURB
SDL mixer supports any number of simultaneously playing channels of 16 bit stereo audio, plus a single channel of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis, and SMPEG MP3 libraries.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_mixer/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsdlmixer, depend)

CONFIGURE_ARGS = --prefix=$(prefix) LDFLAGS=-lsunmath
TEST_SCRIPTS =

include gar/category.mk
