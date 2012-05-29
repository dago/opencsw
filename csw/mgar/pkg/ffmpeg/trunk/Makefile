# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$
# It builds fine. 
# The Linker fix patch is from http://blogs.everycity.co.uk/alasdair/2009/05/ffmpeg-64bit-x86_64-amd64-on-solaris-10/
# This also mentions that ffmpeg build static is way faster then shared. So this would need two builds
# one static for static ffmpeg and one shared to get the shared libs. 
# Another thing is to see if it can be build with suncc see http://ftp.jaist.ac.jp/pub/pkgsrc/current/pkgsrc/multimedia/ffmpeg/Makefile.common

NAME = ffmpeg
VERSION = 0.11
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
PATCHFILES += 0003-change-linker-flags.patch
PATCHFILES += 0003-fix_a_few_shells.patch

LICENSE = COPYING.GPLv3

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS += CSWlibtheora-dev
BUILD_DEP_PKGS += CSWlibvorbis-dev
BUILD_DEP_PKGS += CSWlibx264-dev

PACKAGES += CSWlibavcodec54
SPKG_DESC_CSWlibavcodec54 = FFMPEG library libavcodec.so.54
PKGFILES_CSWlibavcodec54 += $(call pkgfiles_lib,libavcodec.so.54)
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibavfilter2
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibavcodec54 += CSWlibx264-125

PACKAGES += CSWlibavdevice54
SPKG_DESC_CSWlibavdevice54 = FFMPEG library libavdevice.so.54
PKGFILES_CSWlibavdevice54 += $(call pkgfiles_lib,libavdevice.so.54)
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibavformat54
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibavcodec54
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibavdevice54 += CSWlibx264-125

PACKAGES += CSWlibavfilter2
SPKG_DESC_CSWlibavfilter2 = FFMPEG library libavfilter.so.2
PKGFILES_CSWlibavfilter2 += $(call pkgfiles_lib,libavfilter.so.2)
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibavformat54
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibswscale2
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibavcodec54
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibswresample0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibx264-125
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibavresample0
RUNTIME_DEP_PKGS_CSWlibavfilter2 += CSWlibpostproc52

PACKAGES += CSWlibavformat54
SPKG_DESC_CSWlibavformat54 = FFMPEG library libavformat.so.54
PKGFILES_CSWlibavformat54 += $(call pkgfiles_lib,libavformat.so.54)
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibavcodec54
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibavformat54 += CSWlibx264-125

PACKAGES += CSWlibavutil51
SPKG_DESC_CSWlibavutil51 = FFMPEG library libavutil.so.51
PKGFILES_CSWlibavutil51 += $(call pkgfiles_lib,libavutil.so.51)
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibavutil51 += CSWlibx264-125

PACKAGES += CSWlibpostproc52
SPKG_DESC_CSWlibpostproc52 = FFMPEG library libpostproc.so.52
PKGFILES_CSWlibpostproc52 += $(call pkgfiles_lib,libpostproc.so.52)
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibpostproc52 += CSWlibx264-125

PACKAGES += CSWlibswscale2
SPKG_DESC_CSWlibswscale2 = FFMPEG library libswscale.so.2
PKGFILES_CSWlibswscale2 += $(call pkgfiles_lib,libswscale.so.2)
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibswscale2 += CSWlibx264-125

PACKAGES += CSWlibswresample0
SPKG_DESC_CSWlibswresample0 = FFMPEG library libswresample.so.0
PKGFILES_CSWlibswresample0 += $(call pkgfiles_lib,libswresample.so.0)
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibswresample0 += CSWlibx264-125

PACKAGES += CSWlibavresample0
SPKG_DESC_CSWlibavresample0 = FFMPEG library libavresample.so.0
PKGFILES_CSWlibavresample0 += $(call pkgfiles_lib,libavresample.so.0)
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibx264-125
RUNTIME_DEP_PKGS_CSWlibavresample0 += CSWlibtheoraenc1

PACKAGES += CSWffmpeg-dev
SPKG_DESC_CSWffmpeg-dev = Development files for several FFMPEG shared libraries
PKGFILES_CSWffmpeg-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavcodec54
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavdevice54
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavfilter2
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavformat54
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibpostproc52
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibswscale2
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibswresample0
RUNTIME_DEP_PKGS_CSWffmpeg-dev += CSWlibavresample0


PACKAGES += CSWffmpeg
SPKG_DESC_CSWffmpeg = Very fast video and audio converter
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavformat54
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibswscale2
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavutil51
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibz1
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibogg0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavcodec54
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavdevice54
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibswresample0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavresample0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibtheoraenc1
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibavfilter2
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibspeex1
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibpostproc52
RUNTIME_DEP_PKGS_CSWffmpeg += CSWlibx264-125

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
#EXTRA_CFLAGS-64 += -fPIC
#EXTRA_CFLAGS += $(EXTRA_CFLAGS-$(MEMORYMODEL))

#EXTRA_CXXFLAGS-64 += -fPIC
#EXTRA_CXXFLAGS += $(EXTRA_CXXFLAGS-$(MEMORYMODEL))

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

#Needs sse to get asm stuff to work on x86
CONFIGURE_ARGS_i386 += --extra-cflags="-mfpmath=sse -msse"
CONFIGURE_ARGS_i386 += --extra-cxxflags="-mfpmath=sse -msse"
#no asm on sparc
CONFIGURE_ARGS_sparc = --disable-asm

#sparcv9 needs --enable-pic
CONFIGURE_ARGS_sparcv9 += --enable-pic

CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(ISA))

# Needs two builds one shared one static maybe in the future
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
CONFIGURE_ARGS += --enable-libx264

# Tests only work with static build
#SKIPTEST-SHARED-yes = 1
#SKIPTEST ?= $(SKIPTEST-SHARED-$(SHARED))

SKIPTEST ?= 1

include gar/category.mk

# For 'grep -q'
PATH := /opt/csw/gnu:$(PATH)
