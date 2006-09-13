GARNAME = xmms
GARVERSION = 1.2.10
CATEGORIES = gnome

DESCRIPTION = The X MultiMedia System.
define BLURB
    XMMS is a multimedia player based on the look of WinAmp. XMMS plays MPEG layer
    1/2/3, Ogg Vorbis, WAV, all formats supported by libmikmod, and CD audio. XMMS
    has a plugin system for Input / Output / Effects / Visualization, and through
    plugins it can play a lot more sound and video formats.
endef

MASTER_SITES = http://www.xmms.org/files/1.2.x/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

DEPENDS = lib/libvorbis

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-glib-prefix=/usr/sfw
CONFIGURE_ARGS += --with-gtk-prefix=/usr/sfw
CONFIGURE_ARGS += --with-ogg=$(prefix)
CONFIGURE_ARGS += --with-vorbis=$(prefix)

# No test suite
TEST_SCRIPTS =

include ../category.mk
