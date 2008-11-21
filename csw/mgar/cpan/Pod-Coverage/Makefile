GARNAME = Pod-Coverage
GARVERSION = 0.19
CATEGORIES = cpan
AUTHOR = RCLAMP

DESCRIPTION = checks if the documentation of a module is comprehensive
define BLURB
  Developers hate writing documentation. They'd hate it even more if their
  computer tattled on them, but maybe they'll be even more thankful in the
  long run. Even if not, perlmodstyle tells you to, so you must obey.  This
  module provides a mechanism for determining if the pod for a given module is
  comprehensive.
endef

DISTFILES += $(call admfiles,CSWpmpodcoverage,depend)

DEPENDS   += cpan/Devel-Symdump
BUILDDEPS += cpan/Module-Build

include ../category.mk
