NAME = grep
VERSION = 2.14
CATEGORIES = utils
GARTYPE = v2

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
# MASTER_SITES += http://meyering.net/grep/
DISTFILES = $(DISTNAME).tar.xz

PACKAGES = CSWggrep
CATALOGNAME = ggrep
RUNTIME_DEP_PKGS_CSWggrep += CSWlibintl8
RUNTIME_DEP_PKGS_CSWggrep += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWggrep += CSWlibiconv2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += CONFIGURE_ARGS += --with-included-regex

# Use GNUlib for wcscoll as there is an issue with the ru_RU.KOI8-R locale
# See for details http://lists.gnu.org/archive/html/bug-grep/2013-10/msg00020.html
EXTRA_CONFIGURE_ENV += ac_cv_func_wcscoll=no --program-prefix=g

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G)