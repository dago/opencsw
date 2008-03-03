GARNAME = ncmpc
GARVERSION = 0.11.1
CATEGORIES = apps

GARCOMPILER = GNU
OPTARCH_i386 = i686

DESCRIPTION = ncurses client for controlling Music Player Daemons (MPD)
define BLURB
ncmpc is a curses client for the Music Player Daemon (MPD). 
ncmpc connects to a MPD running on a machine on the local
network, and controls this with an interface inspired by
cplay. If ncmpc is used with lirc and irpty it can be used
to manage playlists and control MPD with a remote control.
endef

MASTER_SITES = http://hem.bredband.net/kaw/ncmpc/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWncmpc,prototype)

TEST_TARGET =

include gar/category.mk
CPPFLAGS  += -I/opt/csw/include/ncurses
LDFLAGS   += -lsocket -lnsl -lintl
CONFIGURE_ARGS = $(DIRPATHS)
