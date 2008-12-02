GARNAME = sloccount
GARVERSION = 2.24
CATEGORIES = utils

DESCRIPTION = A suite of programs for counting physical source lines of code.
define BLURB
  SLOCCount is a suite of programs for counting physical source lines of code
  (SLOC) in possibly large software systems. It can count physical SLOC for a
  wide number of languages. It can take a large set of files and automatically
  categorize their types using a number of different heuristics, and also
  comes with analysis tools.
endef

MASTER_SITES = http://www.dwheeler.com/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWsloc.gspec

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Listen to the environment...
PATCHFILES = make.diff

CONFIGURE_SCRIPTS =

# No test suite
TEST_SCRIPTS =

include gar/category.mk

post-extract:
	@( cd $(WORKSRC) ; mv makefile Makefile )
	@$(MAKECOOKIE)
