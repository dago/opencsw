NAME = Test-Simple
VERSION = 0.98
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MSCHWERN

DESCRIPTION = Basic utilities for writing tests.
define BLURB
endef

DISTFILES += COPYING

CATALOG_RELEASE = unstable

PACKAGES += CSWpm-test-simple
CATALOGNAME_CSWpm-test-simple = pm_test_simple
SPKG_DESC_CSWpm-test-simple = Basic utilities for writing tests.
ARCHALL_CSWpm-test-simple = 1
OBSOLETED_BY_CSWpm-test-simple += CSWpmtestsimple
CATALOGNAME_CSWpmtestsimple = pm_testsimple_stub

# Skip manpages as they are also in CSWperldoc. See
#   https://www.opencsw.org/mantis/view.php?id=4567
EXTRA_MERGE_EXCLUDE_FILES += $(mandir)/man3/.*

include gar/category.mk
