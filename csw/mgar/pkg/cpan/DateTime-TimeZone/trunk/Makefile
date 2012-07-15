NAME = DateTime-TimeZone
VERSION = 1.46
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = Time zone object base class and factory
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

BUILD_DEP_PKGS += CSWpm-test-output

PACKAGES += CSWpm-datetime-timezone
CATALOGNAME_CSWpm-datetime-timezone = pm_datetime_timezone
SPKG_DESC_CSWpm-datetime-timezone = Time zone object base class and factory
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-datetime-timezone = 1
RUNTIME_DEP_PKGS_CSWpm-datetime-timezone += CSWpm-params-validate
RUNTIME_DEP_PKGS_CSWpm-datetime-timezone += CSWpm-class-load
RUNTIME_DEP_PKGS_CSWpm-datetime-timezone += CSWpm-class-singleton
OBSOLETED_BY_CSWpm-datetime-timezone += CSWpmdatetimetz
CATALOGNAME_CSWpmdatetimetz = pm_datetimetz_stub

REINPLACEMENTS += zoneinfo
REINPLACE_MATCH_zoneinfo = /usr/share/zoneinfo
REINPLACE_WITH_zoneinfo = /usr/share/lib/zoneinfo
REINPLACE_FILES_zoneinfo += t/04local.t
REINPLACE_FILES_zoneinfo += tools/update-from-latest-olson
REINPLACE_FILES_zoneinfo += tools/compile-all-zones
REINPLACE_FILES_zoneinfo += tools/tests_from_zdump
REINPLACE_FILES_zoneinfo += lib/DateTime/TimeZone/Local/Unix.pm

# This is in fact /usr/share/lib/zoneinfo which is ok
CHECKPKG_OVERRIDES_CSWpm-datetime-timezone += file-with-bad-content|/usr/share|root/opt/csw/share/perl/csw/DateTime/TimeZone/Local/Unix.pm
CHECKPKG_OVERRIDES_CSWpm-datetime-timezone += file-with-bad-content|/usr/share|root/opt/csw/share/man/man3/DateTime::TimeZone::Local::Unix.3perl

include gar/category.mk
