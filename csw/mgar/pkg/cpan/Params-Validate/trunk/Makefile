GARNAME = Params-Validate
GARVERSION = 0.94
CATEGORIES = cpan
AUTHOR = DROLSKY

DESCRIPTION = $(GARNAME): validate method/function parameters
define BLURB
  The Params::Validate module allows you to validate method or function call
  parameters to an arbitrary level of specificity. At the simplest level, it
  is capable of validating the required parameters were given and that no
  unspecified additional parameters were passed in.
endef

PACKAGES = CSWpmparamsvalidate
CATALOGNAME = pm_paramsvalidate

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

include gar/category.mk

LICENSE = LICENSE
