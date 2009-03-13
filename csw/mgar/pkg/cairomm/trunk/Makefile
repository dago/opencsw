GARNAME      = cairomm
GARVERSION   = 1.8.0
CATEGORIES   = lib

DESCRIPTION  = C++ bindings for Cairo
define BLURB
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = $(GARNAME)-$(GARVERSION).tar.gz
PKGDIST       = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWcairomm CSWcairomm-devel
SPKG_DESC_CSWcairomm 		= $(DESCRIPTION)
SPKG_DESC_CSWcairomm-devel 	= $(DESCRIPTION) development package

PKGFILES_CSWcairomm-devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWcairomm-devel += $(prefix)/include/.*
PKGFILES_CSWcairomm-devel += $(prefix)/lib/.*\.a
PKGFILES_CSWcairomm-devel += $(prefix)/lib/pkgconfig/.*

REQUIRED_PKGS_CSWcairomm-devel = CSWcairomm

CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk


