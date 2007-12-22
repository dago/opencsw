GARNAME = mpd
GARVERSION = 0.13.0
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

MASTER_SITES = http://musicpd.org/uploads/files/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWmpd,prototype)
DISTFILES += cswmpd.xml svc-cswmpd cswmpd
DISTFILES += CSWmpd.csw_usrgrp_config

TEST_TARGET = check

include ../category.mk

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-ao
CONFIGURE_ARGS += --bindir=/opt/csw/sbin

$(DOWNLOADDIR)/cswmpd: files/svc-cswmpd
	@echo "Copying svc-cswmpd to cswmpd"
	@cp files/svc-cswmpd download/cswmpd

pre-fetch: $(DOWNLOADDIR)/cswmpd

post-install:
	ginstall -d $(DESTDIR)/opt/csw/var/mpd
	ginstall -d $(DESTDIR)/opt/csw/var/mpd/playlists
	ginstall -d $(DESTDIR)/opt/csw/var/mpd/music
	ginstall -D files/mpd.conf $(DESTDIR)/opt/csw/etc/mpd.conf

# pkg-get -i libao libid3tag libogg libflac libmikmod

# Special goal to generate a proper prototype file 
proto:
	../../bin/cswproto -s $(TIMESTAMP) -r $(DESTDIR) $(DESTDIR)/opt/csw/ | \
		sed "s,\(.*var.mpd.* 0755\).*,\1 mpd other," > files/CSWmpd.prototype

get-packages:
	@echo Run this: pkg-get -i libao id3lib
