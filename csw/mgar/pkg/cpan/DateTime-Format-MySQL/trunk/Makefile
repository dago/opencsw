NAME = DateTime-Format-MySQL
VERSION = 0.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = Parse and format MySQL dates and times
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-datetime-format-mysql
CATALOGNAME_CSWpm-datetime-format-mysql = pm_datetime_format_mysql
SPKG_DESC_CSWpm-datetime-format-mysql = Parse and format MySQL dates and times
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-datetime-format-mysql = 1
RUNTIME_DEP_PKGS_CSWpm-datetime-format-mysql += CSWpm-datetime
RUNTIME_DEP_PKGS_CSWpm-datetime-format-mysql += CSWpm-datetime-format-builder

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
