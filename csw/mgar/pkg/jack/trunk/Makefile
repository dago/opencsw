NAME = jack
VERSION = 1.9.8
CATEGORIES = lib
GARTYPE = v2

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
DISTFILES += $(DISTNAME).tgz

# libcelt is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

GARCOMPILER = GCC4

BUILD64_LIBS_ONLY = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/$(DISTNAME)/waf
CONFIGURE_ARGS = configure --prefix=$(prefix)

BUILD_SCRIPTS = $(WORKSRC)/$(DISTNAME)/waf
# BUILD_ARGS = build

TEST_SCRIPTS = $(WORKSRC)/$(DISTNAME)/waf

INSTALL_SCRIPTS = $(WORKSRC)/$(DISTNAME)/waf
INSTALL_ARGS = --destdir=$(DESTDIR)

include gar/category.mk
