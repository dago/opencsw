NAME = Package-DeprecationManager
VERSION = 0.13
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = Manage deprecation warnings for your distribution
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-fatal
BUILD_DEP_PKGS += CSWpm-test-requires

PACKAGES += CSWpm-package-deprecationmanager
CATALOGNAME_CSWpm-package-deprecationmanager = pm_package_deprecationmanager
SPKG_DESC_CSWpm-package-deprecationmanager = Manage deprecation warnings for your distribution
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-package-deprecationmanager = 1
RUNTIME_DEP_PKGS_CSWpm-package-deprecationmanager += CSWpm-params-util
RUNTIME_DEP_PKGS_CSWpm-package-deprecationmanager += CSWpm-list-moreutils
RUNTIME_DEP_PKGS_CSWpm-package-deprecationmanager += CSWpm-sub-install

include gar/category.mk
