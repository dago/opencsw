NAME = DBD-ODBC
VERSION = 1.37
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MJEVANS

DESCRIPTION = ODBC DBD for Perl DBI
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license, please see for details http://dev.perl.org/licenses/

BUILD_DEP_PKGS += CSWpm-dbi

PACKAGES += CSWpm-dbd-odbc
SPKG_DESC_CSWpm-dbd-odbc = ODBC DBD for Perl DBI
RUNTIME_DEP_PKGS_CSWpm-dbd-odbc += CSWpm-dbi
RUNTIME_DEP_PKGS_CSWpm-dbd-odbc += CSWlibodbc2

# This is the changelog
CHECKPKG_OVERRIDES_CSWpm-dbd-odbc += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/DBD/ODBC/Changes.pm

# Strip unknown options
CONFIGURE_ARGS =

include gar/category.mk
