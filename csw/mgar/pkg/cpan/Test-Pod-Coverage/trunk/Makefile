NAME = Test-Pod-Coverage
VERSION = 1.08
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PETDANCE

DESCRIPTION = Check for pod coverage in your distribution
define BLURB
endef

BUILD_DEP_PKGS = CSWpmtstbldrtester CSWpmpodcoverage
RUNTIME_DEP_PKGS = CSWpmpodsimple CSWpmiostringy

DISTFILES = COPYING

PACKAGES = CSWpmtestpodcoverage
CATALOGNAME = pm_testpodcoverage

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWpmtestpodcoverage += surplus-dependency|CSWpmpodsimple
CHECKPKG_OVERRIDES_CSWpmtestpodcoverage += surplus-dependency|CSWpmiostringy

include gar/category.mk
