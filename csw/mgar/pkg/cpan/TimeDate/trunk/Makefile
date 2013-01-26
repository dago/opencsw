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

PACKAGES += CSWpm-timedate
SPKG_DESC_CSWpm-timedate = ASCII Date parser using regexps
ARCHALL_CSWpm-timedate = 1
OBSOLETED_BY_CSWpm-timedate += CSWpmtimedate
CATALOGNAME_CSWpmtimedate = pm_timedate_stub
# This name was wrongly guessed by makemake and released
OBSOLETED_BY_CSWpm-timedate += CSWpm-date-parse

# This is for a config file location we don't have at all, maybe we need
# to provide one later:
#   /usr/share/lib/locale/LC_TIME/default
CHECKPKG_OVERRIDES_CSWpm-timedate += file-with-bad-content|/usr/share|root/opt/csw/share/perl/csw/Date/Format.pm

include gar/category.mk
