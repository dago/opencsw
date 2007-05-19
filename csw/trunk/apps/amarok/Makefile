GARNAME = amarok
GARVERSION = 1.4.4
CATEGORIES = apps

DESCRIPTION = Amarok is the music player for Linux and Unix with an intuitive interface
define BLURB
  Amarok is the KDE media player, but it
  is also widely used on other desktop environments
endef

MASTER_SITES = ftp://ftp.kde.org/pub/kde/stable/amarok/1.4.4/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWamarok)

GARCOMPILER = GNU
CONFIGURE_ARGS = PATH="/opt/csw/kde-gcc/bin:$$PATH"
#CONFIGURE_ARGS += QTDIR=/opt/csw/kde-gcc
CONFIGURE_ARGS += LDFLAGS="-L/opt/csw/kde-gcc/lib -L/opt/csw/lib -lintl $$LD_FLAGS"
CONFIGURE_ARGS += LD_OPTIONS="-R/opt/csw/kde-gcc/lib -R/opt/csw/lib/$ISALIST $$LD_OPTIONS"
CONFIGURE_ARGS += --prefix=$(prefix)/kde-gcc --with-qt-dir=/opt/csw/kde-gcc --with-qt-libraries=/opt/csw/kde-gcc/lib --disable-debug

include ../category.mk
