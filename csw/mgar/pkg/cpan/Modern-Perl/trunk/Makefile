NAME = Modern-Perl
VERSION = 1.20120521
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CHROMATIC

DESCRIPTION = Enable all of the features of Modern Perl with one import
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-modern-perl
CATALOGNAME_CSWpm-modern-perl = pm_modern_perl
SPKG_DESC_CSWpm-modern-perl = Enable all of the features of Modern Perl with one import
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-modern-perl = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
