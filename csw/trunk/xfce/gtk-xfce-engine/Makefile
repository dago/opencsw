GARNAME = gtk-xfce-engine
CATEGORIES = xfce

DESCRIPTION = Xfce GTK theme engine 
define BLURB
   Xfce GTK theme engine 
endef

GARVERSION = 2.4.0
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgtkxfceengine, depend)

include ../category.mk

CFLAGS   += -xlibmil
CXXFLAGS += -xlibmil -xlibmopt -features=tmplife -norunpath
CPPFLAGS += -I$(DESTDIR)/opt/csw/include/xfce4
LDFLAGS  += -L/opt/csw/lib -R/opt/csw/lib

# DEPENDS += xfce/libxfce4util

CONFIGURE_ARGS = --prefix=/opt/csw --disable-debug --enable-final 

post-install:
	( mv $(DESTDIR)/opt/csw/lib/gtk-2.0/2.10.0/engines $(DESTDIR)/opt/csw/lib/gtk-2.0 )
