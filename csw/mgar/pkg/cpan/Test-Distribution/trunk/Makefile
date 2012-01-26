NAME = Test-Distribution
VERSION = 2.00
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SRSHAH

DESCRIPTION = Perform tests on all modules of a distribution
define BLURB
endef

DISTFILES = CSWpmtestdistribution.gspec

BUILD_DEP_PKGS = CSWpmmodulebuild

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
