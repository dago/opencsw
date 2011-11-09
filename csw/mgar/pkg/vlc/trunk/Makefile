# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = vlc
VERSION = 1.1.12
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = VideoLAN Client, the cross-platform media player and streaming server
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz

PATCHFILES += 0001-Disable-strange-check-this-may-be-dangerous.patch
PATCHFILES += 0002-Hack-around-missing-packed-pragma.patch
# PATCHFILES += 0003-Do-not-propagate-vlc-CFLAGS-to-linking.patch

# We need e.g. stdbool.h
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://www.videolan.org/vlc/

BUILD_DEP_PKGS += CSWliba52
BUILD_DEP_PKGS += CSWlibxcbdevel
BUILD_DEP_PKGS += CSWlibxaudevel
BUILD_DEP_PKGS += CSWlibxdmcpdevel
BUILD_DEP_PKGS += CSWlibx11devel

# This is for libxcb
#EXTRA_INC = /opt/csw/X11/include /usr/X11/include /usr/openwin/share/include
#EXTRA_LIB = /opt/csw/X11/lib
#EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# Sun Studio implements packed attributes differently and compilations bails out:
#   "include/vlc_codecs.h", line 36: #error: FIXME
GARCOMPILER = SOS12U2

# Taken from http://wiki.videolan.org/Solaris
EXTRA_CFLAGS = -D _XPG4_2 -D __SunOS -D __STDC_ISO_10646__ -D __EXTENSIONS__ -features=extensions -fast

# Solaris has MAXNAMELEN instead of NAME_MAX
EXTRA_CFLAGS += -DNAME_MAX=MAXNAMLEN

# For inet_pton
EXTRA_LINKER_FLAGS = -lsocket -lnsl

# For missing /opt/csw/lib/libgconf-2.la and /opt/csw/lib/libgconf-2.la
STRIP_LIBTOOL = 1

CONFIGURE_ARGS += $(DIRPATHS)

# Not there yet, part of ffmpeg
CONFIGURE_ARGS += --disable-avcodec

# No libpostproc yet
#CONFIGURE_ARGS += --disable-postproc

# No QT4 yet
CONFIGURE_ARGS += --disable-qt4 --disable-skins2

# Taken from http://wiki.videolan.org/Solaris
CONFIGURE_ARGS += --disable-libgcrypt --disable-remoteosd --disable-glx --disable-lua --disable-mad --disable-swscale --disable-postproc --disable-a52 --disable-fribidi --with-gnu-ld=no --disable-xcb


include gar/category.mk

