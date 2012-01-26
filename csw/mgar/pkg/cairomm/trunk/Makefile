NAME      = cairomm
VERSION   = 1.8.0
CATEGORIES   = lib
GARTYPE = v2

DESCRIPTION  = C++ bindings for Cairo
define BLURB
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = $(NAME)-$(VERSION).tar.gz
PKGDIST       = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWcairomm CSWcairomm-devel
SPKG_DESC_CSWcairomm 		= $(DESCRIPTION)
SPKG_DESC_CSWcairomm-devel 	= $(DESCRIPTION) development package

PKGFILES_CSWcairomm-devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWcairomm-devel += $(prefix)/include/.*
PKGFILES_CSWcairomm-devel += $(prefix)/lib/.*\.a
PKGFILES_CSWcairomm-devel += $(prefix)/lib/pkgconfig/.*

RUNTIME_DEP_PKGS_CSWcairomm-devel = CSWcairomm

CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk


