GARNAME = ncmpc
GARVERSION = 0.15
CATEGORIES = apps

GARCOMPILER = GNU
#OPTARCH_i386 = i686

DESCRIPTION = ncurses client for controlling Music Player Daemons (MPD)
define BLURB
ncmpc is a curses client for the Music Player Daemon (MPD). 
ncmpc connects to a MPD running on a machine on the local
network, and controls this with an interface inspired by
cplay. If ncmpc is used with lirc and irpty it can be used
to manage playlists and control MPD with a remote control.
endef

SF_PROJ = musicpd
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

TEST_TARGET =

include gar/category.mk
CPPFLAGS  += -I/opt/csw/include/ncurses
LDFLAGS   += -lsocket -lnsl -lintl
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-colors
CONFIGURE_ARGS += --enable-lyrics-screen

REQUIRED_PKGS  = CSWggettextrt
REQUIRED_PKGS += CSWglib2
REQUIRED_PKGS += CSWncurses
