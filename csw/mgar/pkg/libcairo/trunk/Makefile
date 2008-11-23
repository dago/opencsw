GARNAME      = libcairo
GARVERSION   = 1.8.2
CATEGORIES   = libs

DESCRIPTION  = The Cairo 2D Graphics Library
define BLURB
Cairo is a 2D graphics library with support for multiple output devices. Currently supported output targets include the X Window System, Quartz, Win32, image buffers, PostScript, PDF, and SVG file output. Experimental backends include OpenGL (through glitz), XCB, BeOS, OS/2, and DirectFB.
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = cairo-$(GARVERSION).tar.gz 
PKGDIST       = cairo-$(GARVERSION).tar.gz 
DISTFILES    += CSWlibcairo.gspec CSWlibcairo.prototype CSWlibcairo.depend 
DISTFILES    += CSWlibcairodev.gspec CSWlibcairodev.prototype CSWlibcairodev.depend 
DISTFILES    += CSWlibcairodoc.gspec CSWlibcairodoc.prototype CSWlibcairodoc.depend 
# DISTFILES    += $(call admfiles,CSWlibcairo, depend)

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

export CFLAGS CXXFLAGS LDFLAGS

GREP = ggrep

include gar/category.mk

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man --disable-tests --enable-xlib=yes --enable-xlib-xrender=yes --enable-ft=yes --with-x 

post-extract:
	( mv $(WORKDIR)/cairo-$(GARVERSION) $(WORKDIR)/$(GARNAME)-$(GARVERSION) )
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

