NAME = Progress-Any-Output
VERSION = 0.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Assign output to progress indicators
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-progress-any-output
CATALOGNAME_CSWpm-progress-any-output = pm_progress_any_output
SPKG_DESC_CSWpm-progress-any-output = Assign output to progress indicators
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-progress-any-output = 1
RUNTIME_DEP_PKGS_CSWpm-progress-any-output += CSWpm-progress-any

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
