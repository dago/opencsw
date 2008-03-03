GARNAME = kdelibs
CATEGORIES = kde

DESCRIPTION = Base set of libraries needed by KDE programs (gcc3)
define BLURB
  LONG DESCRIPTION
endef

DISTFILES += $(call admfiles,CSWkdelibs,)

#DEPENDS += lib/audiofile lib/glib2 lib/iconv lib/jasper
#DEPENDS += lib/jpeg lib/libart lib/libcups lib/libidn lib/libmad
#DEPENDS += lib/libogg lib/libxml2 lib/libxrender lib/libxslt
#DEPENDS += lib/openssl lib/pcre lib/png lib/tiff lib/libvorbis
#DEPENDS += lib/zlib
#DEPENDS += utils/aspell utils/bzip2
#DEPENDS += gnome/esound
#DEPENDS += lang/gcc
#DEPENDS += devel/gettext

DEPENDS += kde/arts lib/qt

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
