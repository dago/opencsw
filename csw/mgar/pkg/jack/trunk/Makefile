GARNAME = jack
GARVERSION = 1.9.3
CATEGORIES = lib

DESCRIPTION = A system for handling real-time, low latency audio and MIDI
define BLURB
  JACK is system for handling real-time, low latency audio (and MIDI). It runs
  on GNU/Linux, Solaris, FreeBSD, OS X and Windows (and can be ported to other
  POSIX-conformant platforms). It can connect a number of different applications
  to an audio device, as well as allowing them to share audio between themselves.
  Its clients can run in their own processes (ie. as normal applications), or can
  they can run within the JACK server (ie. as a "plugin"). JACK also has support
  for distributing audio processing across a network, both fast & reliable LANs
  as well as slower, less reliable WANs.
endef

MASTER_SITES = http://www.grame.fr/~letz/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/waf
CONFIGURE_ARGS = configure --prefix=$(prefix)

BUILD_SCRIPTS = $(WORKSRC)/waf
BUILD_ARGS = build

INSTALL_SCRIPTS = $(WORKSRC)/waf
INSTALL_ARGS = install --destdir=$(DESTDIR)

include gar/category.mk
