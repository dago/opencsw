NAME = Rinci
VERSION = 1.1.35
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Language-neutral metadata for your code
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-rinci
CATALOGNAME_CSWpm-rinci = pm_rinci
SPKG_DESC_CSWpm-rinci = Language-neutral metadata for your code
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-rinci = 1
RUNTIME_DEP_PKGS_CSWpm-rinci += CSWpm-defhash

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
