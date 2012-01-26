NAME = bison
VERSION = 2.5
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = GNU Project parser generator (yacc replacement)
define BLURB
  Bison is a parser generator in the style of yacc(1). It should be upwardly
  compatible with input files designed for yacc.
endef

MASTER_SITES = $(GNU_MIRROR)
# MASTER_SITES += http://alpha.gnu.org/gnu/bison/

DISTFILES = $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS_CSWbison += CSWlibintl8
RUNTIME_DEP_PKGS_CSWbison += CSWiconv
RUNTIME_DEP_PKGS_CSWbison += CSWgm4

VENDOR_URL = http://www.gnu.org/software/bison/

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset\.alias

# I guess we really need these
CHECKPKG_OVERRIDES_CSWbison += surplus-dependency|CSWgm4
CHECKPKG_OVERRIDES_CSWbison += surplus-dependency|CSWiconv

# Skip tests as some fail due to problems in CSWlibgnugetopt includes
SKIPTEST ?= 1

include gar/category.mk

# Must use GNU grep during test
PATH := /opt/csw/gnu:$(PATH)

post-install-modulated:
	mv $(DESTDIR)$(bindir)/yacc $(DESTDIR)$(bindir)/gyacc
	ginstall -d $(DESTDIR)$(prefix)/gnu
	ln -s ../bin/gyacc $(DESTDIR)$(prefix)/gnu/yacc
	perl -pi \
		-e 's,/usr/local,$(prefix),g' \
		$(DESTDIR)$(infodir)/bison.info
	@$(MAKECOOKIE)
