NAME = Data-ICal
VERSION = 0.16
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ALEXMV

DESCRIPTION = Generates iCalendar (RFC 2445) calendar files
define BLURB
   Generates iCalendar (RFC 2445) calendar files
endef

DISTFILES += COPYING

PACKAGES = CSWpmdataical
CATALOGNAME = pm_dataical
ARCHALL = 1

PATCHFILES += 0001-Replace-crap-installer-with-something-more-standard.patch

RUNTIME_DEP_PKGS += CSWpmclsaccessor CSWpmclassretval CSWpmtextvfileasdata

include gar/category.mk
