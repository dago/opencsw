NAME = DateTime-Locale
VERSION = 0.45
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = Localization support for DateTime.pm
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-datetime-locale
CATALOGNAME_CSWpm-datetime-locale = pm_datetime_locale
SPKG_DESC_CSWpm-datetime-locale = Localization support for DateTime.pm
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-datetime-locale = 1
RUNTIME_DEP_PKGS_CSWpm-datetime-locale += CSWpm-params-validate
RUNTIME_DEP_PKGS_CSWpm-datetime-locale += CSWpm-list-moreutils
OBSOLETED_BY_CSWpm-datetime-locale += CSWpmdatetimelocale
CATALOGNAME_CSWpmdatetimelocale = pm_datetimelocale_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
