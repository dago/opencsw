NAME = Term-ProgressBar-Color
VERSION = 0.00
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHARYANTO

DESCRIPTION = Provide a progress meter on a standard terminal (with color)
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-module-build

PACKAGES += CSWpm-term-progressbar-color
CATALOGNAME_CSWpm-term-progressbar-color = pm_term_progressbar_color
SPKG_DESC_CSWpm-term-progressbar-color = Provide a progress meter on a standard terminal (with color)
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-term-progressbar-color = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
