NAME = Test-Pod
VERSION = 1.44
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DWHEELER

DESCRIPTION = Check for POD errors in files
define BLURB
  Check POD files for errors or warnings in a test file, using Pod::Simple to
  do the heavy lifting.
endef

DISTFILES += COPYING

PACKAGES = CSWpmtestpod
CATALOGNAME = pm_testpod

RUNTIME_DEP_PKGS += CSWpmpodsimple

ARCHALL = 1

include gar/category.mk
