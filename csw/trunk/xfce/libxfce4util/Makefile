GARNAME = libxfce4util
CATEGORIES = xfce

DESCRIPTION = Xfce Utilities Library 
define BLURB
  Xfce Utilities Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWlibxfce4util.depend CSWlibxfce4util.gspec CSWlibxfce4util.prototype
DISTFILES += CSWlibxfce4utildoc.depend CSWlibxfce4utildoc.gspec CSWlibxfce4utildoc.prototype
DISTFILES += CSWlibxfce4utildevel.depend CSWlibxfce4utildevel.gspec CSWlibxfce4utildevel.prototype

PATCHFILES = debug.h.patch

include ../category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | grep ELF | grep -e 'executable' -e 'dynamic lib' | grep 'not stripped' && strip {}"  \; )

