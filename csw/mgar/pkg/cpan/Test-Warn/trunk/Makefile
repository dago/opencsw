NAME = Test-Warn
VERSION = 0.24
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CHORNY

DESCRIPTION = Extension to test methods for warnings
define BLURB
    Extension to test methods for warnings
endef

DISTFILES += COPYING

PACKAGES = CSWpm-test-warn
CATALOGNAME = pm_test_warn
SPKG_DESC_CSWpm-test-warn = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-test-warn = CSWpmtestwarn
CATALOGNAME_CSWpmtestwarn = pm_testwarn_stub
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmtreedagnode
RUNTIME_DEP_PKGS += CSWpm-sub-uplevel

include gar/category.mk
