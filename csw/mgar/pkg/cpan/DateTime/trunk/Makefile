NAME = DateTime
VERSION = 0.76
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = A date and time object
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-fatal

PACKAGES += CSWpm-datetime
CATALOGNAME_CSWpm-datetime = pm_datetime
SPKG_DESC_CSWpm-datetime = A date and time object
RUNTIME_DEP_PKGS_CSWpm-datetime += CSWpm-params-validate
RUNTIME_DEP_PKGS_CSWpm-datetime += CSWpm-datetime-locale
RUNTIME_DEP_PKGS_CSWpm-datetime += CSWpm-math-round
RUNTIME_DEP_PKGS_CSWpm-datetime += CSWpm-datetime-timezone
OBSOLETED_BY_CSWpm-datetime += CSWpmdatetime
CATALOGNAME_CSWpmdatetime = pm_datetime_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
