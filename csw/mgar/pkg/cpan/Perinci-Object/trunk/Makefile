NAME = Perinci-Object
VERSION = 0.11
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Object-oriented interface for Rinci metadata
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-exception
BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-perinci-object
CATALOGNAME_CSWpm-perinci-object = pm_perinci_object
SPKG_DESC_CSWpm-perinci-object = Object-oriented interface for Rinci metadata
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-perinci-object = 1
RUNTIME_DEP_PKGS_CSWpm-perinci-object += CSWpm-rinci
RUNTIME_DEP_PKGS_CSWpm-perinci-object += CSWpm-sharyanto-string-util

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
