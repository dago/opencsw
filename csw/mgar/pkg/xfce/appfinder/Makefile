GARNAME = xfce4-appfinder
CATEGORIES = xfce

DESCRIPTION = Xfce Application Finder
define BLURB
   Xfce Application Finder 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWxfceappfinder.depend CSWxfceappfinder.gspec CSWxfceappfinder.prototype
DISTFILES += $(call admfiles,CSWxfceappfinder, depend)

TEST_SCRIPTS = none

include ../category.mk

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

