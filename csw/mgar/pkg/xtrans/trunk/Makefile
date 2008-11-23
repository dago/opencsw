GARNAME = xtrans
GARVERSION = 1.2.2
CATEGORIES = lib

DESCRIPTION = X transport library
define BLURB
xtrans includes a number of routines to make X implementations transport-independent; at time of writing, it includes support for UNIX sockets, IPv4, IPv6, and DECnet.
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

# DISTFILES    += CSWxtrans.gspec CSWxtrans.prototype CSWxtrans.depend 
# DISTFILES    += CSWxtransdev.gspec CSWxtransdev.prototype CSWxtransdev.depend 
DISTFILES    += $(call admfiles,CSWxtrans, depend)

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export CFLAGS CXXFLAGS LDFLAGS

TEST_SCRIPTS      = none

GREP = ggrep

include gar/category.mk

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man 

test-none:
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
