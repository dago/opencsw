GARNAME = amarok
GARVERSION = 1.4.7
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

GARCOMPILER = GNU

CONFIGURE_ARGS = PATH="/opt/csw/kde-gcc/bin:$$PATH"
CONFIGURE_ARGS += LDFLAGS="-R/opt/csw/kde-gcc/lib -R/opt/csw/lib/$$ISALIST -L/opt/csw/kde-gcc/lib -L/opt/csw/lib/$$ISALIST"
CONFIGURE_ARGS += --prefix=$(prefix)/kde-gcc
CONFIGURE_ARGS += --with-qt-dir=/opt/csw/kde-gcc
CONFIGURE_ARGS += --with-qt-libraries=/opt/csw/kde-gcc/lib
CONFIGURE_ARGS += --includedir=/opt/csw/include
CONFIGURE_ARGS += --with-extra-inc=/opt/csw/include
CONFIGURE_ARGS += --disable-debug
#CONFIGURE_ARGS += --with-libgpod

include ../category.mk

#I'm having all manner of issues with the final RUNPATH linking of amarok
#**not needed? First, remove the wl= statements from libtool, they're causing GCC to not honour $LD_OPTIONS
#Second, set our own LD_OPTIONS, as the kde-gcc/lib dir _MUST_ be first for qt to work

jw:
	( echo $(LD_OPTIONS) )

LD_OPTIONS := "-R/opt/csw/kde-gcc/lib:/opt/csw/\$$ISALIST:/opt/csw/lib"

#post-configure: remove-wl
post-install: fix-libs

remove-wl:
	( gsed -i -e s~wl=\"-Wl,\"~wl=\"\"~ $(SPKG_WORKDIR)/$(GARNAME)-$(GARVERSION)/libtool )

fix-libs:
	( gfind $(DESTDIR)/opt/csw/ -name \*.la -exec gsed -i -e "s~$(SPKG_WORKDIR)/$(GARNAME)-$(GARVERSION)/amarok/src/mediadevice/daap/mongrel/http11~~" -e "s~/opt/build/michael/xrender-0.8.3-buildroot/opt/csw/lib~~" {} \; )
