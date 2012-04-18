NAME = Parse-CPAN-Meta
VERSION = 1.4404
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DAGOLDEN

DESCRIPTION = Parse META.yml and META.json CPAN metadata files
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES += CSWpm-parse-cpan-meta
CATALOGNAME_CSWpm-parse-cpan-meta = pm_parse_cpan_meta
SPKG_DESC_CSWpm-parse-cpan-meta = Parse META.yml and META.json CPAN metadata files
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-parse-cpan-meta = 1
RUNTIME_DEP_PKGS_CSWpm-parse-cpan-meta += CSWpm-cpan-meta-yaml
RUNTIME_DEP_PKGS_CSWpm-parse-cpan-meta += CSWpm-json-pp

# This is ok, we are overwriting the default Perl module
CHECKPKG_OVERRIDES_CSWpm-parse-cpan-meta += file-collision|/opt/csw/share/man/man3/Parse::CPAN::Meta.3perl|CSWperldoc|CSWpm-parse-cpan-meta

include gar/category.mk
