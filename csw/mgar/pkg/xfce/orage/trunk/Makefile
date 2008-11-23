GARNAME = orage
CATEGORIES = xfce

DESCRIPTION = Xfce Orage Calendar
define BLURB
   Orage provides a calendar which integrates nicely into the Xfce desktop environment. It is highly configurable and supports alerts based on dates. It warns you with popup or audio alarm. As it is an application kind-of every day use it launches itself in the background as a daemon.
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfceorage, depend)
# DISTFILES += CSWxfceorage.depend CSWxfceorage.gspec CSWxfceorage.prototype
# DISTFILES += CSWxfceoragedoc.depend CSWxfceoragedoc.gspec CSWxfceoragedoc.prototype

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

CONFIGURE_ARGS += --enable-reentrant

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

