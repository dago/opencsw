GARNAME = xfce4-icon-theme
CATEGORIES = xfce

DESCRIPTION = Xfce Icon Theme
define BLURB
   Xfce Icon Theme
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfce_icontheme, depend)

include ../category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

