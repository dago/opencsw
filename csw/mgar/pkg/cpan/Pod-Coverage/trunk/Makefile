NAME = Pod-Coverage
VERSION = 0.20
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RCLAMP

DESCRIPTION = Checks if the documentation of a module is comprehensive
define BLURB
  Developers hate writing documentation. They'd hate it even more if their
  computer tattled on them, but maybe they'll be even more thankful in the
  long run. Even if not, perlmodstyle tells you to, so you must obey.  This
  module provides a mechanism for determining if the pod for a given module is
  comprehensive.
endef

BUILD_DEP_PKGS = CSWpmmodulebuild CSWpmtestpod
RUNTIME_DEP_PKGS = CSWpmdevelsymdump

DISTFILES = COPYING

PACKAGES = CSWpmpodcoverage
CATALOGNAME = pm_podcoverage

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWpmpodcoverage += surplus-dependency|CSWpmdevelsymdump

include gar/category.mk
