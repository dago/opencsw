NAME = Progress-Any-Output-TermMessage
VERSION = 0.01
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Output progress to terminal as simple message
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-progress-any-output-termms
SPKG_DESC_CSWpm-progress-any-output-termms = Output progress to terminal as simple message
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-progress-any-output-termms = 1
RUNTIME_DEP_PKGS_CSWpm-progress-any-output-termms += CSWpm-progress-any

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
