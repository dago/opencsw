GARNAME = vorbis-tools
GARVERSION = 1.0.1
CATEGORIES = utils

DESCRIPTION = Play, encode and manage Ogg Vorbis files.
define BLURB
    Ogg Vorbis is a high-quality lossy audio codec which is free of intellectual
    property restrictions (like those surrounding MP3). These are the tools that
    one needs to create and play Ogg Vorbis files on the commandline, as well as a
    simple commentor.
endef

UPSTREAM_MASTER_SITES = http://www.vorbis.com/files/
MASTER_SITES = http://www.vorbis.com/files/1.0.1/unix/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

DEPENDS = lib/libvorbis

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
