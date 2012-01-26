NAME = DateTime-TimeZone
VERSION = 1.16
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = Time zone object base class and factory
define BLURB
  This class is the base class for all time zone objects. A time zone is
  represented internally as a set of observances, each of which describes
  the offset from GMT for a given time period.  Note that without the
  DateTime.pm module, this module does not do much. It's primary interface
  is through a DateTime object, and most users will not need to directly
  use DateTime::TimeZone methods.
endef

PACKAGES = CSWpmdatetimetz
CATALOGNAME = pm_datetimetz

LICENSE = LICENSE

ARCHALL = 1

DEP_PKGS = CSWpmclasssingleton CSWpmparamsvalidate

CHECKPKG_OVERRIDES_CSWpmdatetimetz += surplus-dependency|CSWpmclasssingleton
CHECKPKG_OVERRIDES_CSWpmdatetimetz += surplus-dependency|CSWpmparamsvalidate

include gar/category.mk

