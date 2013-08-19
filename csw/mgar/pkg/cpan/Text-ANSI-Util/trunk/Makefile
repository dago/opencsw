NAME = Text-ANSI-Util
VERSION = 0.10
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Routines for text containing ANSI escape codes
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build
BUILD_DEP_PKGS += CSWpm-data-dump

PACKAGES += CSWpm-text-ansi-util
CATALOGNAME_CSWpm-text-ansi-util = pm_text_ansi_util
SPKG_DESC_CSWpm-text-ansi-util = Routines for text containing ANSI escape codes
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-text-ansi-util = 1
RUNTIME_DEP_PKGS_CSWpm-text-ansi-util += CSWpm-text-widechar-util
RUNTIME_DEP_PKGS_CSWpm-text-ansi-util += CSWpm-text-charwidth

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
