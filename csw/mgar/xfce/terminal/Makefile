GARNAME = Terminal
GARVERSION = 0.2.8
CATEGORIES = xfce

DESCRIPTION = Xfce Terminal Emulator
define BLURB
   Xfce Terminal Emulator
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
# DISTFILES += CSWxfceterminal.depend CSWxfceterminal.gspec CSWxfceterminal.prototype
# DISTFILES += CSWxfceterminaldoc.depend CSWxfceterminaldoc.gspec CSWxfceterminaldoc.prototype

# PATCHFILES += configure.in.diff
# PATCHFILES += configure.diff

DISTFILES += $(call admfiles,CSWxfceterminal, depend)

TEST_SCRIPTS = none

include ../category.mk

test-none :
	@$(MAKECOOKIE)

CPPFLAGS += -I$(DESTDIR)/opt/csw/include/dbus-1.0
CPPFLAGS += -I$(DESTDIR)/opt/csw/lib/dbus-1.0/include

CONFIGURE_ARGS += --enable-dbus

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

