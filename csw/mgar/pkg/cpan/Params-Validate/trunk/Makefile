NAME = Params-Validate
VERSION = 1.06
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = Validate method/function parameters
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-implementation
BUILD_DEP_PKGS += CSWpm-test-fatal

# The Module::Build from CSWperl is too old
BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-params-validate
CATALOGNAME_CSWpm-params-validate = pm_params_validate
SPKG_DESC_CSWpm-params-validate = Validate method/function parameters
RUNTIME_DEP_PKGS_CSWpm-params-validate += CSWpm-module-implementation
OBSOLETED_BY_CSWpm-params-validate += CSWpmparamsvalidate
CATALOGNAME_CSWpmparamsvalidate = pm_paramsvalidate_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
