GARNAME = xfdesktop
CATEGORIES = xfce

DESCRIPTION = Xfce Desktop Manager
define BLURB
   Xfce Desktop Manager 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfcedesktop.depend CSWxfcedesktop.gspec CSWxfcedesktop.prototype
DISTFILES += CSWxfcedesktopdoc.depend CSWxfcedesktopdoc.gspec CSWxfcedesktopdoc.prototype

CONFIGURE_ARGS +=   --enable-desktop-icons 
CONFIGURE_ARGS +=   --enable-file-icons
CONFIGURE_ARGS +=   --enable-thunarx 
CONFIGURE_ARGS +=   --enable-exo
CONFIGURE_ARGS +=   --enable-menueditor 
CONFIGURE_ARGS +=   --enable-desktop-menu
CONFIGURE_ARGS +=   --enable-panel-plugin

include ../category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

