NAME = Color-ANSI-Util
VERSION = 0.07
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Routines for dealing with ANSI colors
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-color-ansi-util
CATALOGNAME_CSWpm-color-ansi-util = pm_color_ansi_util
SPKG_DESC_CSWpm-color-ansi-util = Routines for dealing with ANSI colors
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-color-ansi-util = 1
RUNTIME_DEP_PKGS_CSWpm-color-ansi-util += CSWpm-term-detect

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
