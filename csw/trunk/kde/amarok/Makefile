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

PATCHFILES = disable-broken-languages.diff
#PATCHFILES = fix-libtool-linker-problem.diff

GARCOMPILER = GNU
CONFIGURE_ARGS = PATH="/opt/csw/kde-gcc/bin:$$PATH"
CONFIGURE_ARGS += LDFLAGS="-R/opt/csw/kde-gcc/lib -L/opt/csw/kde-gcc/lib"
CONFIGURE_ARGS += --prefix=$(prefix)/kde-gcc --with-qt-dir=/opt/csw/kde-gcc --with-qt-libraries=/opt/csw/kde-gcc/lib --disable-debug --disable-rpath

include ../category.mk

#I'm having all manner of issues with the final linking of amarok, reset any GAR inherited LD_OPTIONS, then remove the wl= statements from libtool, they're confusing GCC

LD_OPTIONS=

post-configure: remove-wl
post-install: fix-libs

remove-wl:
	( gsed -i -e s~wl=\"-Wl,\"~wl=\"\"~ $(SPKG_WORKDIR)/$(GARNAME)-$(GARVERSION)/libtool )

fix-libs:
	( gfind $(DESTDIR)/opt/csw/ -name \*.la -exec gsed -i -e "s~$(SPKG_WORKDIR)/$(GARNAME)-$(GARVERSION)/amarok/src/mediadevice/daap/mongrel/http11~~" -e "s~/opt/build/michael/xrender-0.8.3-buildroot/opt/csw/lib~~" {} \; )
