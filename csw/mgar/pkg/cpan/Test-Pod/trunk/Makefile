GARNAME = Test-Pod
GARVERSION = 1.41
CATEGORIES = cpan
AUTHOR = PETDANCE

DESCRIPTION = Check for POD errors in files
define BLURB
  Check POD files for errors or warnings in a test file, using Pod::Simple to
  do the heavy lifting.
endef

PACKAGES = CSWpmtestpod
CATALOGNAME = pm_testpod

REQUIRED_PKGS = CSWpmiostringy CSWpmpodsimple
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWpmtestsimple

ARCHALL = 1

include gar/category.mk
