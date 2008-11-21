GARNAME = libxcb
GARVERSION = 1.1
CATEGORIES = lib

DESCRIPTION = The XCB library
define BLURB
The XCB library provides an interface to the X Window System protocol, designed to replace the Xlib interface
endef

MASTER_SITES =http://xcb.freedesktop.org/dist/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

DISTFILES    += CSWlibxcb.gspec CSWlibxcb.prototype CSWlibxcb.depend 
DISTFILES    += CSWlibxcbdev.gspec CSWlibxcbdev.prototype CSWlibxcbdev.depend 
# DISTFILES    += $(call admfiles,CSWlibxcb, depend)

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
