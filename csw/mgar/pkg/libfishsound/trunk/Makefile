GARNAME = libfishsound
GARVERSION = 0.9.2
CATEGORIES = lib

DESCRIPTION = Decoding and encoding audio data using the Xiph.org codecs
define BLURB
  libfishsound provides a simple programming interface for decoding and encoding
  audio data using the Xiph.org codecs (FLAC, Speex and Vorbis).
endef

MASTER_SITES =  http://downloads.xiph.org/releases/libfishsound/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.xiph.org/fishsound/

REQUIRED_PKGS = CSWflac CSWlibogg CSWspeex CSWvorbis
PREREQUISITE_PKGS = $(REQUIRED_PKGS)

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

BUILD_ARGS = AM_CFLAGS=

TEST_TARGET = check

include gar/category.mk

# UINTPTR_MAX is defined empty in Solaris, which breaks a constraint check
post-configure-modulated:
	perl -pi -e 's,(.*HAVE_UINTPTR_T.*),/* \1 */,' $(WORKSRC)/config.h
	@$(MAKECOOKIE)
