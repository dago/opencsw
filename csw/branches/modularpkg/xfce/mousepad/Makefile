GARNAME = mousepad
GARVERSION = 0.2.12
CATEGORIES = xfce

DESCRIPTION = Xfce Mousepad Text Editor
define BLURB
   Xfce Mousepad Text Editor 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfcemousepad.depend CSWxfcemousepad.gspec CSWxfcemousepad.prototype


# PATCHFILES += configure.in.diff
# PATCHFILES += configure.diff

include ../category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

