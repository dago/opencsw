NAME = Test-Pod
VERSION = 1.45
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DWHEELER

DESCRIPTION = Check for POD errors in files
define BLURB
  Check POD files for errors or warnings in a test file, using Pod::Simple to
  do the heavy lifting.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-test-pod
CATALOGNAME = pm_test_pod
SPKG_DESC_CSWpm-test-pod = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-test-pod = CSWpmtestpod
CATALOGNAME_CSWpmtestpod = pm_testpod

RUNTIME_DEP_PKGS += CSWpm-pod-simple

ARCHALL = 1

include gar/category.mk
