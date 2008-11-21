GARNAME = libX11
GARVERSION = 1.1.5
CATEGORIES = lib

DESCRIPTION = X11 client-side library
define BLURB
This package provides a client interface to the X Window System, otherwise known as 'Xlib'. It provides a complete API for the basic functions of the window system. 
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

DISTFILES    += CSWlibX11.gspec CSWlibX11.prototype CSWlibX11.depend 
DISTFILES    += CSWlibX11dev.gspec CSWlibX11dev.prototype CSWlibX11dev.depend 
# DISTFILES    += $(call admfiles,CSWlibX11, depend)

include ../category.mk

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION -D__solaris__
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export CFLAGS CXXFLAGS LDFLAGS

TEST_SCRIPTS      = none

GREP = ggrep

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man 

test-none:
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
