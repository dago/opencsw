# $Id$

NAME	=	mplayer
YEAR	=	$(shell date '+%Y')
MONTH	=	$(shell date '+%m')
DAY		=	$(shell date '+%d')
VERSION	=	$(YEAR)$(MONTH)$(DAY)
GARTYPE	=	v2

DESCRIPTION	=	The Movie Player and Encoder
define BLURB

    MPlayer can play most standard video formats out of the box and
    almost all others with the help of external codecs.  MPlayer
    currently works best from the command line, but visual feedback
    for many functions is available from its onscreen status display
    (OSD), which is also used for displaying subtitles. MPlayer also
    has a GUI with skin support and several unofficial alternative
    graphical frontends are available.

	MEncoder is a command line video encoder for advanced users that
	can be built from the MPlayer source tree. Unofficial graphical
	frontends exist but are not included.
endef

MASTER_SITES	=	http://www.mplayerhq.hu/MPlayer/releases/
MASTER_SITES	+=	http://ffmpeg.org/releases/
DISTFILES		=	$(NAME)-export-snapshot.tar.bz2
DISTFILES		+=	ffmpeg-snapshot.tar.bz2
DISTNAME		=	$(NAME)-export-$(YEAR)-$(MONTH)-$(DAY)
PATCHFILES		+=	0001-configure-uses-bash.patch
PATCHFILES		+=	0002-version-uses-bash.patch

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS	+=	CSWfaac
BUILD_DEP_PKGS	+=	CSWfontconfig-dev
BUILD_DEP_PKGS	+=	CSWliba52
BUILD_DEP_PKGS	+=	CSWlibaa-dev
BUILD_DEP_PKGS	+=	CSWlibdvdcss-dev
BUILD_DEP_PKGS	+=	CSWlibdvdnav-dev
BUILD_DEP_PKGS	+=	CSWlibdvdread-dev
BUILD_DEP_PKGS	+=	CSWlibfaad-dev
BUILD_DEP_PKGS	+=	CSWlibfreetype-dev
BUILD_DEP_PKGS	+=	CSWlibgif-dev
BUILD_DEP_PKGS	+=	CSWlibiconv-dev
BUILD_DEP_PKGS	+=	CSWlibjpeg-dev
BUILD_DEP_PKGS	+=	CSWliblz-dev
BUILD_DEP_PKGS	+=	CSWliblzo-dev
BUILD_DEP_PKGS	+=	CSWlibmad-dev
BUILD_DEP_PKGS	+=	CSWlibmp3lame-dev
BUILD_DEP_PKGS	+=	CSWlibncurses-dev
BUILD_DEP_PKGS	+=	CSWlibogg-dev
BUILD_DEP_PKGS	+=	CSWliboggz-dev
BUILD_DEP_PKGS	+=	CSWlibpng-dev
BUILD_DEP_PKGS	+=	CSWlibsdl-dev
BUILD_DEP_PKGS	+=	CSWlibspeex-dev
BUILD_DEP_PKGS	+=	CSWlibtheora-dev
BUILD_DEP_PKGS	+=	CSWlibx264-dev
BUILD_DEP_PKGS	+=	CSWlibxvidcore-dev
BUILD_DEP_PKGS	+=	CSWmesa
BUILD_DEP_PKGS	+=	CSWmpg123
BUILD_DEP_PKGS	+=	CSWnas
BUILD_DEP_PKGS	+=	CSWunrar
BUILD_DEP_PKGS	+=	CSWlibxmms-dev
BUILD_DEP_PKGS	+=	CSWyasm

GARCOMPILER		=	GNU

# 2 packages: mplayer, mencoder; separate recipe for codec, fonts and
# skin

CONFIGURE_SCRIPTS	=	custom
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=	custom

RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWfaac
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWliba52
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibaa1
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibesd0
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibfaad2
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibfribidi0
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibjpeg62
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWliblzo2-2
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibmad0
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibogg0
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibrtmp0
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibspeex1
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibx264-133
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibxvidcore4
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWmesa
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWmpg123
RUNTIME_DEP_PKGS_CSWmplayer	+=	CSWnas

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-extract:
	cd $(WORKSRC) && \
	mv ../ffmpeg ffmpeg
	$(MAKECOOKIE)

# configure is not configure !
# must use internal dvdnav as our library is not a snapshot
configure-custom:
	cd $(WORKSRC) && \
	./configure \
	--cc=gcc \
	--host-cc=gcc \
	--extra-cflags='-std=gnu99' \
	--extra-ldflags='-lrt' \
	--enable-runtime-cpudetection \
	--prefix=$(prefix) \
	--codecsdir=$(libexecdir)/mplayer
	$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) && \
	$(MAKE)
	$(MAKECOOKIE)

test-custom:
ifdef testData
	cd $(WORKSRC) && \
	[ -d $(testData) ] && \
	$(MAKE) FATE_SAMPLES=$(testData) fatetest
endif
	$(MAKECOOKIE)
