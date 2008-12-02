GARNAME      = pixman
GARVERSION   = 0.12.0
CATEGORIES   = lib

DESCRIPTION  = The pixel-manipulation library for X and cairo
define BLURB
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST       = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES    += CSWpixman.gspec CSWpixman.prototype CSWpixman.depend 
DISTFILES    += CSWpixmandev.gspec CSWpixmandev.prototype CSWpixmandev.depend
# DISTFILES    += $(call admfiles,CSWpixman, depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export CFLAGS CXXFLAGS LDFLAGS

GREP = ggrep

include gar/category.mk

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man --enable-gtk

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )


