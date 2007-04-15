GARNAME = Terminal
GARVERSION = 0.2.6
CATEGORIES = xfce

DESCRIPTION = Xfce Terminal Emulator
define BLURB
   Xfce Terminal Emulator
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += CSWxfceterminal.depend CSWxfceterminal.gspec CSWxfceterminal.prototype
DISTFILES += CSWxfceterminaldoc.depend CSWxfceterminaldoc.gspec CSWxfceterminaldoc.prototype

PATCHFILES += configure.in.diff
PATCHFILES += configure.diff

include ../category.mk

CONFIGURE_ARGS += --enable-dbus
