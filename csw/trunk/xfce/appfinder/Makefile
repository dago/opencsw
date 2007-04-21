GARNAME = xfce4-appfinder
CATEGORIES = xfce

DESCRIPTION = Xfce Application Finder
define BLURB
   Xfce Application Finder 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfce_appfinder, depend)

include ../category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

