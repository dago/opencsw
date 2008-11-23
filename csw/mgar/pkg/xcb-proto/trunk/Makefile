GARNAME = xcb-proto
GARVERSION = 1.1
CATEGORIES = lib

DESCRIPTION = xcb-proto
define BLURB
xcb-proto
endef

MASTER_SITES =http://xcb.freedesktop.org/dist/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

DISTFILES    += $(call admfiles,CSWxcb-proto, depend)

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
