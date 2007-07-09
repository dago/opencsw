GARNAME = MPlayer
GARVERSION = 1.0rc1
CATEGORIES = APPS

DESCRIPTION = media player
define BLURB
  LONG DESCRIPTION
endef


MASTER_SITES = http://www3.mplayerhq.hu/MPlayer/releases/ http://www3.mplayerhq.hu/MPlayer/releases/codecs/ http://www.mplayerhq.hu/MPlayer/skins/
DISTFILES  = MPlayer-$(GARVERSION).tar.bz2
DISTFILES += essential-20061022.tar.bz2
DISTFILES += Blue-1.7.tar.bz2
DISTFILES += $(call admfiles,CSWmplayer,depend)

PATCHFILES = fix-configure-sh-errors.diff

GARCOMPILER = GNU
GNU_CC_OPT = -O2 -pipe -mtune=i686 -fomit-frame-pointer

CONFIGURE_ARGS= --with-codecsdir=../essential-20061022 --enable-gui --disable-libcdio --prefix=/opt/csw --mandir=share/man

include ../category.mk

post-install:
	(mkdir -p $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)
	(cp -r $(WORKSRC)/../Blue/* $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)

