GARNAME      = pixman
GARVERSION   = 0.12.0
CATEGORIES   = lib

DESCRIPTION  = The pixel-manipulation library for X and cairo
define BLURB
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST       = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_DESC_CSWpixman 		= $(DESCRIPTION)
SPKG_DESC_CSWpixmandevel  	= $(DESCRIPTION) development package

DISTFILES    += $(call admfiles,CSWpixman, )
DISTFILES    += $(call admfiles,CSWpixmandevel, )

PKGFILES_CSWpixmandevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWpixmandevel += $(prefix)/include/.*
PKGFILES_CSWpixmandevel += $(prefix)/lib/.*\.a
PKGFILES_CSWpixmandevel += $(prefix)/lib/pkgconfig/.*

REQUIRED_PKGS_CSWpixmandevel = CSWpixman
#REQUIRED_PKGS_CSWpixman 	 = CSWlibx11

CFLAGS       += -xlibmil -errtags=yes -erroff=E_EMPTY_DECLARATION
CXXFLAGS     += -xlibmil -xlibmopt -features=tmplife -norunpath
LDFLAGS      += -L/opt/csw/lib -R/opt/csw/lib

CONFIGURE_ARGS = --prefix=/opt/csw --mandir=/opt/csw/share/man --enable-gtk

include gar/category.mk


