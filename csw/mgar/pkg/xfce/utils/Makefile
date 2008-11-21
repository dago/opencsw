GARNAME = xfce-utils
CATEGORIES = xfce

DESCRIPTION = Xfce Utilities
define BLURB
   Xfce Utilities 
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfceutils.depend CSWxfceutils.gspec CSWxfceutils.prototype
DISTFILES += CSWxfceutilsdoc.depend CSWxfceutilsdoc.gspec CSWxfceutilsdoc.prototype

# PATCHFILES = xinitrc.patch

TEST_SCRIPTS = none

include ../category.mk

test-none :
	@$(MAKECOOKIE)

CPPFLAGS += -I$(DESTDIR)/opt/csw/include/dbus-1.0
CPPFLAGS += -I$(DESTDIR)/opt/csw/lib/dbus-1.0/include

CONFIGURE_ARGS += --enable-dbus

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

