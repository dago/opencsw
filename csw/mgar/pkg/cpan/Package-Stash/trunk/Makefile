NAME = Package-Stash
VERSION = 0.33
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DOY

DESCRIPTION = Routines for manipulating stashes
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-fatal
BUILD_DEP_PKGS += CSWpm-test-requires

PACKAGES += CSWpm-package-stash
CATALOGNAME_CSWpm-package-stash = pm_package_stash
SPKG_DESC_CSWpm-package-stash = Routines for manipulating stashes
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-package-stash = 1
RUNTIME_DEP_PKGS_CSWpm-package-stash += CSWpm-dist-checkconflicts
RUNTIME_DEP_PKGS_CSWpm-package-stash += CSWpm-package-deprecationmanager

include gar/category.mk
