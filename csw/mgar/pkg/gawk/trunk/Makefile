NAME = gawk
VERSION = 4.1.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = GNU awk
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
DISTFILES = $PATCHFILES += 0001-Add-inclusion-of-mkdev.h-for-major-minor.patch

# Use patch until this is fixed:
#   http://lists.gnu.org/archive/html/bug-gawk/2013-10/msg00000.html
PATCHFILES += 0001-Allow-null-pointer-on-readline-detect.patch $PACKAGES += CSWgawk
SPKG_DESC_CSWgawk = GNU awk
# PKGFILES is catchall$(DISTNAME).tar.xz

RUNTIME_DEP_PKGS_CSWgawk += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgawk += CSWlibsigsegv2
RUNTIME_DEP_PKGS_CSWgawk RUNTIME_DEP_PKGS_CSWgawk += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgawk += CSWlibgmp10 +BUILD64 = 1
ISAEXEC = 1 += CSWlibreadline6

# Otherwise libsigsegv is not detected properly on Solaris 9 i386 as reported in
#   http://lists.gnu.org/archive/html/bug-gnulib/2011-07/msg00008.html
# Additionally, there is probably a bug in /usr/include/ia32/sys/reg.h which requires
# the replacement of uint64_t by upad64_t.
EXTRA_CFLAGS = -Xc -D_XPG4_2 -D/man/man1/pgawk.1

include gar/categot-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/g*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G)