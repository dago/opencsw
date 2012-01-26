NAME = Test-Differences
VERSION = 0.47
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RBS

DESCRIPTION = test strings and data structures and show differences
define BLURB
  When the code you're testing returns multiple lines, records or data
  structures and they're just plain wrong, an equivalent to the Unix diff
  utility may be just what's needed.
endef

DISTFILES += $(call admfiles,CSWpmtestdiff,depend prototype)

DEPENDS += cpan/Text-Diff

include gar/category.mk
