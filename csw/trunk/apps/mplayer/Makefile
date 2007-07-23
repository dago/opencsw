GARNAME = MPlayer
GARVERSION = 1.0rc1
CATEGORIES = APPS

DESCRIPTION = A multimedia player
define BLURB
#  LONG DESCRIPTION
endef


MASTER_SITES = http://www3.mplayerhq.hu/MPlayer/releases/ http://www3.mplayerhq.hu/MPlayer/releases/codecs/ http://www.mplayerhq.hu/MPlayer/skins/

DISTFILES  = $(GARNAME)-1.0rc1.tar.bz2
DISTFILES += Blue-1.7.tar.bz2
DISTFILES += $(call admfiles,CSWmplayer)

PATCHFILES  = fix-configure-variables.diff
PATCHFILES += fix-solaris8-llrint.diff
PATCHFILES += fix-stdint.h-includes.diff
PATCHFILES += fix-configure-stdint.h-detection.diff
PATCHFILES += security-asmrules_fix_20061231.diff
PATCHFILES += security-cddb_fix_20070605.diff
###v8 build PATCHFILES += sparc-v8build.diff

GARCOMPILER = GNU
#doesn't work well on sparc!! GNU_CC_OPT = -O2 -pipe -mtune=i686 -fomit-frame-pointer

ifeq ($(GARCH),i386)
	GNU_CC_OPT = -O2 -pipe -mtune=i686 -fomit-frame-pointer
else
	GNU_CC_OPT = -O2 -pipe -mv8
endif


CONFIGURE_ARGS  = --with-codecsdir=/opt/csw/share/codecs --prefix=/opt/csw
CONFIGURE_ARGS += --with-extraincdir=/usr/X11/include
CONFIGURE_ARGS += --mandir=share/man
CONFIGURE_ARGS += --enable-gui
CONFIGURE_ARGS += --disable-libcdio
#CONFIGURE_ARGS += --as=/opt/csw/bin/gas

include ../category.mk

##ISA opt area start##
#i686 is Pentium Pro and above

i386_ISALIST	= i686 pentium3 pentium4
sparc_ISALIST	= sparcv8plus+vis sparcv9

jw:
#	( echo $(GARCH) ) #GARCH is 'i386'
#	( echo $(GARCH)_ISALIST )  #GARCH is 'i386_ISALIST'

#	( for ISA in "" $($(GARCH)_ISALIST); do echo $$ISA; done )
	( cd $(WORKSRC) if [ -f mplayer.i* ] then rm mplayer.* fi && \
	for ISA in $($(GARCH)_ISALIST); do \
	 	GNU_CC_OPT="-O2 -pipe -mtune=$$ISA" gmake && mv mplayer mplayer.$$ISA; done )

##ISA opt area end##

post-install: skins fonts # codecs

skins:
	(mkdir -p $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)
	(cp -r $(WORKSRC)/../Blue/* $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/skins/default)

fonts:
	(ln -f -s /usr/openwin/lib/X11/fonts/TrueType/Arial.ttf $(DESTDIR)$(BUILD_PREFIX)/share/mplayer/subfont.ttf)

codecs:
	(mkdir -p $(DESTDIR)$(BUILD_PREFIX)/lib/codecs)
	(cp -r $(WORKSRC)/../all-20061022/* $(DESTDIR)$(BUILD_PREFIX)/share/codecs) 
