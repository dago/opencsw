NAME = Plack-Middleware-MethodOverride
VERSION = 0.10
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DWHEELER

DESCRIPTION = Override REST methods to Plack apps via POST
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

PACKAGES += CSWpm-plack-middleware-methodov
SPKG_DESC_CSWpm-plack-middleware-methodov = Override REST methods to Plack apps via POST
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-plack-middleware-methodov = 1
RUNTIME_DEP_PKGS_CSWpm-plack-middleware-methodov += CSWpm-uri
RUNTIME_DEP_PKGS_CSWpm-plack-middleware-methodov += CSWpm-plack

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
