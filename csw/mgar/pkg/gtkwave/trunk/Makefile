GARNAME = gtkwave
GARVERSION = 3.2.3
CATEGORIES = devel

DESCRIPTION = Brief description
define BLURB
  Long description
endef

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PREREQUISITE_BASE_PKGS = CSWtofrodos

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS) LDFLAGS=-lintl

pre-build-modulated:
	find $(WORKSRC) -type f | xargs -I _ /opt/csw/bin/dos2unix _ _
	@$(MAKECOOKIE)

TEST_SCRIPTS =

include gar/category.mk
