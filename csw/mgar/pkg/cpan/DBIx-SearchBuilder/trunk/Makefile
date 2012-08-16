NAME = DBIx-SearchBuilder
VERSION = 1.62
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RUZ

DESCRIPTION = Encapsulate SQL queries and rows in simple perl objects
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-dbd-sqlite

PACKAGES += CSWpm-dbix-searchbuilder
CATALOGNAME_CSWpm-dbix-searchbuilder = pm_dbix_searchbuilder
SPKG_DESC_CSWpm-dbix-searchbuilder = Encapsulate SQL queries and rows in simple perl objects
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-dbix-searchbuilder = 1
RUNTIME_DEP_PKGS_CSWpm-dbix-searchbuilder += CSWpm-dbi
RUNTIME_DEP_PKGS_CSWpm-dbix-searchbuilder += CSWpm-clone
RUNTIME_DEP_PKGS_CSWpm-dbix-searchbuilder += CSWpm-want
RUNTIME_DEP_PKGS_CSWpm-dbix-searchbuilder += CSWpm-dbix-dbschema
RUNTIME_DEP_PKGS_CSWpm-dbix-searchbuilder += CSWpm-cache-simple-timedexpiry
RUNTIME_DEP_PKGS_CSWpm-dbix-searchbuilder += CSWpm-class-accessor
RUNTIME_DEP_PKGS_CSWpm-dbix-searchbuilder += CSWpm-class-returnvalue
OBSOLETED_BY_CSWpm-dbix-searchbuilder += CSWpmdbixsrchbuilder
CATALOGNAME_CSWpmdbixsrchbuilder = pm_dbixsrchbuilder_stub

include gar/category.mk
