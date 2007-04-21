GARNAME = xfwm4-themes
CATEGORIES = xfce

DESCRIPTION = Xfce Window Manager Themes
define BLURB
   Xfce Window Manager Themes
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfce_xfwm4_themes, depend)

include ../category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

