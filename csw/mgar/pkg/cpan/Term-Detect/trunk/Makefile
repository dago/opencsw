NAME = Term-Detect
VERSION = 0.06
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Detect running under terminal (and get terminal emulator information)
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-term-detect
CATALOGNAME_CSWpm-term-detect = pm_term_detect
SPKG_DESC_CSWpm-term-detect = Detect running under terminal (and get terminal emulator information)
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-term-detect = 1
RUNTIME_DEP_PKGS_CSWpm-term-detect += CSWpm-experimental
RUNTIME_DEP_PKGS_CSWpm-term-detect += CSWpm-sharyanto-proc-util

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
