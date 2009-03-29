GARNAME      = libcairo
GARVERSION   = 1.8.6
CATEGORIES   = lib

DESCRIPTION  = The Cairo 2D Graphics Library
define BLURB
Cairo is a 2D graphics library with support for multiple output devices. Currently supported output targets include the X Window System, Quartz, Win32, image buffers, PostScript, PDF, and SVG file output. Experimental backends include OpenGL (through glitz), XCB, BeOS, OS/2, and DirectFB.
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = cairo-$(GARVERSION).tar.gz 

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWlibcairo 		= $(DESCRIPTION)
SPKG_DESC_CSWlibcairodevel 	= $(DESCRIPTION) development package
SPKG_DESC_CSWlibcairodoc 	= $(DESCRIPTION) documentaiton

DISTFILES    += $(call admfiles,CSWlibcairo, )
DISTFILES    += $(call admfiles,CSWlibcairodevel, )
DISTFILES    += $(call admfiles,CSWlibcairodoc, )

PKGFILES_CSWlibcairodevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibcairodevel += /opt/csw/share/doc/libcairo_devel/.*
PKGFILES_CSWlibcairodoc    = $(prefix)/share/gtk-doc.*
PKGFILES_CSWlibcairodoc   += /opt/csw/share/doc/libcairo_doc/.*

REQUIRED_PKGS_CSWlibcairodevel  = CSWlibcairo
REQUIRED_PKGS_CSWlibcairodoc    = 
# REQUIRED_PKGS_CSWlibcairo 	   += CSWlibx11
# REQUIRED_PKGS_CSWlibcairo 	   += CSWfconfig
# REQUIRED_PKGS_CSWlibcairo 	   += CSWftype2
# REQUIRED_PKGS_CSWlibcairo 	   += CSWlibxrender
# REQUIRED_PKGS_CSWlibcairo 	   += CSWpixman
# REQUIRED_PKGS_CSWlibcairo 	   += CSWpng
# REQUIRED_PKGS_CSWlibcairo 	   += CSWzlib

# CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
# CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
# LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-tests --enable-xlib=yes --enable-xlib-xrender=yes --enable-ft=yes --with-x 

post-extract:
	( cd  $(WORKROOTDIR)/build-$(firstword $(MODULATIONS)) ; \
		mv cairo-$(GARVERSION) $(GARNAME)-$(GARVERSION) )
	@$(MAKECOOKIE)

include gar/category.mk


