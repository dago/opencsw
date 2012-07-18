NAME = DBIx-Connector
VERSION = 0.52
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DWHEELER

DESCRIPTION = Fast, safe DBI connection and transaction management
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-test-mockmodule

PACKAGES += CSWpm-dbix-connector
CATALOGNAME_CSWpm-dbix-connector = pm_dbix_connector
SPKG_DESC_CSWpm-dbix-connector = Fast, safe DBI connection and transaction management
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-dbix-connector = 1
RUNTIME_DEP_PKGS_CSWpm-dbix-connector += CSWpm-dbi

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
