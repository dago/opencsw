NAME = Module-Build-Tiny
VERSION = 0.025
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = LEONT

DESCRIPTION = A tiny replacement for Module::Build
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-module-build-tiny
CATALOGNAME_CSWpm-module-build-tiny = pm_module_build_tiny
SPKG_DESC_CSWpm-module-build-tiny = A tiny replacement for Module::Build
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-module-build-tiny = 1
RUNTIME_DEP_PKGS_CSWpm-module-build-tiny += CSWpm-extutils-installpaths
RUNTIME_DEP_PKGS_CSWpm-module-build-tiny += CSWpm-extutils-helpers
RUNTIME_DEP_PKGS_CSWpm-module-build-tiny += CSWpm-cpan-meta
RUNTIME_DEP_PKGS_CSWpm-module-build-tiny += CSWpm-extutils-config
RUNTIME_DEP_PKGS_CSWpm-module-build-tiny += CSWpm-json-pp

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
