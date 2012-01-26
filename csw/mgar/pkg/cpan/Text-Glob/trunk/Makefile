NAME = Text-Glob
VERSION = 0.09
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RCLAMP

DESCRIPTION = Match globbing patterns against text
define BLURB
endef

DISTFILES = COPYING

PACKAGES = CSWpmtextglob
CATALOGNAME = pm_textglob

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWpmtextglob += catalogname-does-not-match-pkgname|pkgname=CSWpmtextglob|catalogname=pm_textglob|expected-catalogname=pmtextglob

include gar/category.mk
