GARNAME = grep
GARVERSION = 2.6
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
DISTNAME = grep-2.6.7-64540
DISTFILES = $(DISTNAME).tar.xz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS_CSWgrep = CSWggettextrt CSWpcrert

# As suggested in
#   <http://savannah.gnu.org/bugs/?24813>
EXTRA_CFLAGS = -features=extensions

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)
