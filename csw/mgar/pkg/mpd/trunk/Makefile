NAME = mpd
VERSION = 0.15.8
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = The Music Player Daemon
define BLURB
Music Player Daemon (MPD) allows remote access for playing music (MP3,
Ogg Vorbis, FLAC, AAC, Mod, and wave files) and managing playlists. MPD
is designed for integrating a computer into a stereo system that
provides control for music playback over a local network. It also makes
a great desktop music player, especially if you are a console junkie,
like frontend options, or restart X often.
endef

# TODO:
#
# There already are libraries to compile in AAC and mp4 support, but the
# configure script is not smart enough to pick up the header files.
#
# For example, faad.h test fails when faad.h is in /opt/csw/include.  This
# might require patching.

SF_PROJ = musicpd
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += cswmpd.init
DISTFILES += cswusergroup
DISTFILES += mpd.conf

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

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
CONFIGURE_ARGS += --enable-aac
CONFIGURE_ARGS += --bindir=/opt/csw/sbin
CONFIGURE_ARGS += --with-faad=/opt/csw
CONFIGURE_ARGS += --with-faad-libraries=/opt/csw/lib
CONFIGURE_ARGS += --with-faad-includes=/opt/csw/include

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

RUNTIME_DEP_PKGS_CSWmpd += CSWaudiofile
RUNTIME_DEP_PKGS_CSWmpd += CSWflac
RUNTIME_DEP_PKGS_CSWmpd += CSWggettextrt
RUNTIME_DEP_PKGS_CSWmpd += CSWglib2
RUNTIME_DEP_PKGS_CSWmpd += CSWlame
RUNTIME_DEP_PKGS_CSWmpd += CSWlibao
RUNTIME_DEP_PKGS_CSWmpd += CSWlibid3tag
RUNTIME_DEP_PKGS_CSWmpd += CSWlibmad
RUNTIME_DEP_PKGS_CSWmpd += CSWlibogg
RUNTIME_DEP_PKGS_CSWmpd += CSWsqlite3rt
RUNTIME_DEP_PKGS_CSWmpd += CSWvorbis
RUNTIME_DEP_PKGS_CSWmpd += CSWzlib

BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)

include gar/category.mk
