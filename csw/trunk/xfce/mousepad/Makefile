GARNAME = mousepad
GARVERSION = 0.2.13
CATEGORIES = xfce

DESCRIPTION = Xfce Mousepad Text Editor
define BLURB
   Xfce Mousepad Text Editor 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWxfcemousepad.depend CSWxfcemousepad.gspec CSWxfcemousepad.prototype
DISTFILES += $(call admfiles,CSWxfcemousepad, depend)

TEST_SCRIPTS = none

include ../category.mk

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

