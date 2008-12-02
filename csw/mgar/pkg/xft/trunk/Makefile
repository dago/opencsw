GARNAME = libxft2
GARVERSION = 2.1.13
CATEGORIES = lib

DESCRIPTION = FreeType-based font drawing library for X
define BLURB
Xft provides a client-side font API for X applications, making the FreeType font rasterizer available to X clients. Fontconfig is used for font specification resolution. Where available, the RENDER extension handles glyph drawing; otherwise, the core X protocol is used.
endef

MASTER_SITES =http://xorg.freedesktop.org/releases/individual/lib/
DISTFILES = libXft-$(GARVERSION).tar.gz
PKGDIST = libXft-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES    += CSWlibxft2.gspec CSWlibxft2.prototype CSWlibxft2.depend 
DISTFILES    += CSWlibxft2dev.gspec CSWlibxft2dev.prototype CSWlibxft2dev.depend 
# DISTFILES    += $(call admfiles,CSWlibxft2, depend)

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
	( mv $(WORKDIR)/libXft-$(GARVERSION) $(WORKDIR)/$(GARNAME)-$(GARVERSION) )
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
