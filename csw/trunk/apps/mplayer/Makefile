GARNAME = MPlayer
GARVERSION = 1.0rc1
CATEGORIES = APPS

DESCRIPTION = A multimedia player
define BLURB
#  LONG DESCRIPTION
endef


MASTER_SITES = http://www3.mplayerhq.hu/MPlayer/releases/ http://www3.mplayerhq.hu/MPlayer/releases/codecs/ http://www.mplayerhq.hu/MPlayer/skins/
#PATCH_SITES = http://www.mplayerhq.hu/MPlayer/patches/

DISTFILES  = $(GARNAME)-1.0rc1.tar.bz2
DISTFILES += essential-20061022.tar.bz2
DISTFILES += Blue-1.7.tar.bz2
DISTFILES += $(call admfiles,CSWmplayer)

PATCHFILES  = fix-configure-sh-errors.diff
PATCHFILES += fix-solaris8-llrint.diff
PATCHFILES += fix-stdint.h-lazy.diff
PATCHFILES += security-asmrules_fix_20061231.diff
PATCHFILES += security-cddb_fix_20070605.diff

GARCOMPILER = GNU
#doesn't work well on sparc!! GNU_CC_OPT = -O2 -pipe -mtune=i686 -fomit-frame-pointer
GNU_CC_OPT = -O2 -pipe -fomit-frame-pointer

CONFIGURE_ARGS  = --with-codecsdir=../essential-20061022 --prefix=/opt/csw
CONFIGURE_ARGS += --with-extraincdir=/usr/X11/include
CONFIGURE_ARGS += --enable-gui
CONFIGURE_ARGS += --disable-libcdio
CONFIGURE_ARGS += --mandir=share/man
CONFIGURE_ARGS += --as=/opt/csw/bin/gas

include ../category.mk

post-install:
	(mkdir -p $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)
	(ln -f -s /usr/openwin/lib/X11/fonts/TrueType/Arial.ttf $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/subfont.ttf)
	(cp -r $(WORKSRC)/../Blue/* $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)
