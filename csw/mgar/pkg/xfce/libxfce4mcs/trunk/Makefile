GARNAME = libxfce4mcs
CATEGORIES = xfce

DESCRIPTION = Xfce Settings Manager Library 
define BLURB
   Xfce Settings Manager Library 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWlibxfce4mcs.depend CSWlibxfce4mcs.gspec CSWlibxfce4mcs.prototype
# DISTFILES += CSWlibxfce4mcsdoc.depend CSWlibxfce4mcsdoc.gspec CSWlibxfce4mcsdoc.prototype
# DISTFILES += CSWlibxfce4mcsdev.depend CSWlibxfce4mcsdev.gspec CSWlibxfce4mcsdev.prototype
DISTFILES += $(call admfiles,CSWlibxfce4mcs, depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_SCRIPTS = none

include gar/category.mk

test-none : 
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

