GARNAME = xfce4-dev-tools
CATEGORIES = xfce

DESCRIPTION = Xfce Development Tools
define BLURB
   Xfce Development Tools 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfcedevtools, depend)

include ../category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

