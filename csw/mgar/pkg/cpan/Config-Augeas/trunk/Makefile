NAME = Config-Augeas
VERSION = 0.701
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DDUMONT

DESCRIPTION = Augeas Perl Binding
define BLURB
endef

DISTFILES = COPYING
PATCHFILES = 0001-Do-not-use-GCC-flags.patch

PACKAGES = CSWpmconfigaugeas
CATALOGNAME = pm_configaugeas

DEP_PKGS = CSWaugeas

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk
