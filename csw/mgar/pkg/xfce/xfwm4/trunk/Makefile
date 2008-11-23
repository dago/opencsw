GARNAME = xfwm4
CATEGORIES = xfce

DESCRIPTION = Xfce Window Manager 
define BLURB
   Xfce Window Manager
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfcexfwm4.depend CSWxfcexfwm4.gspec CSWxfcexfwm4.prototype
DISTFILES += CSWxfcexfwm4doc.depend CSWxfcexfwm4doc.gspec CSWxfcexfwm4doc.prototype

# PATCHFILES = frame.c.diff

LIBDEPS = xfce/mcs-mananager

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

CONFIGURE_ARGS +=  --enable-xsync --enable-render --enable-randr --enable-xinerama --enable-compositor

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

