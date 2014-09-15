NAME = Router-Simple
VERSION = 0.15
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TOKUHIROM

DESCRIPTION = Simple HTTP router
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-router-simple
CATALOGNAME_CSWpm-router-simple = pm_router_simple
SPKG_DESC_CSWpm-router-simple = Simple HTTP router
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-router-simple = 1
RUNTIME_DEP_PKGS_CSWpm-router-simple += CSWpm-class-accessor-lite

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
