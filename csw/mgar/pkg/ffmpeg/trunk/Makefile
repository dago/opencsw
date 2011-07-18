# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = ffmpeg
VERSION = 0.8
CATEGORIES = lib

DESCRIPTION = Very fast video and audio converter (includes libavcodec)
define BLURB
  FFmpeg is a complete, cross-platform solution to record, convert and stream
  audio and video. It includes libavcodec - the leading audio/video codec library.
endef

MASTER_SITES = http://ffmpeg.org/releases/
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
PATCHFILES = 0001-fix-version.sh.patch
PATCHFILES += 0002-change-linker-flags.patch
PATCHFILES += 0003-fix-testsuite-shells.patch

BUILD64 = 1

NODIRPATHS += --exec_prefix
NODIRPATHS += --sbindir
NODIRPATHS += --libexecdir
NODIRPATHS += --sysconfdir
NODIRPATHS += --sharedstatedir

CONFIGURE_ARGS += --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --datadir=$(datadir)
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURE_ARGS += --shlibdir=$(libdir)
CONFIGURE_ARGS += --incdir=$(includedir)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --enable-gpl
CONFIGURE_ARGS += --enable-shared
#CONFIGURE_ARGS += --disable-static

GARCOMPILER = GNU

include gar/category.mk

# For 'grep -q'
PATH := /opt/csw/gnu:$(PATH)
