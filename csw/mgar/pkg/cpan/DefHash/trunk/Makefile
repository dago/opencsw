NAME = DefHash
VERSION = 1.0.3
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Define things according to a specification, using hashes
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-defhash
CATALOGNAME_CSWpm-defhash = pm_defhash
SPKG_DESC_CSWpm-defhash = Define things according to a specification, using hashes
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-defhash = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
