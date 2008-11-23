GARNAME = libxrender
GARVERSION = 0.9.4
CATEGORIES = lib

DESCRIPTION = X Render extension library
define BLURB
The X Rendering Extension (Render) introduces digital image composition as the foundation of a new rendering model within the X Window System. Rendering geometric figures is accomplished by client-side tesselation into either triangles or trapezoids.
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = libXrender-$(GARVERSION).tar.gz
PKGDIST = libXrender-$(GARVERSION).tar.gz

DISTFILES    += CSWlibxrender.gspec CSWlibxrender.prototype CSWlibxrender.depend 
DISTFILES    += CSWrenderdev.gspec CSWrenderdev.prototype CSWrenderdev.depend 
# DISTFILES    += $(call admfiles,CSWxrender, depend)

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

post-extract:
	( mv $(WORKDIR)/libXrender-$(GARVERSION) $(WORKDIR)/$(GARNAME)-$(GARVERSION) )
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
