NAME      = rcairo
VERSION   = 1.8.0
CATEGORIES   = lib
GARTYPE = v2

DESCRIPTION  = Ruby Bindings for Cairo
define BLURB
endef

MASTER_SITES  = http://www.cairographics.org/releases/
DISTFILES     = $(NAME)-$(VERSION).tar.gz
PKGDIST       = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
PACKAGES = CSWrcairo CSWrcairo-devel

SPKG_DESC_CSWrcairo 		= $(DESCRIPTION)
SPKG_DESC_CSWrcairo-devel  	= $(DESCRIPTION) development package

PKGFILES_CSWrcairo-devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWrcairo-devel += $(prefix)/include/.*
PKGFILES_CSWrcairo-devel += $(prefix)/lib/.*\.a
PKGFILES_CSWrcairo-devel += $(prefix)/lib/pkgconfig/.*

RUNTIME_DEP_PKGS_CSWrcairo-devel = CSWrcairo

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk


