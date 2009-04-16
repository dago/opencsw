GARNAME = pango-libthai
GARVERSION = 0.1.4
CATEGORIES = lib

DESCRIPTION = Pango bindings for Thai language support
define BLURB
endef

SF_PROJ = libthai
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=34448
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWlibthai

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWpango-libthai
CATALOGNAME = pango_libthai

include gar/category.mk
