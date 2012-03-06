NAME = Tie-DBI
VERSION = 1.05
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TODDR

DESCRIPTION = Tie hashes to DBI relational databases
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-dbd-sqlite

PACKAGES += CSWpm-tie-dbi
CATALOGNAME_CSWpm-tie-dbi = pm_tie_dbi
SPKG_DESC_CSWpm-tie-dbi = Tie hashes to DBI relational databases
ARCHALL_CSWpm-tie-dbi = 1
RUNTIME_DEP_PKGS_CSWpm-tie-dbi += CSWpm-dbi
RUNTIME_DEP_PKGS_CSWpm-tie-dbi += CSWpm-dbd-sqlite

include gar/category.mk
