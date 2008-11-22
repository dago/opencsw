GARNAME = xfce4-mixer
CATEGORIES = xfce

DESCRIPTION = Xfce Volume Control
define BLURB
   Xfce Volume Control 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWxfcemixer.depend CSWxfcemixer.gspec CSWxfcemixer.prototype
DISTFILES += $(call admfiles,CSWxfcemixer, depend)

TEST_SCRIPTS = none

include ../category.mk

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

