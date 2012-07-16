NAME = Plack-Middleware-Status
VERSION = 1.101150
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PDONELAN

DESCRIPTION = Plack Middleware for mapping urls to status code-driven responses
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-libwww-perl
BUILD_DEP_PKGS += CSWpm-plack

PACKAGES += CSWpm-plack-middleware-status
CATALOGNAME_CSWpm-plack-middleware-status = pm_plack_middleware_status
SPKG_DESC_CSWpm-plack-middleware-status = Plack Middleware for mapping urls to status code-driven responses
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-plack-middleware-status = 1
RUNTIME_DEP_PKGS_CSWpm-plack-middleware-status += CSWpm-libwww-perl
RUNTIME_DEP_PKGS_CSWpm-plack-middleware-status += CSWpm-plack

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
