NAME = xfce4-dev-tools
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Development Tools
define BLURB
   Xfce Development Tools 
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfcedevtools, depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

include gar/category.mk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

