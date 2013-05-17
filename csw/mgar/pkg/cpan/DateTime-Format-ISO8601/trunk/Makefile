NAME = DateTime-Format-ISO8601
VERSION = 0.08
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JHOBLITT

DESCRIPTION = Parses ISO8601 formats
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-datetime-format-iso8601
CATALOGNAME_CSWpm-datetime-format-iso8601 = pm_datetime_format_iso8601
SPKG_DESC_CSWpm-datetime-format-iso8601 = Parses ISO8601 formats
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-datetime-format-iso8601 = 1
RUNTIME_DEP_PKGS_CSWpm-datetime-format-iso8601 += CSWpm-datetime
RUNTIME_DEP_PKGS_CSWpm-datetime-format-iso8601 += CSWpm-datetime-format-builder

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
