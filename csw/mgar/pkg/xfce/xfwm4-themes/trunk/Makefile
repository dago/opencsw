GARNAME = xfwm4-themes
CATEGORIES = xfce

DESCRIPTION = Xfce Window Manager Themes
define BLURB
   Xfce Window Manager Themes
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWxfcexfwm4themes.depend CSWxfcexfwm4themes.gspec CSWxfcexfwm4themes.prototype
DISTFILES += $(call admfiles,CSWxfcexfwm4themes, depend)

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

