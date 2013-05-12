NAME = Data-ICal
VERSION = 0.20
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TSIBLEY

DESCRIPTION = Generates iCalendar (RFC 2445) calendar files
define BLURB
endef

DISTFILES += COPYING

PACKAGES = CSWpm-data-ical
CATALOGNAME = pm_data_ical
SPKG_DESC_CSWpm-data-ical = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-data-ical = CSWpmdataical
CATALOGNAME_CSWpmdataical = pm_dataical

ARCHALL = 1

PATCHFILES += 0001-Replace-crap-installer-with-something-more-standard.patch

BUILD_DEP_PKGS += CSWpm-test-longstring
BUILD_DEP_PKGS += CSWpm-test-nowarnings
BUILD_DEP_PKGS += CSWpmtestwarn

RUNTIME_DEP_PKGS += CSWpm-class-accessor
RUNTIME_DEP_PKGS += CSWpm-class-returnvalue
RUNTIME_DEP_PKGS += CSWpm-text-vfile-asdata

include gar/category.mk
