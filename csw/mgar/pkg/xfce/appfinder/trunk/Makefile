NAME = xfce4-appfinder
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Application Finder
define BLURB
   Xfce Application Finder 
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
# DISTFILES += CSWxfceappfinder.depend CSWxfceappfinder.gspec CSWxfceappfinder.prototype
DISTFILES += $(call admfiles,CSWxfceappfinder, depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

