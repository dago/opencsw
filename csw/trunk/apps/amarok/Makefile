GARNAME = amarok
GARVERSION = 1.4.6
CATEGORIES = apps

DESCRIPTION = Amarok is the music player for Linux and Unix with an intuitive interface
define BLURB
  Amarok is the KDE media player, but it
  is also widely used on other desktop environments
endef

MASTER_SITES = ftp://ftp.kde.org/pub/kde/stable/amarok/$(GARVERSION)/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWamarok,depend)

GARCOMPILER = GNU
CONFIGURE_ARGS = PATH="/opt/csw/kde-gcc/bin:$$PATH"
CONFIGURE_ARGS += LDFLAGS="-L/opt/csw/kde-gcc/lib -L/opt/csw/lib -lintl $$LD_FLAGS"
CONFIGURE_ARGS += LD_OPTIONS="-R/opt/csw/kde-gcc/lib -R/opt/csw/lib/$ISALIST $$LD_OPTIONS"
CONFIGURE_ARGS += --prefix=$(prefix)/kde-gcc --with-qt-dir=/opt/csw/kde-gcc --with-qt-libraries=/opt/csw/kde-gcc/lib --disable-debug

include ../category.mk

post-install: fix-libs

fix-libs:
	( gfind $(DESTDIR)/opt/csw/ -name \*.la -exec gsed -i -e "s~$(SPKG_WORKDIR)/$(GARNAME)-$(GARVERSION)/amarok/src/mediadevice/daap/mongrel/http11~~" -e "s~/opt/build/michael/xrender-0.8.3-buildroot/opt/csw/lib~~" {} \; )
