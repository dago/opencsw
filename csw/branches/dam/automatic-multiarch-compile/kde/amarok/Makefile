GARNAME = amarok
GARVERSION = 1.4.8
CATEGORIES = apps

DESCRIPTION = Amarok is the music player for Linux and Unix with an intuitive interface
define BLURB
  Amarok is the KDE media player, but it
  is also widely used on other desktop environments
endef

MASTER_SITES = ftp://ftp.kde.org/pub/kde/stable/amarok/$(GARVERSION)/src/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWamarok,depend)

PATCHFILES = disable-broken-languages.diff
PATCHFILES += gpod-stdint.h.diff

GARCOMPILER = GNU

LIBDEPS += lib/libgpod

CONFIGURE_ARGS = PATH="/opt/csw/kde-gcc/bin:$$PATH"
CONFIGURE_ARGS += LDFLAGS="-R/opt/csw/kde-gcc/lib -R/opt/csw/lib/$$ISALIST -L/opt/csw/kde-gcc/lib -L/opt/csw/lib/$$ISALIST"
CONFIGURE_ARGS += --prefix=$(prefix)/kde-gcc
CONFIGURE_ARGS += --with-qt-dir=/opt/csw/kde-gcc
CONFIGURE_ARGS += --with-qt-libraries=/opt/csw/kde-gcc/lib
CONFIGURE_ARGS += --includedir=/opt/csw/include
CONFIGURE_ARGS += --with-extra-inc=/opt/csw/include
CONFIGURE_ARGS += --with-libgpod
CONFIGURE_ARGS += --includedir=$(DESTDIR)/opt/csw/include/gpod-1.0/gpod
CONFIGURE_ARGS += --with-extra-libs=$(DESTDIR)/opt/csw/lib/gpod-1.0/gpod
CONFIGURE_ARGS += --disable-debug

TEST_SCRIPTS =

include ../category.mk


#I'm having all manner of issues with the final RUNPATH linking of amarok
#Setting LD_OPTIONS here explicitly, as kde-gcc/lib _MUST_ be first for qt to work

LD_OPTIONS := "-R/opt/csw/kde-gcc/lib:/opt/csw/\$$ISALIST:/opt/csw/lib"

post-install: fix-libtool-paths

fix-libtool-paths:
	( gfind $(DESTDIR)/opt/csw/kde-gcc -name \*.la -exec gsed -i -e "s~$(SPKG_WORKDIR)/$(GARNAME)-$(GARVERSION)/amarok/src/mediadevice/daap/mongrel/http11~~" -e "s~/opt/build/michael/xrender-0.8.3-buildroot/opt/csw/lib~~" -e "s~/opt/build/jwheeler/build/opt/csw/lib/gpod-1.0/gpod~~" -e "s~/opt/build/jwheeler/build/opt/csw/lib~~" {} \; )
