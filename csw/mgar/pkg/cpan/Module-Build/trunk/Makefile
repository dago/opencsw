NAME = Module-Build
VERSION = 0.40
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = LEONT

DESCRIPTION = Build and install Perl modules
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-cpan-meta-yaml

PACKAGES += CSWpm-module-build
CATALOGNAME_CSWpm-module-build = pm_module_build
SPKG_DESC_CSWpm-module-build = Build and install Perl modules
ARCHALL_CSWpm-module-build = 1
RUNTIME_DEP_PKGS_CSWpm-module-build += CSWpm-perl-ostype
RUNTIME_DEP_PKGS_CSWpm-module-build += CSWpm-cpan-meta
RUNTIME_DEP_PKGS_CSWpm-module-build += CSWpm-module-metadata

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

# We have a ton of collisions with CSWperl, this is intended.
CHECKPKG_OVERRIDES_CSWpm-module-build += file-collision

include gar/category.mk
