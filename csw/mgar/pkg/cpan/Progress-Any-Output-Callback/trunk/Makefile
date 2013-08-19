NAME = Progress-Any-Output-Callback
VERSION = 0.01
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Propagate progress update to a callback function
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-progress-any-output-call
SPKG_DESC_CSWpm-progress-any-output-call = Propagate progress update to a callback function
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-progress-any-output-call = 1
RUNTIME_DEP_PKGS_CSWpm-progress-any-output-call += CSWpm-progress-any

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
