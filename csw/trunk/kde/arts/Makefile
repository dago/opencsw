GARNAME = arts
GARVERSION = 1.5.2
CATEGORIES = kde

DESCRIPTION = Analog RealTime Synthesizer for KDE (gcc3)
define BLURB
  LONG DESCRIPTION
endef

DISTFILES += $(call admfiles,CSWartsgcc,)

#DEPENDS += lib/audiofile lib/glib2 lib/iconv
#DEPENDS += lib/libogg lib/libxml2 lib/libxrender lib/libxslt
#DEPENDS += lib/png lib/libvorbis lib/libmad lib/zlib
#DEPENDS += gnome/esound
#DEPENDS += lang/gcc
#DEPENDS += devel/gettext

DEPENDS += lib/qt-gcc

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk
