GARNAME = rl
GARVERSION = 0.2.6
CATEGORIES = apps

DESCRIPTION = A command-line tool that randomizes lines of input.
define BLURB
  rl is a command-line tool that reads lines from an input file or stdin, randomizes the lines and outputs a specified number of lines. It does this with only a single pass over the input while trying to use as little memory as possible.
endef

MASTER_SITES = http://ch.tudelft.nl/~arthur/rl/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWrl,)

CONFIGURE_ARGS = $(DIRPATHS)
# Not gonna do it
TEST_SCRIPTS =


include ../category.mk
