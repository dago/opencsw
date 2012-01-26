NAME = pango-libthai
VERSION = 0.1.4
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Pango bindings for Thai language support
define BLURB
endef

SF_PROJ = libthai
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=34448
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS = CSWlibthai

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

PACKAGES = CSWpango-libthai
CATALOGNAME = pango_libthai

include gar/category.mk
