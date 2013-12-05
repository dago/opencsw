NAME = Class-Std
VERSION = 0.011
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DCONWAY

DESCRIPTION = Support for creating standard "inside-out" classes
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the Perl license

PACKAGES += CSWpm-class-std
CATALOGNAME_CSWpm-class-std = pm_class_std
SPKG_DESC_CSWpm-class-std = Support for creating standard "inside-out" classes
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-class-std = 1
OBSOLETED_BY_CSWpm-class-std += CSWpmclassstd
CATALOGNAME_CSWpmclassstd = pm_classstd_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
