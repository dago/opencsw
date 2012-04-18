NAME = Dist-CheckConflicts
VERSION = 0.02
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DOY

DESCRIPTION = Declare version conflicts for your dist
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-fatal

PACKAGES += CSWpm-dist-checkconflicts
CATALOGNAME_CSWpm-dist-checkconflicts = pm_dist_checkconflicts
SPKG_DESC_CSWpm-dist-checkconflicts = Declare version conflicts for your dist
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-dist-checkconflicts = 1
RUNTIME_DEP_PKGS_CSWpm-dist-checkconflicts += CSWpm-sub-exporter
RUNTIME_DEP_PKGS_CSWpm-dist-checkconflicts += CSWpm-list-moreutils

include gar/category.mk
