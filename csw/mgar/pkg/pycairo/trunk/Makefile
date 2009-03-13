GARNAME      = pycairo
GARVERSION   = 1.8.0
CATEGORIES   = lib

DESCRIPTION  = Python Bindings for Cairo
define BLURB
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST       = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWpycairo CSWpycairo-devel

SPKG_DESC_CSWpycairo       = $(DESCRIPTION)
SPKG_DESC_CSWpycairo-devel = $(DESCRIPTION) development package

PKGFILES_CSWpycairo-devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWpycairo-devel += $(prefix)/include/.*
PKGFILES_CSWpycairo-devel += $(prefix)/lib/.*\.a
PKGFILES_CSWpycairo-devel += $(prefix)/lib/pkgconfig/.*

REQUIRED_PKGS_CSWpycairo-devel = CSWpycairo

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


