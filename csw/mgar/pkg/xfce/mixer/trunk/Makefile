NAME = xfce4-mixer
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Volume Control
define BLURB
   Xfce Volume Control 
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
# DISTFILES += CSWxfcemixer.depend CSWxfcemixer.gspec CSWxfcemixer.prototype
DISTFILES += $(call admfiles,CSWxfcemixer, depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

