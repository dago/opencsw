NAME = Text-WideChar-Util
VERSION = 0.06
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Routines for text containing wide characters
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-text-widechar-util
CATALOGNAME_CSWpm-text-widechar-util = pm_text_widechar_util
SPKG_DESC_CSWpm-text-widechar-util = Routines for text containing wide characters
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-text-widechar-util = 1
RUNTIME_DEP_PKGS_CSWpm-text-widechar-util += CSWpm-text-charwidth

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
