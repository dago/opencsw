# This is pretty hard to build and outdated:
#   https://trac.macports.org/ticket/17141
# Use libmp4v2 instead.

NAME = mpeg4ip
VERSION = 1.6.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Libraries for MPEG-4/H.261/MPEG-2/H.263 MP3/AAC/AMR
define BLURB
  Provided are a live MPEG-4/H.261/MPEG-2/H.263 MP3/AAC/AMR broadcaster
  and file recorder, command line utilities such as an MP4 file creator
  and hinter, and an player that can both stream and playback from local file.
endef

SF_PROJ = mpeg4ip
# SF doesn't have the latest version as it was removed due to some breakage
# So we get it from another place and patch the flaw away
MASTER_SITES = http://download.m0k.org/handbrake/contrib/


DISTFILES   = $(NAME)-$(VERSION).tar.gz
DISTNAME    = $(NAME)
PATCHFILES  = mpeg4ip-1.6.1-mjj.patch 
# PATCHFILES += SDL_sunaudio.c.diff
# PATCHFILES += type_basic.cpp.diff

# PATCHFILES += 0001-Bootstrap-again.patch

PATCHFILES  = 0002-Move-external-function-definition-out-of-function.patch
PATCHFILES += 0003-Change-type-from-Void-to-void.patch
PATCHFILES += 0004-Add-one-more-scratch-channel-or-compilation-fails.patch

GARCOMPILER = GNU
BUILD64_LIBS_ONLY = 1

# EXTRA_CPPFLAGS = -D_GETOPT_H=1 -DHAVE_GETOPT_H
EXTRA_CPPFLAGS = -DHAVE_GETOPT_H -D__GNU_LIBRARY__

CONFIGURE_SCRIPTS = $(WORKSRC)/cvs_bootstrap

# The player needs ffmpeg which needs faad which needs mpeg4ip.
# Build the player in a separate recipe after we have the lib to break the circle.
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static
CONFIGURE_ARGS += --enable-server --disable-player
CONFIGURE_ARGS += --enable-mp4live
CONFIGURE_ARGS += --enable-ipv6

CONFIGURE_ARGS_isa-i386 = --enable-mmx
CONFIGURE_ARGS_isa-sparc = --disable-mmx
CONFIGURE_ARGS += $(CONFIGURE_ARGS_isa-$(ISA))

PACKAGES = CSWmpeg4ip
CATALOGNAME_CSWmpeg4ip = mpeg4ip
SPKG_DESC_CSWmpeg4ip = $(DESCRIPTION)

BUILD_DEP_PKGS_CSWmpeg4ip = CSWlibgnugetopt


include gar/category.mk

post-extract-modulated:
	-rm -f $(WORKSRC)/bootstrapped
	@$(MAKECOOKIE)

configure-%/cvs_bootstrap:
	@echo " ==> Running CVS bootstrap in $*"
	cd $* && $(CONFIGURE_ENV) ./cvs_bootstrap $(CONFIGURE_ARGS)
	@$(MAKECOOKIE)
