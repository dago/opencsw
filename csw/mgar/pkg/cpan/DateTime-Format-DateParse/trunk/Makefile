NAME = DateTime-Format-DateParse
VERSION = 0.05
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JHOBLITT

DESCRIPTION = Parses Date::Parse compatible formats
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-datetime-format-dateparse
CATALOGNAME_CSWpm-datetime-format-dateparse = pm_datetime_format_dateparse
SPKG_DESC_CSWpm-datetime-format-dateparse = Parses Date::Parse compatible formats
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-datetime-format-dateparse = 1
RUNTIME_DEP_PKGS_CSWpm-datetime-format-dateparse += CSWpm-datetime
RUNTIME_DEP_PKGS_CSWpm-datetime-format-dateparse += CSWpm-date-parse
RUNTIME_DEP_PKGS_CSWpm-datetime-format-dateparse += CSWpm-datetime-timezone

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
