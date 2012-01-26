NAME = Test-Requires
VERSION = 0.06
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TOKUHIROM

DESCRIPTION = Checks to see if the module can be loaded
define BLURB
endef

PACKAGES += CSWpm-test-requires
CATALOGNAME_CSWpm-test-requires = pm_test_requires
ARCHALL_CSWpm-test-requires = 1

# This whole license thing needs to be reworked
CHECKPKG_OVERRIDES_CSWpm-test-requires += license-missing|/opt/csw/share/doc/pm_test_requires/license

include gar/category.mk
