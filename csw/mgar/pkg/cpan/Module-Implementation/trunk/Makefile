NAME = Module-Implementation
VERSION = 0.06
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = Loads one of several alternate underlying implementations for a module
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-fatal
BUILD_DEP_PKGS += CSWpm-test-requires

PACKAGES += CSWpm-module-implementation
CATALOGNAME_CSWpm-module-implementation = pm_module_implementation
SPKG_DESC_CSWpm-module-implementation = Loads one of several alternate underlying implementations for a module
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-module-implementation = 1
RUNTIME_DEP_PKGS_CSWpm-module-implementation += CSWpm-try-tiny
RUNTIME_DEP_PKGS_CSWpm-module-implementation += CSWpm-module-runtime

include gar/category.mk
