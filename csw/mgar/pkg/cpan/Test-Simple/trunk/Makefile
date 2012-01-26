NAME = Test-Simple
VERSION = 0.96
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MSCHWERN

DESCRIPTION = Basic utilities for writing tests
define BLURB
  This is an extremely simple, extremely basic module for writing
  tests suitable for CPAN modules and other pursuits. If you wish
  to do more complicated testing, use the Test::More module
  (a drop-in replacement for this one).
endef

DISTFILES = COPYING

PACKAGES = CSWpmtestsimple
CATALOGNAME = pm_testsimple

ARCHALL = 1

# Skip manpages as they are also in CSWperldoc. See
#   https://www.opencsw.org/mantis/view.php?id=4567
EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3\/.* .*\/man\/man1\/.*

include gar/category.mk
