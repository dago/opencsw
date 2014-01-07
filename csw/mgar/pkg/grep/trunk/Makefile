NAME = grep
VERSION = 2.16
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

MASTER_SIT = $(GNU_MIRROR)
# MASTER_SITES += http://meyering.net/grep/
DISTFILES = $(DISTNAME).tar.xz

PACKAGES = CSWggrep
CATALOGNAME = ggrep
RUNTIME_DEP_PKGS_CSWggrep += CSWlibintl8
RUNTIME_DEP_PKGS_CSWggrep += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWggreNOGITPATCH = 1rep += CSWlibiconv2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += CONFIGURE_ARGS += --with-included-regex
CONFIGURE_ARGS += --enable-gcc-warnings

# Skip tests until this is fixed:
#   http://debbugs.gnu.org/cgi/bugreport.cgi?bug=16380
SKIPTEST ?= 1 --program-prefix=g

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G)