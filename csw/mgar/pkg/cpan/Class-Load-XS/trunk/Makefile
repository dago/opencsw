NAME = Class-Load-XS
VERSION = 0.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = XS implementation of parts of Class::Load
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

# This is also in CSWperl, but we need a newer version
BUILD_DEP_PKGS += CSWpm-module-build

BUILD_DEP_PKGS += CSWpm-module-implementation
BUILD_DEP_PKGS += CSWpm-test-fatal
BUILD_DEP_PKGS += CSWpm-class-load
BUILD_DEP_PKGS += CSWpm-test-requires

PACKAGES += CSWpm-class-load-xs
CATALOGNAME_CSWpm-class-load-xs = pm_class_load_xs
SPKG_DESC_CSWpm-class-load-xs = XS implementation of parts of Class::Load
RUNTIME_DEP_PKGS_CSWpm-class-load-xs += CSWpm-class-load

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
