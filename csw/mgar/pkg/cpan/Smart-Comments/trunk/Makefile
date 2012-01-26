NAME = Smart-Comments
VERSION = 1.0.4
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = CHORNY

DESCRIPTION = Smart::Comments - Comments that do more than just sit there
define BLURB
	Smart comments provide an easy way to insert debugging and tracking code into a
	program. They can report the value of a variable, track the progress of a loop,
	and verify that particular assertions are true.

	Best of all, when you're finished debugging, you don't have to remove them.
	Simply commenting out the use Smart::Comments line turns them back into regular
	comments. Leaving smart comments in your code is smart because if you needed
	them once, you'll almost certainly need them again later.
endef

PACKAGES = CSWpmsmartcomments
CATALOGNAME = pm_smartcomments

ARCHALL = 1
LICENSE = README

RUNTIME_DEP_PKGS = CSWpmversion
BUILD_DEP_PKGS += CSWpmtestpodcoverage
BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS)

include gar/category.mk
