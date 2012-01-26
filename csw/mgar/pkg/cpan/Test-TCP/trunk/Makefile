NAME = Test-TCP
VERSION = 1.11
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TOKUHIROM

DESCRIPTION = testing TCP program
define BLURB
endef

PACKAGES += CSWpm-test-tcp
CATALOGNAME_CSWpm-test-tcp = pm_test_tcp
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-test-tcp = 1
RUNTIME_DEP_PKGS_CSWpm-test-tcp = CSWpm-test-sharedfork

# This has not been released yet
CHECKPKG_OVERRIDES_CSWpm-test-tcp += license-missing|/opt/csw/share/doc/pm_test_tcp/license

# There really is no license
CHECKPKG_OVERRIDES_CSWpm-test-tcp += unidentified-dependency|CSWpm-test-sharedfork

include gar/category.mk
