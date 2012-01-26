NAME = Params-Validate
VERSION = 0.95
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = Validate method/function parameters
define BLURB
  The Params::Validate module allows you to validate method or function call
  parameters to an arbitrary level of specificity. At the simplest level, it
  is capable of validating the required parameters were given and that no
  unspecified additional parameters were passed in.
endef

# CSWpmprmsvldt is the old package. It is empty and depends on the new one.
PACKAGES = CSWpmparamsvalidate CSWpmprmsvldt

CATALOGNAME_CSWpmparamsvalidate = pm_paramsvalidate
CATALOGNAME_CSWpmprmsvldt       = pm_prmsvldt

SPKG_DESC_CSWpmparamsvalidate = $(DESCRIPTION)
SPKG_DESC_CSWpmprmsvldt       = Empty stub depending on new package CSWpmparamsvalidate

RUNTIME_DEP_PKGS_CSWpmprmsvldt = CSWpmparamsvalidate

LICENSE = LICENSE

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

PKGFILES_CSWpmprmsvldt = NOFILES
ARCHALL_CSWpmprmsvldt = 1

include gar/category.mk
