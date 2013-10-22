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

VENDOR_URL		=	http://www.mplayerhq.hu/MPlayer/
MASTER_SITES	=	http://www.mplayerhq.hu/MPlayer/releases/
MASTER_SITES	+=	http://ffmpeg.org/releases/
DISTFILES		=	$(NAME)-export-snapshot.tar.bz2
DISTFILES		+=	ffmpeg-snapshot.tar.bz2
DISTNAME		=	$(NAME)-export-$(YEAR)-$(MONTH)-$(DAY)
PATCHFILES		+=	0001-configure-uses-bash.patch
PATCHFILES		+=	0002-version-uses-bash.patch
PATCHFILES		+=	0003-use-csw-catalog-for-documentation.patch
PATCHFILES		+=	0004-test-sse-support.patch

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS	+=	CSWdocbookdtds
BUILD_DEP_PKGS	+=	CSWdocbookxsl
BUILD_DEP_PKGS	+=	CSWfaac
BUILD_DEP_PKGS	+=	CSWfontconfig-dev
BUILD_DEP_PKGS	+=	CSWliba52
BUILD_DEP_PKGS	+=	CSWlibaa-dev
BUILD_DEP_PKGS	+=	CSWlibaudiofile-dev
BUILD_DEP_PKGS	+=	CSWlibdvdcss-dev
BUILD_DEP_PKGS	+=	CSWlibdvdnav-dev
BUILD_DEP_PKGS	+=	CSWlibdvdread-dev
BUILD_DEP_PKGS	+=	CSWlibfaad-dev
BUILD_DEP_PKGS	+=	CSWlibfreetype-dev
BUILD_DEP_PKGS	+=	CSWlibfribidi-dev
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
BUILD_DEP_PKGS	+=	CSWlibrtmp-dev
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

PACKAGES						=	CSWmplayer
CATALOGNAME_CSWmplayer			=	mplayer
SPKG_DESC_CSWmplayer			=	$(DESCRIPTION), the player
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWfaac
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWliba52
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibaa1
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibaudiofile0
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibesd0
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibfaad2
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibfribidi0
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibjpeg62
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWliblzo2-2
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibmad0
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibogg0
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibrtmp0
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibspeex1
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibx264-133
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibxvidcore4
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWmesa
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWmpg123
RUNTIME_DEP_PKGS_CSWmplayer		+=	CSWnas

# only on BO build farm; on my build farm it's included and detected TODO
CHECKPKG_OVERRIDES_CSWmplayer	+=	surplus-dependency|CSWlibaudiofile0

CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libGL.so
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libSDL-1.2.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libXt.so.4
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|liba52.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libaa.so.1
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libaudio.so.2
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libaudiofile.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libbz2.so.1
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libesd.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libfaac.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libfaad.so.2
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libfontconfig.so.1
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libfreetype.so.6
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libfribidi.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libiconv.so.2
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libjpeg.so.62
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libkstat.so.1
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|liblzo2.so.2
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libmad.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libmp3lame.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libmpg123.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libogg.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libpng12.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|librtmp.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libspeex.so.1
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libtheoradec.so.1
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libvorbis.so.0
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libvorbisenc.so.2
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libx264.so.133
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libxvidcore.so.4
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libz.so.1
CHECKPKG_OVERRIDES_CSWmplayer	+=	no-direct-binding|/opt/csw/bin/mplayer|is|not|directly|bound|to|soname|libGL.so.1

PACKAGES						+=	CSWmencoder
CATALOGNAME_CSWmencoder			=	mencoder
SPKG_DESC_CSWmencoder			=	$(DESCRIPTION), the encoder
PKGFILES_CSWmencoder			+=	/opt/csw/bin/mencoder
PKGFILES_CSWmencoder			+=	/opt/csw/share/man/man1/mencoder.1

RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWliba52
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibfribidi0
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibxvidcore4
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibspeex1
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibfaad2
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibx264-133
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibogg0
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibjpeg62
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWfaac
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibrtmp0
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWliblzo2-2
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWlibmad0
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWmpg123
RUNTIME_DEP_PKGS_CSWmencoder	+=	CSWmplayer
CHECKPKG_OVERRIDES_CSWmencoder	+=	surplus-dependency|CSWmplayer

CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|liba52.so.0
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libbz2.so.1
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libfaac.so.0
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libfaad.so.2
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libfontconfig.so.1
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libfreetype.so.6
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libfribidi.so.0
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libiconv.so.2
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libjpeg.so.62
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libkstat.so.1
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|liblzo2.so.2
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libmad.so.0
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libmp3lame.so.0
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libmpg123.so.0
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libogg.so.0
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libpng12.so.0
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|librtmp.so.0
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libspeex.so.1
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libtheoradec.so.1
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libvorbis.so.0
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libvorbisenc.so.2
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libx264.so.133
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libxvidcore.so.4
CHECKPKG_OVERRIDES_CSWmencoder	+=	no-direct-binding|/opt/csw/bin/mencoder|is|not|directly|bound|to|soname|libz.so.1

PACKAGES						+=	CSWmplayer-doc
CATALOGNAME_CSWmplayer-doc		=	$(NAME)_doc
SPKG_DESC_CSWmplayer-doc		=	$(DESCRIPTION), the documentation
PKGFILES_CSWmplayer-doc			+=	$(docdir)/$(NAME)_doc/.*
ARCHALL_CSWmplayer-doc			=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-extract:
	cd $(WORKSRC) && \
	mv ../ffmpeg ffmpeg
	$(MAKECOOKIE)

# configure is not configure !
# must use internal dvdnav as our library is not a snapshot

ifneq ($(GARCH),sparc)
CPU_DETECTION	=--enable-runtime-cpudetection
else
CPU_DETECTION	=
endif

configure-custom:
	cd $(WORKSRC) && \
	./configure \
	--cc=gcc \
	--host-cc=gcc \
	--extra-cflags='-std=gnu99' \
	--extra-ldflags='-lrt' \
	$(CPU_DETECTION) \
	--prefix=$(prefix) \
	--codecsdir=$(libexecdir)/mplayer
	$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) && \
	$(MAKE) && \
	$(MAKE) doc
	$(MAKECOOKIE)

test-custom:
ifdef testData
	cd $(WORKSRC) && \
	[ -d $(testData) ] && \
	$(MAKE) FATE_SAMPLES=$(testData) fatetest
endif
	$(MAKECOOKIE)

post-install: thedocdir = $(docdir)/$(NAME)_doc
post-install: thehtmldocdir = $(thedocdir)/html
post-install:
	ginstall -d "$(DESTDIR)/$(thedocdir)"
	gtar --directory $(WORKSRC)/DOCS --create --file=- tech | \
	gtar --directory $(DESTDIR)/$(thedocdir) --extract
	ginstall -d "$(DESTDIR)/$(thehtmldocdir)"
	gtar --directory $(WORKSRC)/DOCS/HTML/en --create --file=- . | \
	gtar --directory $(DESTDIR)/$(thehtmldocdir) --extract
	$(MAKECOOKIE)
