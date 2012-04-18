NAME = CPAN-Meta
VERSION = 2.120921
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DAGOLDEN

DESCRIPTION = The distribution metadata for a CPAN dist
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-cpan-meta
CATALOGNAME_CSWpm-cpan-meta = pm_cpan_meta
SPKG_DESC_CSWpm-cpan-meta = The distribution metadata for a CPAN dist
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-cpan-meta = 1
RUNTIME_DEP_PKGS_CSWpm-cpan-meta += CSWpm-cpan-meta-yaml
RUNTIME_DEP_PKGS_CSWpm-cpan-meta += CSWpm-json-pp
RUNTIME_DEP_PKGS_CSWpm-cpan-meta += CSWpm-cpan-meta-requirements

include gar/category.mk
