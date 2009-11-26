# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = ffmpeg
GARVERSION = 0.5
CATEGORIES = lib

DESCRIPTION = Very fast video and audio converter (includes libavcodec)
define BLURB
  FFmpeg is a complete, cross-platform solution to record, convert and stream
  audio and video. It includes libavcodec - the leading audio/video codec library.
endef

MASTER_SITES = http://ffmpeg.org/releases/
DISTFILES  = $(DISTNAME).tar.bz2

PATCHFILES = gnu-grep.patch

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
NO_ISAEXEC = 1

FFMPEG_CONFIGURE_ARGS_1 = $(filter-out --exec_%,$(DIRPATHS))
FFMPEG_CONFIGURE_ARGS_2 = $(filter-out --sbindir%,$(FFMPEG_CONFIGURE_ARGS_1))
CONFIGURE_ARGS = $(FFMPEG_CONFIGURE_ARGS)

GARCOMPILER = GNU

include gar/category.mk
