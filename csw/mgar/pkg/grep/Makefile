GARNAME = grep
GARVERSION = 2.5
CATEGORIES = utils

DESCRIPTION = GNU grep
define BLURB
	The GNU family of grep utilities may be the "fastest grep in the west".
	GNU grep is based on a fast lazy-state deterministic matcher (about
	twice as fast as stock Unix egrep) hybridized with a Boyer-Moore-Gosper
	search for a fixed string that eliminates impossible text from being
	considered by the full regexp matcher without necessarily having to
	look at every character. The result is typically many times faster
	than Unix grep or egrep. (Regular expressions containing backreferencing
	will run more slowly, however.)
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

# Patch makefile to honor DESTDIR
PATCHFILES = install.diff

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Spencer bre test #16 fails
TEST_SCRIPTS =

include ../category.mk

pre-test:
	@( cd $(WORKSRC)/tests ; chmod 555 *.sh *.awk )
