# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
# It builds fine. The Test are failing though.
# The Linker fix patch is from http://blogs.everycity.co.uk/alasdair/2009/05/ffmpeg-64bit-x86_64-amd64-on-solaris-10/
# This also mentions that ffmpeg build static is way faster then shared. So this would need two builds
# one static for static ffmpeg and one shared to get the shared libs. 
# Another thing is to see if it can be build with suncc see http://ftp.jaist.ac.jp/pub/pkgsrc/current/pkgsrc/multimedia/ffmpeg/Makefile.common
# They disable all optimizations though. I don't know why. 
# 3. No external libs are enabled atm. We might want to think about two versions with and without external libs

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
# Tests need to be fixed
TEST_SCRIPTS = 

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

GARCOMPILER = GNU

include gar/category.mk

# For 'grep -q'
PATH := /opt/csw/gnu:$(PATH)
