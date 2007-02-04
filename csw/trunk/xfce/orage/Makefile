GARNAME = orage
CATEGORIES = xfce

DESCRIPTION = Xfce Orage Calendar
define BLURB
   Orage provides a calendar which integrates nicely into the Xfce desktop environment. It is highly configurable and supports alerts based on dates. It warns you with popup or audio alarm. As it is an application kind-of every day use it launches itself in the background as a daemon.
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWxfceorage, depend)

include ../category.mk

CONFIGURE_ARGS += --enable-reentrant
