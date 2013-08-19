NAME = Progress-Any-Output-TermProgressBarColor
VERSION = 0.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Output progress to terminal as color bar
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-progress-any-output-termpb
SPKG_DESC_CSWpm-progress-any-output-termpb = Output progress to terminal as color bar
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-progress-any-output-termpb = 1
RUNTIME_DEP_PKGS_CSWpm-progress-any-output-termpb += CSWpm-text-ansi-util
RUNTIME_DEP_PKGS_CSWpm-progress-any-output-termpb += CSWpm-color-ansi-util
RUNTIME_DEP_PKGS_CSWpm-progress-any-output-termpb += CSWpm-term-size
RUNTIME_DEP_PKGS_CSWpm-progress-any-output-termpb += CSWpm-progress-any

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
