# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
# It builds fine. 
# The Linker fix patch is from http://blogs.everycity.co.uk/alasdair/2009/05/ffmpeg-64bit-x86_64-amd64-on-solaris-10/
# This also mentions that ffmpeg build static is way faster then shared. So this would need two builds
# one static for static ffmpeg and one shared to get the shared libs. 
# Another thing is to see if it can be build with suncc see http://ftp.jaist.ac.jp/pub/pkgsrc/current/pkgsrc/multimedia/ffmpeg/Makefile.common

NAME = ffmpeg
VERSION = 0.8.6
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Very fast video and audio converter (includes libavcodec)
define BLURB
  FFmpeg is a complete, cross-platform solution to record, convert and stream
  audio and video. It includes libavcodec - the leading audio/video codec library.
endef

MASTER_SITES = http://ffmpeg.org/releases/
DISTFILES  = $(DISTNAME).tar.bz2

PATCHFILES += 0001-fix-version.sh.patch
PATCHFILES += 0002-change-linker-flags.patch
PATCHFILES += 0003-fix-testsuite-shells.patch

LICENSE = COPYING.GPLv3

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS += CSWlibtheora-dev
BUILD_DEP_PKGS += CSWlibvorbis-dev

PACKAGES += CSWlibavcodec53
SPKG_DESC_CSWlibavcodec53 = FFMPEG library libavcodec.so.53
PKGFILES_CSWlibavcodec53 += $(call pkgfiles_lib,libavcodec.so.53)
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibsdl
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibavcodec53 += CSWlibspeex1

PACKAGES += CSWlibavdevice53
SPKG_DESC_CSWlibavdevice53 = FFMPEG library libavdevice.so.53
PKGFILES_CSWlibavdevice53 += $(call pkgfiles_lib,libavdevice.so.53)
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibavformat53
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibsdl
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibavcodec53
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibavdevice53 += CSWlibspeex1

PACKAGES += CSWlibavfilter2
SPKG_DESC_CSWlibavfilter2 = FFMPEG library libavfilter.so.2
PKGFILES_CSWlibavfilter2 += $(call pkgfiles_lib,libavfilter.so.2)
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibavformat53
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibswscale2
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibsdl
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibavcodec53
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibtheoraenc1

PACKAGES += CSWlibavformat53
SPKG_DESC_CSWlibavformat53 = FFMPEG library libavformat.so.53
PKGFILES_CSWlibavformat53 += $(call pkgfiles_lib,libavformat.so.53)
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibsdl
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibavcodec53
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibavformat53 += CSWlibspeex1

PACKAGES += CSWlibavutil51
SPKG_DESC_CSWlibavutil51 = FFMPEG library libavutil.so.51
PKGFILES_CSWlibavutil51 += $(call pkgfiles_lib,libavutil.so.51)
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibsdl
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibtheoraenc1

PACKAGES += CSWlibpostproc51
SPKG_DESC_CSWlibpostproc51 = FFMPEG library libpostproc.so.51
PKGFILES_CSWlibpostproc51 += $(call pkgfiles_lib,libpostproc.so.51)
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibsdl
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibpostproc51 += CSWlibspeex1

PACKAGES += CSWlibswscale2
SPKG_DESC_CSWlibswscale2 = FFMPEG library libswscale.so.2
PKGFILES_CSWlibswscale2 += $(call pkgfiles_lib,libswscale.so.2)
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibsdl
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWftype2
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibspeex1

PACKAGES += CSWffmpeg-dev
SPKG_DESC_CSWffmpeg-dev = Development files for several FFMPEG shared libraries
PKGFILES_CSWffmpeg-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavcodec53
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavdevice53
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavfilter2
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavformat53
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibpostproc51
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibswscale2

PACKAGES += CSWffmpeg
SPKG_DESC_CSWffmpeg = Very fast video and audio converter
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavformat53
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibswscale2
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibsdl
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibz1
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibogg0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavcodec53
RUNTIME_DEP_PKGS_CSWffmpeg += CSWftype2
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavdevice53
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavfilter2
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibpostproc51

# These are all examples
CHECKPKG_OVERRIDES_CSWffmpeg += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/ffmpeg.1
CHECKPKG_OVERRIDES_CSWffmpeg += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/ffplay.1
CHECKPKG_OVERRIDES_CSWffmpeg += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/ffmpeg.1
CHECKPKG_OVERRIDES_CSWffmpeg += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/ffplay.1

#EXTRA_MODULATORS = SHARED
#MODULATIONS_SHARED = yes no

BUILD64_LIBS_ONLY = 1

GARCOMPILER = GNU

NODIRPATHS += --exec_prefix
NODIRPATHS += --sbindir
NODIRPATHS += --libexecdir
NODIRPATHS += --sysconfdir
NODIRPATHS += --sharedstatedir

#EXTRA_CFLAGS-64 += -xcode=pic32
EXTRA_CFLAGS-64 += -fPIC
EXTRA_CFLAGS += $(EXTRA_CFLAGS-$(MEMORYMODEL))

EXTRA_CXXFLAGS-64 += -fPIC
EXTRA_CXXFLAGS += $(EXTRA_CXXFLAGS-$(MEMORYMODEL))

CONFIGURE_ARGS += --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --datadir=$(datadir)
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURE_ARGS += --shlibdir=$(libdir)
CONFIGURE_ARGS += --incdir=$(includedir)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGURE_ARGS += --disable-debug
CONFIGURE_ARGS += --enable-gpl
CONFIGURE_ARGS += --enable-version3
CONFIGURE_ARGS += --enable-runtime-cpudetect

# All ASM code is broke no clue if it yasm that breaks it or solaris in gerneral. As it is disabled in pkgsrc too probably a global problem.
CONFIGURE_ARGS += --disable-asm

# Needs two builds one shared one static
#CONFIGURE_ARGS-SHARED-yes += --enable-shared
#CONFIGURE_ARGS += $(CONFIGURE_ARGS-SHARED-$(SHARED))

CONFIGURE_ARGS += --enable-shared

#externel libs:
# libfaac is not free
#CONFIGURE_ARGS += --enable-libfaac
CONFIGURE_ARGS += --enable-libfreetype
CONFIGURE_ARGS += --enable-libmp3lame
CONFIGURE_ARGS += --enable-libspeex
# No libtheora
CONFIGURE_ARGS += --enable-libtheora
CONFIGURE_ARGS += --enable-libvorbis

# Tests only work with static build
#SKIPTEST-SHARED-yes = 1
#SKIPTEST ?= $(SKIPTEST-SHARED-$(SHARED))

SKIPTEST ?= 1

include gar/category.mk

# For 'grep -q'
PATH := /opt/csw/gnu:$(PATH)
