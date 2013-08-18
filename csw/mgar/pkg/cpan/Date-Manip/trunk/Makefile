NAME = Date-Manip
VERSION = 6.40
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SBECK

DESCRIPTION = Date manipulation routines
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-inter

PACKAGES += CSWpm-date-manip
CATALOGNAME_CSWpm-date-manip = pm_date_manip
SPKG_DESC_CSWpm-date-manip = Date manipulation routines
ARCHALL_CSWpm-date-manip = 1
OBSOLETED_BY_CSWpm-date-manip += CSWpmdatemanip
CATALOGNAME_CSWpmdatemanip = pm_datemanip_stub

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
