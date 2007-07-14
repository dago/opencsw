GARNAME = MPlayer
GARVERSION = 1.0rc1#will be try3
CATEGORIES = APPS

DESCRIPTION = media player
define BLURB
  LONG DESCRIPTION
endef


MASTER_SITES = http://www3.mplayerhq.hu/MPlayer/releases/ http://www3.mplayerhq.hu/MPlayer/releases/codecs/ http://www.mplayerhq.hu/MPlayer/skins/
#PATCH_SITES = http://www.mplayerhq.hu/MPlayer/patches/

DISTFILES  = MPlayer-$(GARVERSION).tar.bz2
DISTFILES += essential-20061022.tar.bz2
DISTFILES += Blue-1.7.tar.bz2
DISTFILES += $(call admfiles,CSWmplayer,depend)

PATCHFILES = fix-configure-sh-errors.diff
PATCHFILES += fix-solaris8-llrint.diff
PATCHFILES += fix-stdint.h-lazy.diff
PATCHFILES += security-asmrules_fix_20061231.diff
PATCHFILES += security-cddb_fix_20070605.diff

GARCOMPILER = GNU
#doesn't work well on sparc!! GNU_CC_OPT = -O2 -pipe -mtune=i686 -fomit-frame-pointer
GNU_CC_OPT = -O2 -pipe -fomit-frame-pointer

CONFIGURE_ARGS  = --with-codecsdir=../essential-20061022 --prefix=/opt/csw
# CONFIGURE_ARGS += --with-extraincdir=/usr/include
CONFIGURE_ARGS += --enable-gui
CONFIGURE_ARGS += --disable-libcdio
CONFIGURE_ARGS += --mandir=share/man

include ../category.mk

post-install:
	(mkdir -p $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)
	(cp -r $(WORKSRC)/../Blue/* $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)

