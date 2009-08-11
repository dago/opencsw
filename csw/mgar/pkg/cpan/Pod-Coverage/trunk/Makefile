GARNAME = Pod-Coverage
GARVERSION = 0.20
CATEGORIES = cpan
AUTHOR = RCLAMP

DESCRIPTION = Checks if the documentation of a module is comprehensive
define BLURB
  Developers hate writing documentation. They'd hate it even more if their
  computer tattled on them, but maybe they'll be even more thankful in the
  long run. Even if not, perlmodstyle tells you to, so you must obey.  This
  module provides a mechanism for determining if the pod for a given module is
  comprehensive.
endef

PREREQUISITE_PKS = CSWpmmodulebuild CSWpmtestpod
REQUIRED_PKGS = CSWpmdevelsymdump

DISTFILES = COPYING

PACKAGES = CSWpmpodcoverage
CATALOGNAME = pm_podcoverage

ARCHALL = 1

include gar/category.mk
