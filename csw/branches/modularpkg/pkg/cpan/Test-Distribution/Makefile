GARNAME = Test-Distribution
GARVERSION = 2.00
CATEGORIES = cpan
AUTHOR = SRSHAH

DESCRIPTION = Perform tests on all modules of a distribution
define BLURB
endef

DISTFILES = CSWpmtestdistribution.gspec

PREREQUISITE_PKGS = CSWpmmodulebuild

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include ../category.mk
