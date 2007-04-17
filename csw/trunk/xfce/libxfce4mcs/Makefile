GARNAME = libxfce4mcs
CATEGORIES = xfce

DESCRIPTION = Xfce Settings Manager Library 
define BLURB
   Xfce Settings Manager Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWlibxfce4mcs.depend CSWlibxfce4mcs.gspec CSWlibxfce4mcs.prototype
DISTFILES += CSWlibxfce4mcsdoc.depend CSWlibxfce4mcsdoc.gspec CSWlibxfce4mcsdoc.prototype
DISTFILES += CSWlibxfce4mcsdevel.depend CSWlibxfce4mcsdevel.gspec CSWlibxfce4mcsdevel.prototype
#DISTFILES += $(call admfiles,CSWlibxfce4mcs, depend)

include ../category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

