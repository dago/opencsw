GARNAME = libXdmcp
GARVERSION = 1.0.2
CATEGORIES = lib

DESCRIPTION = X11 authorisation library
define BLURB
This package provides the main interface to the X11 display manager control protocol library, which allows for remote logins to display managers. 
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST = $(GARNAME)-$(GARVERSION).tar.gz

DISTFILES    += CSWlibXdmcp.gspec CSWlibXdmcp.prototype CSWlibXdmcp.depend 
DISTFILES    += CSWlibXdmcpdev.gspec CSWlibXdmcpdev.prototype CSWlibXdmcpdev.depend 
# DISTFILES    += $(call admfiles,CSWlibXdmcp, depend)

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
