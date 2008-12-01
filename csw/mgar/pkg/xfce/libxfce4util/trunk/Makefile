GARNAME = libxfce4util
CATEGORIES = xfce

DESCRIPTION = Xfce Utilities Library 
define BLURB
  Xfce Utilities Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWlibxfce4util.depend CSWlibxfce4util.gspec CSWlibxfce4util.prototype
DISTFILES += CSWlibxfce4utildoc.depend CSWlibxfce4utildoc.gspec CSWlibxfce4utildoc.prototype
DISTFILES += CSWlibxfce4utildev.depend CSWlibxfce4utildev.gspec CSWlibxfce4utildev.prototype
# DISTFILES += $(call admfiles,CSWlibxfce4util, depend) 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PATCHFILES += gar-base.diff

TEST_SCRIPTS = none

include gar/category.mk


test-none:
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

