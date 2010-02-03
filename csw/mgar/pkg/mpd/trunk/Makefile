GARNAME = mpd
GARVERSION = 0.14.2
CATEGORIES = server

DESCRIPTION = The Music Player Daemon
define BLURB
Music Player Daemon (MPD) allows remote access for playing music (MP3,
Ogg Vorbis, FLAC, AAC, Mod, and wave files) and managing playlists. MPD
is designed for integrating a computer into a stereo system that
provides control for music playback over a local network. It also makes
a great desktop music player, especially if you are a console junkie,
like frontend options, or restart X often.
endef

# A problem:
#
# The build, ported from gar v1 to v2 by Maciej Bliziński is pretty much done,
# but unfortunately, mpd segfaults when testing. More debugging is needed; this
# build is being submitted to separate segfault fixes from v1-v2 port.

SF_PROJ = musicpd
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += cswmpd.init
DISTFILES += cswusergroup
DISTFILES += mpd.conf

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_TARGET = check

SPKG_CLASSES = none cswcpsampleconf cswusergroup ugfiles cswinitsmf
PROTOTYPE_FILTER  = awk ' \
    $$$$3 ~ /\/init.d\/cswmpd$$$$/ { $$$$2 = "cswinitsmf" } \
    $$$$3 ~ /\/mpd\.conf\.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
    $$$$3 ~ /\/CSWmpd\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } \
    $$$$3 ~ /\/var\/opt\/csw\/mpd/ { $$$$5 = "mpd" } \
    $$$$3 ~ /\/var\/opt\/csw\/mpd/ { $$$$2 = "ugfiles" } \
    $$$$3 ~ /\/sbin\/mpd$$$$/ { $$$$4 = "0755" } \
    { print }'
GARCOMPILER = SOS12

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ao
CONFIGURE_ARGS += --bindir=/opt/csw/sbin

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

post-install-modulated:
	ginstall -d $(DESTDIR)/var/opt/csw/mpd
	ginstall -d $(DESTDIR)/var/opt/csw/mpd/playlists
	ginstall -d $(DESTDIR)/var/opt/csw/mpd/music
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 0644 $(FILEDIR)/mpd.conf $(DESTDIR)/etc/opt/csw/mpd.conf.CSW
	ginstall $(FILEDIR)/cswmpd.init $(DESTDIR)/etc/opt/csw/init.d/cswmpd
	ginstall -D $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWmpd/cswusergroup

RUNTIME_DEP_PKGS  = CSWaudiofile
RUNTIME_DEP_PKGS += CSWcswclassutils
RUNTIME_DEP_PKGS += CSWflac
RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWlibao
RUNTIME_DEP_PKGS += CSWlibid3tag
RUNTIME_DEP_PKGS += CSWlibmad
RUNTIME_DEP_PKGS += CSWzlib

BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)

include gar/category.mk
