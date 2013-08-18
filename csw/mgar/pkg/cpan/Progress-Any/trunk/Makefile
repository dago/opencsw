NAME = Progress-Any
VERSION = 0.09
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Record progress to any output
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-progress-any
CATALOGNAME_CSWpm-progress-any = pm_progress_any
SPKG_DESC_CSWpm-progress-any = Record progress to any output
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-progress-any = 1
RUNTIME_DEP_PKGS_CSWpm-progress-any += CSWpm-time-duration

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
