NAME = SDL_mixer
VERSION = 1.2.12
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Multi-channel audio mixer library
define BLURB
SDL mixer supports any number of simultaneously playing channels of 16 bit stereo audio, plus a single channel of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis, and SMPEG MP3 libraries.
endef

MASTER_SITES = http://www.libsdl.org/projects/SDL_mixer/release/
DISTFILES  = $(NAME)-$(VERSION).+= CSWlibsdl-mixer1-2-0
CATALOGNAME_CSWlibsdl-mixer1-2-0 = libsdl_mixer1_2_0
OBSOLETED_BY_CSWlibsdl-mixer1-2-0 = CSWsdlmixer

SPKG_DESC_CSWlibsdl-mixer1-2-0 += $(DESCRIPTION), libSDL_mixer-1.2.so.0
RUNTIME_DEP_PKGS_CSWlibsdl-mixer1-2-0 += CSWlibsdl1-2-0

EXTRA_LDFLAGS = -lm

REINPLACE_USRLOCAL += timidity/config.h
REINPLACE_USRSHARE += timidity/config.hTRA_LDFLAGS = -lm

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = --prefix=$(prefix) --disable-staticCHECKPKG_OVERRIDES_CSWlibsdl-mixer1-2-0 += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libSDL_mixer.so

include gar/category.mk
