GARNAME = gtk-xfce-engine
CATEGORIES = xfce

DESCRIPTION = Xfce GTK theme engine 
define BLURB
   Xfce GTK theme engine 
endef

GARVERSION = 2.4.2
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWgtkxfceengine.depend CSWgtkxfceengine.gspec CSWgtkxfceengine.prototype
DISTFILES += $(call admfiles,CSWgtkxfceengine, depend)

TEST_SCRIPTS = none

include ../category.mk

CFLAGS   += -xlibmil
CXXFLAGS += -xlibmil -xlibmopt -features=tmplife -norunpath
CPPFLAGS += -I$(DESTDIR)/opt/csw/include/xfce4
LDFLAGS  += -L/opt/csw/lib -R/opt/csw/lib

# DEPENDS += xfce/libxfce4util

CONFIGURE_ARGS = --prefix=/opt/csw --disable-debug --enable-final 

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
	( if [ -d $(DESTDIR)/opt/csw/lib/gtk-2.0/2.10.0/engines ] ; then  cp -frpv $(DESTDIR)/opt/csw/lib/gtk-2.0/2.10.0/engines $(DESTDIR)/opt/csw/lib/gtk-2.0 ; rm -fr $(DESTDIR)/opt/csw/lib/gtk-2.0/2.10.0 ; fi ; )
