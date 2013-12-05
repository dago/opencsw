NAME = Class-Std-Fast
VERSION = v0.0.8
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ACID

DESCRIPTION = Faster but less secure than Class::Std
define BLURB
endef

# MODDIST = Class-Std-Fast-v0.0.8.tar.gz

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

PACKAGES += CSWpm-class-std-fast
CATALOGNAME_CSWpm-class-std-fast = pm_class_std_fast
SPKG_DESC_CSWpm-class-std-fast = Faster but less secure than Class::Std
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-class-std-fast = 1
RUNTIME_DEP_PKGS_CSWpm-class-std-fast += CSWpm-class-std

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
