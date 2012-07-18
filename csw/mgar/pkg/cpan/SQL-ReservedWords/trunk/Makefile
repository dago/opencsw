NAME = SQL-ReservedWords
VERSION = 0.7
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CHANSEN

DESCRIPTION = Reserved SQL words by ANSI/ISO
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES += CSWpm-sql-reservedwords
CATALOGNAME_CSWpm-sql-reservedwords = pm_sql_reservedwords
SPKG_DESC_CSWpm-sql-reservedwords = Reserved SQL words by ANSI/ISO
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-sql-reservedwords = 1
RUNTIME_DEP_PKGS_CSWpm-sql-reservedwords += CSWpm-sub-exporter

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
