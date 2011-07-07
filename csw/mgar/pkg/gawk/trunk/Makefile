NAME = gawk
VERSION = 4.0.0
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
DISTFILES = $(DISTNAME).tar.xz

PATCHFILES += 0001-Be-not-that-strict-on-standard.patch

RUNTIME_DEP_PKGS_CSWgawk += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgawk += CSWlibsigsegv2
RUNTIME_DEP_PKGS_CSWgawk += CSWlibreadline6

# Otherwise libsigsegv is not detected properly on Solaris 9 i386 as reported in
#   http://lists.gnu.org/archive/html/bug-gnulib/2011-07/msg00008.html
# Also needs the above patch.
EXTRA_CFLAGS = -features=extensions

# These are install instructions for other platforms (os/2... 'nuff said.)
CHECKPKG_OVERRIDES_CSWgawk += file-with-bad-content|/usr/share|root/opt/csw/share/info/gawk.info

# These are instruction for awk, possible adjust them later
CHECKPKG_OVERRIDES_CSWgawk += file-with-bad-content|/usr/local|root/opt/csw/share/info/gawk.info

# This is an example path (YMMV in the docs)
CHECKPKG_OVERRIDES_CSWgawk += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/gawk.1
CHECKPKG_OVERRIDES_CSWgawk += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/pgawk.1

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/g*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)
