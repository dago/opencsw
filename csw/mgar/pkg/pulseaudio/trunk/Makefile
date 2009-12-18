GARNAME = pulseaudio
GARVERSION = 0.9.21
CATEGORIES = lib

DESCRIPTION = PulseAudio is a sound server for POSIX systems
define BLURB
endef

MASTER_SITES = http://0pointer.de/lennart/projects/pulseaudio/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://pulseaudio.org/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
