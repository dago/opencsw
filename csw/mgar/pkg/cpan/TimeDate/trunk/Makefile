NAME = TimeDate
VERSION = 1.20
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GBARR

DESCRIPTION = ASCII Date parser using regexps
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = README

PACKAGES += CSWpm-date-parse
CATALOGNAME_CSWpm-date-parse = pm_date_parse
SPKG_DESC_CSWpm-date-parse = ASCII Date parser using regexps
ARCHALL_CSWpm-date-parse = 1
OBSOLETED_BY_CSWpm-date-parse += CSWpmtimedate
CATALOGNAME_CSWpmtimedate = pm_timedate_stub

# This is for a config file location we don't have at all, maybe we need
# to provide one later:
#   /usr/share/lib/locale/LC_TIME/default
CHECKPKG_OVERRIDES_CSWpm-date-parse += file-with-bad-content|/usr/share|root/opt/csw/share/perl/csw/Date/Format.pm

include gar/category.mk
