NAME = rl
VERSION = 0.2.7
CATEGORIES = apps

DESCRIPTION = A command-line tool that randomizes lines of input.
define BLURB
  rl is a command-line tool that reads lines from an input file or stdin, randomizes the
  lines and outputs a specified number of lines. It does this with only a single pass over
  the input while trying to use as little memory as possible.
endef

MASTER_SITES = http://arthurdejong.org/rl/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Add-missing-typedef.patch
PATCHFILES += 0002-Rename-option.patch

# Not gonna do it
# TEST_SCRIPTS =

include gar/category.mk
