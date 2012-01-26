NAME = Text-Diff
VERSION = 0.35
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RBS

DESCRIPTION = perform diffs on files and record sets
define BLURB
  diff() provides a basic set of services akin to the GNU diff utility. It is
  not anywhere near as feature complete as GNU diff, but it is better
  integrated with Perl and available on all platforms. It is often faster than
  shelling out to a system's diff executable for small files, and generally
  slower on larger files.
endef

DISTFILES = $(call admfiles,CSWpmtextdiff,depend prototype)

DEPENDS += cpan/Algorithm-Diff

include gar/category.mk
