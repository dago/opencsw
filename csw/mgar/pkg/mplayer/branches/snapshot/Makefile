# $Id$

NAME	=	mplayer
YEAR	?=	$(shell date '+%Y')
MONTH	?=	$(shell date '+%m')
DAY		?=	$(shell date '+%d')
VERSION	?=	$(YEAR)$(MONTH)$(DAY)
GARTYPE	=	v2

DESCRIPTION	=	Development snapshot of The Movie Player and Encoder
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
PATCHFILES		+=	0005-enhance-X-Windows-detection.patch
PATCHFILES		+=	0006-fix-memalign-detection.patch
PATCHFILES		+=	0007-fix-memalign-prototype.patch

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS	+=	CSWdocbookdtds
BUILD_DEP_PKGS	+=	CSWdocbookxsl
BUILD_DEP_PKGS	+=	CSWfaac
BUILD_DEP_PKGS	+=	CSWfontconfig-dev
BUILD_DEP_PKGS	+=	CSWgroff
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

PACKAGES								=	CSWmplayer-snapshot
CATALOGNAME_CSWmplayer-snapshot			=	mplayer_snapshot
SPKG_DESC_CSWmplayer-snapshot			=	$(DESCRIPTION), the player
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWfaac
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWliba52
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibaa1
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibaudiofile0
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibesd0
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibfaad2
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibfribidi0
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibjpeg62
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWliblzo2-2
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibmad0
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibmp3lame0
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibogg0
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibrtmp0
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibsdl1-2-0
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibspeex1
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibtheoradec1
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibx264-133
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibxvidcore4
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWmesa
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWmpg123
RUNTIME_DEP_PKGS_CSWmplayer-snapshot	+=	CSWnas

CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libGL.so
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libSDL-1.2.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libX11.so.4
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libXext.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libXinerama.so.1
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libXt.so.4
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|liba52.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libaa.so.1
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libaudio.so.2
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libbz2.so.1
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libesd.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libfaac.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libfaad.so.2
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libfontconfig.so.1
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libfreetype.so.6
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libfribidi.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libiconv.so.2
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libjpeg.so.62
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libkstat.so.1
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|liblzo2.so.2
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libmad.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libmp3lame.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libmpg123.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libogg.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libpng12.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|librtmp.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libspeex.so.1
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libtheoradec.so.1
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libvdpau.so.1
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libvorbis.so.0
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libvorbisenc.so.2
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libx264.so.133
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libxvidcore.so.4
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	no-direct-binding|/opt/csw/bin/mplayer-snapshot|is|not|directly|bound|to|soname|libz.so.1

# only on BO build farm; on my build farm it's included and detected TODO
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	surplus-dependency|CSWlibaudiofile0

# this cannot be computed:
RUNTIME_DEP_PKGS_CSWmplayer-snapshot		+=	CSWunrar
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	surplus-dependency|CSWunrar

# this exists only on i386 and Solaris 10
CHECKPKG_OVERRIDES_CSWmplayer-snapshot	+=	missing-dependency|NVDAgraphics
# this in incongruous (due to man/cat1 usage):
CHECKPKG_OVERRIDES_CSWmencoder-snapshot += missing-dependency|CSWfltk

PACKAGES								+=	CSWmencoder-snapshot
CATALOGNAME_CSWmencoder-snapshot		=	mencoder_snapshot
SPKG_DESC_CSWmencoder-snapshot			=	$(DESCRIPTION), the encoder
PKGFILES_CSWmencoder-snapshot			+=	/opt/csw/bin/mencoder-snapshot
PKGFILES_CSWmencoder-snapshot			+=	/opt/csw/share/man/man1/mencoder-snapshot.1
PKGFILES_CSWmencoder-snapshot			+=	/opt/csw/share/man/cat1/mencoder-snapshot.1
ARCHALL_CSWmencoder-snapshot			=	1
RUNTIME_DEP_PKGS_CSWmencoder-snapshot	+=	CSWmplayer-snapshot
CHECKPKG_OVERRIDES_CSWmencoder-snapshot	+=	surplus-dependency|CSWmplayer-snapshot

PACKAGES							+=	CSWmplayer-snapshot-doc
CATALOGNAME_CSWmplayer-snapshot-doc	=	$(NAME)_snapshot_doc
SPKG_DESC_CSWmplayer-snapshot-doc	=	$(DESCRIPTION), the documentation
PKGFILES_CSWmplayer-snapshot-doc	+=	$(docdir)/$(NAME)_snapshot_doc/.*
ARCHALL_CSWmplayer-snapshot-doc		=	1

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-extract:
	cd $(WORKSRC) && \
	mv ../ffmpeg ffmpeg && \
	rm -f .gitignore
	$(MAKECOOKIE)

# - configure is not configure !
# - must use internal dvdnav as our library is not a snapshot and
#   mplayer uses new primitives
# - run-time CPU detection is not implemented only for SPARC
# - disable shared memory, used only for X11, which, in Solaris 10
#    extensions doesn't support all the required primitives,
#   e.g. XShmGetEventBase

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
	--disable-shm \
	--prefix=$(prefix) \
	--confdir=$(sysconfdir)/$(NAME)-snapshot \
	--codecsdir=$(libexecdir)/mplayer-snapshot
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

post-install: thedocdir = $(docdir)/$(NAME)_snapshot_doc
post-install: thehtmldocdir = $(thedocdir)/html
post-install: thecatmandir = $(mandir)/cat1
post-install:
	ginstall -d "$(DESTDIR)/$(thecatmandir)"
	gnroff -Tlatin1 -mman $(WORKSRC)/DOCS/man/en/mplayer.1 > "$(DESTDIR)/$(thecatmandir)/mplayer-snapshot.1"
	cd "$(DESTDIR)/$(thecatmandir)" && ln -s mplayer-snapshot.1 mencoder-snapshot.1
	ginstall -d "$(DESTDIR)/$(thedocdir)"
	gtar --directory $(WORKSRC)/DOCS --create --file=- tech | \
	gtar --directory $(DESTDIR)/$(thedocdir) --extract
	ginstall -d "$(DESTDIR)/$(thehtmldocdir)"
	gtar --directory $(WORKSRC)/DOCS/HTML/en --create --file=- . | \
	gtar --directory $(DESTDIR)/$(thehtmldocdir) --extract
	cd $(DESTDIR)/$(bindir) && \
	mv mplayer mplayer-snapshot && \
	rm -f mencoder && \
	ln -s mplayer-snapshot mencoder-snapshot
	cd $(DESTDIR)/$(mandir)/man1 && \
	mv mplayer.1 mplayer-snapshot.1 && \
	rm -f mencoder.1 && \
	ln -s mplayer-snapshot.1 mencoder-snapshot.1
	$(MAKECOOKIE)
