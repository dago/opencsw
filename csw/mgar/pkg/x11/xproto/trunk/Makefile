GARNAME = xproto
GARVERSION = 7.0.14
CATEGORIES = lib

DESCRIPTION = xproto
define BLURB
xproto
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/proto/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES    += $(call admfiles,CSWxproto, depend)

LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export LDFLAGS

TEST_SCRIPTS      = none

GREP = ggrep

include gar/category.mk

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man 

test-none:
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
