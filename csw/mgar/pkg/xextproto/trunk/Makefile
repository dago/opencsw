GARNAME = xextproto
GARVERSION = 7.0.3
CATEGORIES = lib

DESCRIPTION = xextproto
define BLURB
xextproto
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/proto/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

DISTFILES    += $(call admfiles,CSWxextproto, depend)

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
