GARNAME = Array-Compare
GARVERSION = 1.13
CATEGORIES = cpan
AUTHOR = DAVECROSS

DESCRIPTION = extension for comparing arrays.
define BLURB
  If you have two arrays and you want to know if they are the same or
  different, then Array::Compare will be useful to you.
endef

DISTFILES += CSWpmarraycompare.gspec CSWpmarraycompare.depend

DEPENDS += cpan/Module-Build

# Setup for Module::Build
BUILD_PL = $(WORKSRC)/Build
CONFIGURE_SCRIPTS = $(BUILD_PL).PL
BUILD_SCRIPTS = $(BUILD_PL)
TEST_SCRIPTS = $(BUILD_PL)
INSTALL_SCRIPTS = $(BUILD_PL)

include gar/category.mk
